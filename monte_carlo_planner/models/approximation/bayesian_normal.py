import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Simulate some data
np.random.seed(42)
true_mean = 5
true_std = 2
n = 100
data = np.random.normal(true_mean, true_std, n)

# Prior parameters
mu_0 = 0  # Prior mean
sigma_0_sq = 1  # Prior variance

# Known data variance (for simplicity, we assume it's known)
sigma_sq = true_std ** 2

# Calculate posterior parameters
n = len(data)
x_bar = np.mean(data)
mu_N = (sigma_sq * mu_0 + n * sigma_0_sq * x_bar) / (sigma_sq + n * sigma_0_sq)
sigma_N_sq = 1 / (1 / sigma_0_sq + n / sigma_sq)

# Generate values for plotting
x = np.linspace(-2, 12, 500)

# Plotting the prior
prior = stats.norm.pdf(x, mu_0, np.sqrt(sigma_0_sq))
plt.plot(x, prior, label='Prior', c='blue')

# Plotting the likelihood
likelihood = stats.norm.pdf(x, x_bar, np.sqrt(sigma_sq/n))
plt.plot(x, likelihood, label='Likelihood', c='green')

# Plotting the posterior
posterior = stats.norm.pdf(x, mu_N, np.sqrt(sigma_N_sq))
plt.plot(x, posterior, label='Posterior', c='red')

plt.title('Bayesian Estimation of Normal Mean')
plt.xlabel('Mean')
plt.ylabel('Density')
plt.legend()
plt.show()

print(f"Posterior Mean: {mu_N}, Posterior Variance: {sigma_N_sq}")
