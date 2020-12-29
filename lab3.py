'''
Created on 9/1919
@author:   Gregory Baumann
Pledge:   I pledge my honor I have abided by the stevens honor system.

CS115 - Lab 3
'''
from cs115 import map, reduce, filter

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
