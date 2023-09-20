from monte_carlo_planner.models.exponential.expon import *
from typing import List 
def exponential_distribution(num_samples:int,alpha:float,beta:float)->List[float]:
    """
    The function returns a list of random numbers from a two-parameter exponential distribution

    Args:
        num_samples (int): Number of samples
        alpha (float): First parameter of the exponential distribution
        beta (float): Second parameter of the exponential distribution

    Returns:
        List[float]: List of random numbers from a two-parameter exponential distribution
    
    """
    data = []
    for _ in range(num_samples): 
        x = generate_two_param_exponential(alpha,beta)
        data.append(x)
    return data
"""
import matplotlib.pyplot as plt
# Initialize parameters
alpha = 1  # first parameter
beta = 2 # second parameter
num_samples = 10000
# Generate data
data = exponential_distribution(num_samples,alpha,beta)
plt.hist(data, bins=50, density=True, alpha=0.6, color='g')
plt.show()
"""