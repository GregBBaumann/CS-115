'''
Created on 9/26/19
@author:  Gregory Baumann
Pledge:   I pledge my honor that I have abided by the Stevens Honor System
CS115 - Lab 4
'''
from cs115 import reduce
def coin_row(L):
    if L == []:
        return 0
    else:
        ValueIfUseFirst = L[0] + coin_row(L[2:])
        ValueIfNotUseFirst = coin_row(L[1:])
        return max(ValueIfUseFirst,ValueIfNotUseFirst)
def coin_row_with_values(L):
    return [coin_row(L),coinValue(L)]
def coinValue(L):
    if L == []:
        return []
    else:
        ValueIfUse = [L[0]] + coinValue(L[2:])
        ValueIfNotUse = coinValue(L[1:])
        if ValueIfUse == []:
            return ValueIfNotUse
        elif ValueIfNotUse== []:
            return ValueIfUse
        elif reduce(lambda x,y:x+y,ValueIfUse) > reduce(lambda x,y:x+y,ValueIfNotUse):
            return ValueIfUse
        else:
            return ValueIfNotUse
