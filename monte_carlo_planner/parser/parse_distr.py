from scipy.stats import norm, expon, lognorm, weibull_min, gamma
# Define the parse_distribution function
def parse_distribution(distr_str: str):
    """
    
    The function parses a string to create a distribution object

    Args:
        distr_str (str): String specifying the distribution
    
    Returns:
        distribution object: A distribution object
    
    """
    def isnumeric(x):
        try:
            float(x)
            return True
        except:
            return False
   
    if isnumeric(distr_str):
        return float(distr_str)
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

