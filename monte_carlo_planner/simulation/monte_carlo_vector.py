import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, lognorm, weibull_min, gamma
import sys 
sys.path.append('G:\\montecarlo_planner\\monte_carlo_planner')


from models.approximation.generate_summaries import *
from models.approximation.mle import *
from distr_parser.parserfunction import *
# Function to parse distribution strings
# Gibbs sampler for two distributions
def gibbs_sampler_two_distrbution(iterations, distribution_X, distribution_Y, operator='+'):
    x_samples = distribution_X.rvs(iterations)
    y_samples = distribution_Y.rvs(iterations)

    if operator == '+':
        return x_samples + y_samples
    elif operator == '-':
        return x_samples - y_samples
    elif operator == '*':
        return x_samples * y_samples
    elif operator == '/':
        return x_samples / y_samples

# Process the input object
def process_input_object(input_object, iterations):
    vector1_str = input_object['vector1']
    vector2_str = input_object['vector2']
    operations = input_object['operations']
    
    vector1_distr = [parse_distribution(d) for d in vector1_str]
    vector2_distr = [parse_distribution(d) for d in vector2_str]
    
    # Initialize an array for the accumulated result
    accumulated_result = np.zeros(iterations)
    
    for v1, v2, op in zip(vector1_distr, vector2_distr, operations):
        result_vector = gibbs_sampler_two_distrbution(iterations, v1, v2, operator=op)
        
        # Accumulate the result component-wise
        accumulated_result += result_vector
    
    return accumulated_result

# Define the input object
input_object = {
    'vector1': ['NORM(20,4)', 'NORM(50,6)', 'NORM(20,5)'],
    'vector2': ['NORM(30,2)', 'NORM(30,5)', 'NORM(60,6)'],
    'operations': ['*', '*', '*']
}

iterations = 50000
accumulated_result = process_input_object(input_object, iterations)

# Plotting the accumulated distribution
plt.hist(accumulated_result, bins=50, density=True, alpha=0.6, label='Accumulated Result')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()