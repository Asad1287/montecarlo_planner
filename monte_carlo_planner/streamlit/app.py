import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import sys
import os

# Get the current script's directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# Get the parent directory
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

# Append the parent directory to sys.path
sys.path.append(parent_directory)
from models.approximation.mle import *

# Function to run Monte Carlo simulation
def monte_carlo_runner(expression, variable_distributions):
    # Placeholder function. Replace with actual implementation
    return np.random.normal(size=1000)

# Function to describe distribution
def describe_distribution(data):
    # Placeholder function. Replace with actual implementation
    return "Description of distribution"

# Streamlit UI
st.title("Monte Carlo Simulation App")

# Get user input
st.title("Enter the expression and number of variables")

# Get user input
expression = st.text_input("Enter the expression:", 'Variable1 + Variable2')
num_variables = st.number_input("Enter the number of variables", min_value=2, value=2, step=1)


# Set variable distributions
variable_distributions = {}
for i in range(1, num_variables + 1):
    variable_name = f'Variable{i}'
    variable_distribution = st.text_input(f"Enter the distribution for {variable_name}:", 'NORM(50,1)')
    variable_distributions[variable_name] = variable_distribution

# Run Monte Carlo simulation and get results
if st.button("Run Simulation"):
    results = monte_carlo_runner(expression, variable_distributions)
    #fit the distribution using MLE
    # Fit different distributions
    
    best_dist = fit_best_distribution(results)
    
    # Display description and plot histogram
    st.text(describe_distribution(results))
    st.text(best_dist)
    fig, ax = plt.subplots()
    ax.hist(results, bins=30, density=True, alpha=0.6, color='g')
    st.pyplot(fig)
