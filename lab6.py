'''
Created on 10/10/19
@author:  Gregory Baumann
Pledge:   I pledge my honor I have abided by the stevens honor system

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False
    else:
        return True
    pass  # TODO

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    return powConv(n,0)
    pass  # TODO
def powConv(n,p):
    if 2**p > n:
        return binConv(n,p-1,'')
    else:
        return powConv(n,p+1)
def binConv(n,p,s):
    if n == 0:
        return s
    elif 2**p > n:
        return binConv(n,p-1,s+'0')
    else:
        if n - 2**p == 0 and p != 0:
            return binConv(n-(2**p),p-1,s+'1'+(p*'0'))
        else:
            return binConv(n-(2**p),p-1,s+'1')

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return (int(s[0]))*2**(len(s)-1)+binaryToNum(s[1:])
    pass  # TODO
def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '11111111':
        return '00000000'
    else:
        return  (8-len(numToBinary(binaryToNum(s)+1)))*'0' + numToBinary(binaryToNum(s)+1)
    pass  # TODO

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n == 0:
        return
    else:
        return count(increment(s),n-1)
    pass  # TODO

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    return pow3Conv(n,0)
    pass  # TODO
def pow3Conv(n,p):
    if 3**p > n:
        return TerConv(n,p-1,'')
    else:
        return pow3Conv(n,p+1)
def TerConv(n,p,s):
    if n == 0:
        return s
    elif 3**p > n:
        return TerConv(n,p-1,s+'0')
    else:
        if (n - 3**p == 0 or n - (2*(3**p))==0) and p != 0:
            if n-3**p == 0:
                return TerConv(n-(3**p),p-1,s+'1'+(p*'0'))
            else:
                return TerConv(n-(2*(3**p)),p-1,s+'2'+(p*'0'))
        else:
            if n - (2*(3**p)) > 0:
                return TerConv(n-(2*(3**p)),p-1,s+'2')
            else:
                return TerConv(n-((3**p)),p-1,s+'1')
    pass  # TODO

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return (int(s[0]))*3**(len(s)-1)+ternaryToNum(s[1:])
    pass  # TODO
