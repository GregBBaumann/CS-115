
#I plegde my honor that I have abided by the Stevens Honor System
#Gregory Baumann


from cs115 import map, reduce
import math

def add(x,y):
    return x+y
def add1(x):
    return x+1
def mutiply(x,y):
    return x*y
def inverseFactorial(n):
    return inverse(reduce(mutiply,map(add1,range(n))))
def inverse(n):
    return 1/n
def e(n):
    return reduce(add,map(inverseFactorial,map(add1,range(n))))+1   
def error(n):
    return math.e - e(n)
