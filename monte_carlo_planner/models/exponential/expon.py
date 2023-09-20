import ctypes
import os

# Load the shared library
exp_distribution = ctypes.CDLL('G:\\montecarlo_planner\\monte_carlo_planner\\models\\exponential\\expon.so')  

# Specify the argument types and return type for the C function
exp_distribution.generate_two_param_exponential.argtypes = [ctypes.c_double, ctypes.c_double]
exp_distribution.generate_two_param_exponential.restype = ctypes.c_double

def generate_two_param_exponential(alpha:float, beta:float)->float:
    """
    The function returns a random number from a two-parameter exponential distribution

    Args:
        alpha (float): First parameter of the exponential distribution
        beta (float): Second parameter of the exponential distribution

    Returns:
        float: A random number from a two-parameter exponential distribution

    """
    return exp_distribution.generate_two_param_exponential(ctypes.c_double(alpha), ctypes.c_double(beta))
