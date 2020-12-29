'''
Created on 9/26/19
@author:  Gregory Baumann
Pledge:   I pledge my honor that I have abided by the Stevens Honor System
CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

from cs115 import map, reduce, filter
def giveChange(a,L):
    return [change(a,L),leastCoins(a,L)]
def change(a,L):
    if a==0:
        return 0
    elif L == []:
        return float("inf")
    elif a < L[0]:
        return change(a,L[1:])
    else:
        ValueIf = 1+change(a-L[0],L)
        ValueIfNot = change(a,L[1:])
        return min(ValueIf,ValueIfNot)
def leastCoins(a,L):
    if a==0:
        return []
    elif L == []:
        return list(range(1,1000))
    elif a < L[0]:
        return leastCoins(a,L[1:])
    else:
        ValueIf = [L[0]] + leastCoins(a-L[0],L)
        ValueIfNot = leastCoins(a,L[1:])
        if len(ValueIf) < len(ValueIfNot):
            return ValueIf
        else:
            return ValueIfNot

        

