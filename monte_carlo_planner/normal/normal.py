from typing import List 
from box_muller import box_muller

def normal_distribution(num_samples:int,mean:float,std:float)->List[float]:

    """
    The function returns a list of random numbers from a normal distribution

    Args:
        num_samples (int): Number of samples
        mean (float): Mean of the normal distribution
        std (float): Standard deviation of the normal distribution
    Returns:
        List[float]: List of random numbers from a normal distribution
    
    """
    data = []
    for _ in range(num_samples // 2): 
        z1, z2 = box_muller()
        x1 = mean + z1 * std
        x2 = mean + z2 * std
        data.extend([x1, x2])
    return data

import matplotlib.pyplot as plt
# Initialize parameters
mu = 0  # mean
sigma = 1  # standard deviation
num_samples = 10000
# Generate data
data = normal_distribution(num_samples,mu,sigma)
# Convert to NumPy array for easier handling

# Plot the histogram
plt.hist(data, bins=50, density=True, alpha=0.6, color='g')
# Plot a standard normal distribution for comparison
plt.show()  

