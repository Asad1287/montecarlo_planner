import numpy as np
from scipy.optimize import minimize

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

def fit_distribution_mle(data, distr='normal'):
    if distr == 'normal':
        initial_params = [np.mean(data), np.std(data)]
        result = minimize(normal_log_likelihood, initial_params, args=(data,))
    elif distr == 'weibull':
        initial_params = [1.0, 1.0]  # Arbitrary initial values
        result = minimize(weibull_log_likelihood, initial_params, args=(data,))
    elif distr == 'lognormal':
        initial_params = [0.0, 1.0]  # Arbitrary initial values
        result = minimize(lognormal_log_likelihood, initial_params, args=(data,))
    elif distr == 'exponential':
        initial_params = [1.0]  # Arbitrary initial value
        result = minimize(exponential_log_likelihood, initial_params, args=(data,))
    else:
        raise ValueError("Unknown distribution")

    # Extract optimized parameters
    params_optimized = result.x
    return f"{distr.capitalize()}({', '.join(map(lambda x: f'{x:.2f}', params_optimized))})"

# Example data
data = np.array([8.9, 9.8, 10.5, 10.1, 9.9, 9.7, 10.2, 10.0, 9.8])

# Fit different distributions
for distr in ['normal', 'weibull', 'lognormal', 'exponential']:
    print(f"Best-fit for {distr}: {fit_distribution_mle(data, distr=distr)}")
