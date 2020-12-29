'''
Created on 9/18/19
@author:   Gregory Baumann
Pledge:   I pledge my honor I have abided by the stevens honor system.

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def letterScore(s,L):
    if L == []:
        return 0
    elif s == L[0][0]:
        return L[0][1]
    else:
        return letterScore(s,L[1:])

def wordScore(s,L):
    return scoreTotal(s,L,0)
def scoreTotal(s,L,t):
    if s == '':
        return t
    else:
        t = t + letterScore(s[0],L)
        return scoreTotal(s[1:],L,t)

def scoreList(L):
    return scoredList(L,Dictionary,0)
def scoredList(L,W,n):
    if len(W) == n:
        return W
    elif IsAList(W[n]) == True:
        W[n] = W[n][0]
        return scoredList(L,W,n)
    elif posWord(L,W[n],0) == True:
        W[n] = [W[n],wordScore(W[n],scrabbleScores)]
        return scoredList(L,W,n+1)
    else:
        W = W[:n] + W[n+1:]
        return scoredList(L,W,n)
def posWord(L,s,n):
    if s == '':
        return True
    elif len(L) == n:
        return False
    elif s[0] == L[n]:
        return posWord(L[:n]+L[n+1:],s[1:],0)
    else:
        return posWord(L,s,n+1)

def bestWord(L):
    if len(scoreList(L)) == 0:
        return ['',0]
    elif len(scoreList(L)) == 1:
        return scoreList(L)[0]
    else:
        return reduce(greaterThan,scoreList(L))
def greaterThan(x,y):
    if x[1] > y[1] :
        return x
    else:
        return y
def IsAList(x):
    return isinstance(x,list)


    
