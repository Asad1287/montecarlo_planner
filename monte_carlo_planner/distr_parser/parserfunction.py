from scipy.stats import norm, expon, lognorm, weibull_min, gamma
from scipy import stats
from typing import List
import sys




def parse_distribution(distr_str: str) -> stats._distn_infrastructure.rv_frozen:

    """
    The function takes in a string and returns a distribution object

    Parameters
    ----------
    distr_str : str
        A string representing a distribution
    Returns 
    -------
    stats._distn_infrastructure.rv_frozen
    
    """
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

# List of distribution specification strings
distr_strings = ['EXP(10,1)', 'NORM(10,1)', 'NORM(10,1)']

# Convert list of strings to list of scipy.stats distribution objects
distr_objects = [parse_distribution(distr_str) for distr_str in distr_strings]

# Test to see if the list of distributions was created successfully


for i, distr in enumerate(distr_objects):
    print(f"Object {i+1}: mean = {distr.mean()}, std = {distr.std()}")

    
def tokenize(expression: str) -> List[str]:
    """
    The function takes in a string and returns a list of tokens

    Parameters
    ----------
    expression : str
        A string representing an expression
    Returns
    -------
    List[str]

    
    """
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

def parse_and_evaluate(tokens: List[str], variable_values: dict) -> float:
    """
    The function takes in a list of tokens and a dictionary of variable values and returns the result of the expression

    Parameters
    ----------
    tokens : List[str]
        A list of tokens
    variable_values : dict
        A dictionary of variable values
    Returns
    -------
    float


    """
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

#test tokenize
test_expression = '1+2'
test_result = tokenize(test_expression)
print(f"test_result_tokenize: {test_result}")

def parser(expression, variable_values):
    tokens = tokenize(expression)
    result = parse_and_evaluate(tokens, variable_values)
    return result

#test parser
test_expression = '1+2'
test_variable_values = {'1':1,'2':2}
test_result = parser(test_expression,test_variable_values)
print(f"test_result_parser: {test_result}")