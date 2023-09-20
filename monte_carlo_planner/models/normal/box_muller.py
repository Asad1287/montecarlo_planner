import ctypes
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
# Load the shared library
box_muller_lib = ctypes.CDLL('monte_carlo_planner\models\\normal\\box_muller.so')

# Declare the return type and argument types of the C function
box_muller_lib.box_muller.restype = None
box_muller_lib.box_muller.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

def box_muller() -> Tuple[float, float]:
    """
    The function returns two random numbers from a standard normal distribution
    using the Box-Muller algorithm.

    Returns:
        Tuple[float, float]: Two random numbers from a standard normal distribution

    """
    z1 = ctypes.c_double()
    z2 = ctypes.c_double()
    box_muller_lib.box_muller(ctypes.byref(z1), ctypes.byref(z2))
    return z1.value, z2.value
