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
    
        - str: Random ASCII character.
    """
    
    return chr(randInt(ASCII_LB, ASCII_UB))

def isNumberAscii(char):
    """
        Test if character is a number in Ascii table

    Args:
    
        - char (str): Character to test

    Returns:
    
        - bool: Result of the test
    """
    
    if(ord(char) >= 48 and ord(char) <= 57):
        return True
    else:
        return False

def isLowercaseAscii(char):
    """
        Test if character is a lowercase letter in Ascii table

    Args:
    
        - char (str): Character to test

    Returns:
    
        - bool: Result of the test
    """
    
    if(ord(char) >= 97 and ord(char) <= 121):
        return True
    else:
        return False
    
def isUppercaseAscii(char):
    """
        Test if character is an uppercase letter in Ascii table
        
    Args:
    
        - char (str): Character to test

    Returns:
    
        - bool: Result of the test
    """
    
    if(ord(char) >= 65 and ord(char) <= 90):
        return True
    else:
        return False

def isSymbolAscii(char):
    """
        Test if character is a symbol in Ascii table

    Args:
    
        - char (str): Character to test

    Returns:
    
        - bool: Result of the test
    """
    
    if(ord(char) >= 33 and ord(char) <= 126 and isNumberAscii(char) == False and isLowercaseAscii(char) == False and isUppercaseAscii(char) == False):
        return True
    else:
        return False

def generator(size, lowercase = True, uppercase = False, number = False, symbol = False):
    """
        Generate a password with the wanted size and the wanted characters.

    Args:
    
        size (int): Size of the password.
        
        lowercase (bool, optional): Generate password with lowercase letter. Defaults to True.
        
        uppercase (bool, optional): Generate password with uppercase letter. Defaults to False.
        
        number (bool, optional): Generate password with number. Defaults to False.
        
        symbol (bool, optional): Generate password with symbol. Defaults to False.
        
        It is highly recommended to use a password with all of the character's types when you register an account.

    Returns:
    
        str: Generated password.
    """
    
    password = ""
    for i in range(size):
        addOk = False
        while(addOk == False):
            char = randomAscii()
            if( lowercase and isLowercaseAscii(char) ):
                password += char
                addOk = True
            elif( uppercase and isUppercaseAscii(char) ):
                password += char
                addOk = True
            elif( number and isNumberAscii(char) ):
                password += char
                addOk = True
            elif( symbol and isSymbolAscii(char) ):
                password += char
                addOk = True
    return password