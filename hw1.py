'''
Created on September 12, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Gregory Baumann
username: baumann
'''

from cs115 import map, reduce
import math

def add(x,y):
    return x+y
def add1(x):
    return x+1
def multiply(x,y):
    return x*y
def factorial(n):
    if n==0:
        return 1
    else:
        return reduce(multiply,map(add1,range(n)))
def mean(L):
    n = len(L)-1
    return sum(0,L,n)/len(L)


def sum(t,L,n):
    if (n == -1):
        return t
    else:
        n-=1
        return sum(t + L[n+1],L,n)

def primes(n):
    k= n-1
    return divides(n,n-1)

def divides(n,k):
   if k <= 1:
      return True
   elif n % k == 0:
      return False
   else:
      return divides(n,k-1)
    
 
    

