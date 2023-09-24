import numpy as np
from scipy.optimize import minimize
from scipy import stats as ss 
# Normal log-likelihood
def normal_log_likelihood(params, data):
    mu, sigma = params
    n = len(data)
    return -(-0.5 * n * np.log(2 * np.pi) - n * np.log(sigma) - (1 / (2 * sigma**2)) * np.sum((data - mu)**2))

# Weibull log-likelihood
def weibull_log_likelihood(params, data):
    k, lam = params
    n = len(data)
    return - (n * np.log(k) + n * k * np.log(lam) - k * np.sum(np.log(data)) - np.sum((data / lam)**k))

# Log-Normal log-likelihood
def lognormal_log_likelihood(params, data):
    mu, sigma = params
    n = len(data)
    return - (-0.5 * n * np.log(2 * np.pi) - n * np.log(sigma) - (1 / (2 * sigma**2)) * np.sum((np.log(data) - mu)**2))

# Exponential log-likelihood
def exponential_log_likelihood(params, data):
    lam = params[0]
    n = len(data)
    return - (n * np.log(lam) - lam * np.sum(data))

def fit_best_distribution(data):
    """
    Fit a list of distributions to the given data and return the best fitting distribution along with its parameters.
    """
    # Define the list of distributions to try
    distributions = [ss.norm, ss.expon, ss.lognorm, ss.weibull_min]
    
    # Set up variables to store the best fitting distribution and its parameters
    best_distribution = None
    best_params = None
    best_sse = np.inf
    
    # Estimate distribution parameters from data
    for distribution in distributions:
        # Try to fit the distribution
        try:
            # Ignore warnings from data that can't be fit
            with np.errstate(all='ignore'):
                params = distribution.fit(data)
                arg = params[:-2]
                loc = params[-2]
                scale = params[-1]
                
                # Calculate the sum of squared error (SSE) for the fitted distribution
                pdf = distribution.pdf(data, loc=loc, scale=scale, *arg)
                sse = np.sum((pdf - data)**2)
                
                # If the SSE is smaller than the best one so far, store this distribution and its parameters
                if sse < best_sse:
                    best_distribution = distribution
                    best_params = params
                    best_sse = sse
                    
        except Exception as e:
            print(f"Error fitting {distribution.name}: {e}")
            pass
    
        resultstring = f"Best fit distribution: {best_distribution.name} with parameters {best_params}"
    return resultstring


