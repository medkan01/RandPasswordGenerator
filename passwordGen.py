import random

def randInt(lb, ub):
    """
        Return integer between lb and ub

    Args:
    
        lb (int): lower bound
        
        ub (int): upper bound
    """
    return random.randint(lb, ub)

def generator(lowercase = True, uppercase = False, number = False, symbol = False):
    """
        Generate random password with the differents arguments needed
        
        Default: Only lowercases are selected

    Args:
    
        lowercase ([type]): [description]
        
        uppercase ([type]): [description]
        
        number ([type]): [description]
        
        symbol ([type]): [description]
    """