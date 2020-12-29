'''
Created on 10/10/19
@author:   Gregory Baumann
Pledge:    I pledge my honor I have abided by the stevens honor system

CS115 - Hw 4
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def snowflake(trunk_length, levels):
    turtle.clear
    if levels == 0:
        turtle.forward(trunk_length)
        turtle.right(120)
        turtle.forward(trunk_length)
        turtle.right(120)
        turtle.forward(trunk_length)
        turtle.right(120)
    else:
        snowflakeSide((int(trunk_length/(3**levels))),levels)
        turtle.right(120)
        snowflakeSide((int(trunk_length/(3**levels))),levels)
        turtle.right(120)
        snowflakeSide((int(trunk_length/(3**levels))),levels)
        turtle.right(120)
    turtle.bye
def snowflakeSide(trunk_length,levels):
    if levels == 0:
        return trunk_length
    else:
        turtle.forward(snowflakeSide(trunk_length,levels-1))
        turtle.left(60)
        turtle.forward(snowflakeSide(trunk_length,levels-1))
        turtle.right(120)
        turtle.forward(snowflakeSide(trunk_length,levels-1))
        turtle.left(60)
        turtle.forward(snowflakeSide(trunk_length,levels-1))
        return 0
    pass  # TODO

D={}
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    if amount==0:
        return 0
    elif coins == []:
        return float("inf")
    elif (amount,len(coins)) in D:
        return D[(amount,len(coins))]
    elif amount < coins[0]:
        return fast_change(amount,coins[1:])
    else:
        ValueIf = 1+fast_change(amount-coins[0],coins)
        D[(amount-coins[0],len(coins))] = ValueIf - 1
        ValueIfNot = fast_change(amount,coins[1:])
        D[(amount,len(coins[1:]))] = ValueIfNot
        return min(ValueIf,ValueIfNot)

# If you did this correctly, the results should be nearly instantaneous.
print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a snow flake
snowflake(800, 3)
