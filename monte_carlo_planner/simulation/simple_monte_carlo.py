from scipy.stats import norm, expon, lognorm, weibull_min, gamma
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('D:\\RealProject\\capital_planning_simulator\\src')

from models.approximation.generate_summaries import *
from models.approximation.mle import *

# Define the parse_distribution function
def parse_distribution(distr_str):
    def isnumeric(x):
        try:
            float(x)
            return True
        except:
            return False
    #if distr_str is a numerical value, return it as is
    if isnumeric(distr_str):
        return float(distr_str)
    # Remove spaces
    distr_str = distr_str.replace(" ", "")
    # Find the type of distribution
    distr_type = distr_str.split("(")[0].upper()
    # Extract parameters
    params = [float(x) for x in distr_str.split("(")[1].rstrip(")").split(",")]
    
    if distr_type == "NORM":
        return norm(loc=params[0], scale=params[1])
    elif distr_type == "EXP":
        return expon(scale=params[0])
    elif distr_type == "LOGNORMAL":
        return lognorm(params[0], scale=params[1])
    elif distr_type == "WEIBULL":
        return weibull_min(params[0], scale=params[1])
    elif distr_type == "GAMMA":
        return gamma(params[0], scale=params[1])
    else:
        raise ValueError(f"Unknown distribution type: {distr_type}")
    
def tokenize(expression):
    tokens = []
    token = ""
    for char in expression:
        if char == ' ':
            continue
        elif char in ['*', '/', '+', '-', ',', '(', ')']:
            if token:
                tokens.append(token)
                token = ""
            tokens.append(char)
        else:
            token += char
    if token:
        tokens.append(token)
    return tokens

def parse_and_evaluate(tokens, variable_values):
    operands = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}

    for token in tokens:
        if token in variable_values:
            operands.append(variable_values[token])
        elif token in ['+', '-', '*', '/']:
            while operators and precedence[operators[-1]] >= precedence[token]:
                operator = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                if operator == '+':
                    operands.append(operand1 + operand2)
                elif operator == '-':
                    operands.append(operand1 - operand2)
                elif operator == '*':
                    operands.append(operand1 * operand2)
                elif operator == '/':
                    operands.append(operand1 / operand2)
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                operator = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                if operator == '+':
                    operands.append(operand1 + operand2)
                elif operator == '-':
                    operands.append(operand1 - operand2)
                elif operator == '*':
                    operands.append(operand1 * operand2)
                elif operator == '/':
                    operands.append(operand1 / operand2)
            operators.pop()  # Remove the '(' from the stack
        elif token == ',':
            continue  # Assuming ',' is a separator, just ignore it for this case
        else:
            operands.append(float(token))

    while operators:
        operator = operators.pop()
        operand2 = operands.pop()
        operand1 = operands.pop()
        if operator == '+':
            operands.append(operand1 + operand2)
        elif operator == '-':
            operands.append(operand1 - operand2)
        elif operator == '*':
            operands.append(operand1 * operand2)
        elif operator == '/':
            operands.append(operand1 / operand2)
    
    return operands[0]  # The result should be the only element left in the operands list


def parser(expression, variable_values):
    tokens = tokenize(expression)
    result = parse_and_evaluate(tokens, variable_values)
    return result

def monte_carlo_runner(expression, variable_distributions, n_iterations=10000):
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
expression = 'Variable1 + Variable2'
variable_distributions = {
    'Variable1': 10.0,
    'Variable2': 'NORM(50,1)',
  }



results = monte_carlo_runner(expression, variable_distributions)


print( describe_distribution(results) )
