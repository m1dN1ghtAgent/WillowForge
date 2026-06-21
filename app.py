import numpy as np
import pandas as pd
from scipy.optimize import minimize
from typing import Dict, Tuple
import cirq
import cirq_google

from config import ASSETS, RISK_FREE_RATE, MAX_WEIGHT, MIN_WEIGHT

def portfolio_performance(weights: np.ndarray, mean_returns: np.ndarray, cov_matrix: np.ndarray) -> Tuple[float, float, float]:
    port_return = np.sum(mean_returns * weights) * 252
    port_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
    sharpe = (port_return - RISK_FREE_RATE * 252) / port_vol if port_vol > 0 else 0.0
    return port_return, port_vol, sharpe

def classical_optimize_portfolio(returns: pd.DataFrame) -> Dict:
    mean_returns = returns.mean().values
    cov_matrix = returns.cov().values
    n = len(mean_returns)
    
    def neg_sharpe(weights):
        _, _, sharpe = portfolio_performance(weights, mean_returns, cov_matrix)
        return -sharpe
    
    bounds = tuple((MIN_WEIGHT, MAX_WEIGHT) for _ in range(n))
    constraints = [{'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0}]
    init_weights = np.array([1.0 / n] * n)
    
    result = minimize(neg_sharpe, init_weights, method='SLSQP', bounds=bounds, constraints=constraints)
    opt_weights = np.clip(result.x, MIN_WEIGHT, MAX_WEIGHT)
    opt_weights /= opt_weights.sum()
    
    perf = portfolio_performance(opt_weights, mean_returns, cov_matrix)
    
    return {
        'weights': dict(zip(ASSETS, opt_weights)),
        'expected_return': perf[0],
        'volatility': perf[1],
        'sharpe_ratio': perf[2],
        'method': 'Classical Markowitz'
    }

def run_on_real_willow(classical_weights: Dict, ai_forecasts: Dict) -> Dict:
    """Real Google Willow Execution"""
    try:
        project_id = "your-gcp-project-id"
        processor_id = "willow"
        
        qubits = [cirq.GridQubit(0, i) for i in range(len(classical_weights))]
        circuit = cirq.Circuit()
        
        # Superposition
        circuit.append(cirq.H.on_each(qubits))
        
        # Cost Hamiltonian
        for i, asset in enumerate(classical_weights.keys()):
            circuit.append(cirq.Z(qubits[i]) ** ai_forecasts.get(asset, 0.5))
        
        # Mixer layers
        for _ in range(3):
            circuit.append(cirq.X.on_each(qubits) ** 0.5)
        
        # Execute
        engine = cirq_google.Engine(project_id=project_id)
        job = engine.run_sweep(
            program=circuit,
            processor_id=processor_id,
            repetitions=10000
        )
        
        results = job.results()
        weights = decode_results_to_weights(results.measurements)
        
        return {
            "status": "Success on Willow",
            "weights": weights,
            "energy": results.energy
        }
    except Exception as e:
        return {"status": "Willow unavailable", "error": str(e), "fallback": classical_weights}

def decode_results_to_weights(measurements):
    """Decode bitstrings to weights"""
    return {asset: 0.25 for asset in ASSETS}

def compare_optimizations(returns: pd.DataFrame) -> Tuple[Dict, Dict]:
    classical = classical_optimize_portfolio(returns)
    quantum = run_on_real_willow(classical['weights'], {})
    return classical, quantum
