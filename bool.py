def NOT(a):
    if a == 0:
        print(bool(1))
    elif a == 1:
        print(bool(0))
    else:
        print("This type is not in the database")


def AND(a, b):
    if a == 1 and b == 1:
        print(bool(1))
    else:
        print(bool(0))


def OR(a, b):
    if a == 0 and b == 0:
        return(bool(0))
    else:
        return(bool(1))


# Nor gate is when we first use an or gate then use that output for a NOT gate
def NOR(a, b):
    if a == 0 and b == 0:

        return(bool(1))
    else:
        return(bool(0))


def NAND(a, b):
    if a == 1 and b == 1:
        return(bool(0))
    else:
        return(bool(1))


# AND   |   OR   |   NOT  |   NOR


"""
TO convert binary to integer
    
    Make a Grid with 5 columns and 2 rows, start with 1 and keep multiplying by 2
    Visualization:
    
    16  |   8   |   4   |   2   |   1
        |       |       |       |
             
    And then right your binary number in the lower row, In out case 1001
    Visualization: 
    
    16  |   8   |   4   |   2   |   1
        |   1    |    0   |    0   |   1
    
    Now check the top row for evey number in the top row check if below tht number is a one, so for every number there is a one below it add them all to get the 
    Final Result:
    
    Visualization: 
    
    16  |   8   |   4   |   2   |   1
        |   1    |    0   |    0   |   1
        
    8 + 1 = 9 
    Result = 9
        
"""


# To convert bin to int
def bint(n):
    return int(n)


#  To convert int to bin

def dbin(n):
    return bin(n)


NOT(False)