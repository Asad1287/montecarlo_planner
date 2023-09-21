from scipy.stats import norm, expon, lognorm, weibull_min, gamma
from scipy import stats
from typing import List,Dict
import numpy as np
import matplotlib.pyplot as plt
import sys 
sys.path.append('G:\\montecarlo_planner\\monte_carlo_planner')


from models.approximation.generate_summaries import *
from models.approximation.mle import *
from distr_parser.parserfunction import *

def monte_carlo_runner(expression: str, variable_distributions: Dict[str, str], n_iterations: int = 100000) -> np.ndarray:
    """
    Run a Monte Carlo simulation for the given expression and variable distributions.

    Parameters
    ----------
    expression : str
        A string representing the expression to be evaluated
    variable_distributions : Dict[str, str]
        A dictionary mapping variable names to their distribution specifications
    n_iterations : int, optional
        Number of Monte Carlo iterations to run, by default 100000
    
    Returns 
    -------
    np.ndarray
        A NumPy array containing the results of the Monte Carlo simulation
    """

    # Initialize a list to hold the Monte Carlo results
    results = []

    #for each value of variable_distribution pass it to the distr_parser function
    for key, value in variable_distributions.items():
        variable_distributions[key] = parse_distribution(value)
    
    # Run Monte Carlo iterations
    for _ in range(n_iterations):
        # Generate samples for each variable from its distribution, if its a static value, just use that value
        variable_values = {k: v.rvs() if hasattr(v, 'rvs') else v for k, v in variable_distributions.items()}        
        # Evaluate the expression for the current sample
        result = parser(expression, variable_values)
        
        # Store the result
        results.append(result)
        
    # Convert results to a NumPy array for easier analysis
    results = np.array(results)
    


    return results

# Example usage

if __name__ == "__main__":

    expression = 'Variable1 + Variable2'
    variable_distributions = {
        'Variable1': 10.0,
        'Variable2': 'NORM(50,1)',
    }



    results = monte_carlo_runner(expression, variable_distributions)


    print( describe_distribution(results) )
