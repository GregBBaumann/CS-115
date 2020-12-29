'''
Created on 10/19/19
@author:   Gregory Baumann
Pledge:   I pledge my honor I have abided by the stevens honor system

CS115 - Hw 5
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def compress(S):
    k='0'
    t=0
    return compressAssit(S,k,t)

def compressAssit(S,k,t):
    if S == '':
        if t != 0:
            return ((5-len(numToBinary(t)))*'0' + numToBinary(t))
        return ''
    elif S[0] == k:
        t=t+1
        if numToBinary(t) == '1'*COMPRESSED_BLOCK_SIZE:
            if k == '1':
                k= '0'
            else:
                k= '1'
            return '11111' + compressAssit(S[1:],k,0)
        return compressAssit(S[1:],k,t)
    else:
        if k == '1':
            k='0'
        else:
            k='1'      
        return ((5-len(numToBinary(t)))*'0') + numToBinary(t) + compressAssit(S,k,0)

def uncompress(S):
    k = '1'
    return uncompressAssit(S,k)
def uncompressAssit(S,k):
    if k == '1':
        k = '0'
    else:
        k = '1'
    if S == '':
        return ''
    else:
        return k*binaryToNum(S[0:(COMPRESSED_BLOCK_SIZE)]) + uncompressAssit(S[(COMPRESSED_BLOCK_SIZE):],k)
        
def compression(S):
    return len(compress(S))/len(S)


def numToBinary(n):
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
    if s == '':
        return 0
    else:
        return (int(s[0]))*2**(len(s)-1)+binaryToNum(s[1:])
