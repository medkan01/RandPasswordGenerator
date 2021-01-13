import random

ASCII_LB = 31
ASCII_UB = 126

def randInt(lb, ub):
    """
        Generate random integer in range [ lb ; ub ].

    Args:
    
        lb (int): Lower bound.
        
        ub (int): Upper bound.

    Returns:
    
        - int: Random integer.
    """
    return random.randint(lb, ub)

def randomAscii():
    """
        Generate random ASCII character.

    Returns:
    
        - str: ASCII character.
    """
    return chr(randInt(ASCII_LB, ASCII_UB))

def isNumberAscii(str):
    if(str >= 48 and str <= 57):
        return True
    else:
        return False

def isLowercaseAscii(str):
    if(str >= 97 and str <= 121):
        return True
    else:
        return False
    
def isUppercaseAscii(str):
    if(str >= 65 and str <= 90):
        return True
    else:
        return False

def isSymbolAscii(str):
    if(str >= 33 and str <= 126 and isNumberAscii(str) == False and isLowercaseAscii(str) == False and isUppercaseAscii(str) == False):
        return True
    else:
        return False

def generator(size, lowercase = True, uppercase = False, number = False, symbol = False):
    password = ""
    for i in range(size):
        char = randomAscii()
        if( lowercase and isLowercaseAscii(char) ):
            password += char
        elif( uppercase and isUppercaseAscii(char) ):
            password += char
        elif( number and isNumberAscii(char) ):
            password += char
        elif( symbol and isSymbolAscii(char) ):
            password += char
    return password