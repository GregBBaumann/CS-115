'''
Created on September 12, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Gregory Baumann
username: baumann
'''

def dot(L,K):
    return listTimesList(L,K,0,0)
def add(x,y):
    return x+y
def listTimesList(L, K, n,t):
    if L == [] or K == []:
        return 0
    if n == length(L,0) or n == length(K,0):
        return t
    else:
        t = t + L[n] * K[n]
        return listTimesList(L,K,n+1,t)

def explode(S):
    L = list(range(lengthWord(S,0)))
    return expandWord(S,L)
def expandWord(S,L):
    n = lengthWord(S,0)-1
    if n == -1 :
        return L
    else:
        L[n] = S[n]
        return expandWord(S[:n],L)


    
def lengthWord(S,n):
    if S == '':
        return n
    else:
        return lengthWord(S[1:],n+1)


    
def ind(e,L):
    return searchList(e,L,0)
def searchList(e,L,n):
    if len(L) == n:
        return n
    elif e == L[n]:
        return n
    else:
        return searchList(e,L,n+1)

def removeAll(e,L):
    return removedList(e,L,0)
def removedList(e,L,n):
    if n == length(L,0):
        return L
    elif e != L[n] :
        n += 1
        return removedList(e,L,n)
    else:
        L= L[:n]+L[n+1:]
        return removedList(e,L,n)

def myFilter(f,L):
    return filteredList(f,L,0)
def filteredList(f,L,n):
    if n == length(L,0):
        return L
    elif f(L[n]) == True :
        n += 1
        return filteredList(f,L,n)
    else:
        L= L[:n]+L[n+1:]
        return filteredList(f,L,n)
def length(L,t):
    if L == []:
        return t
    else:
        return length(L[1:],t = t+1)
def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def deepReverse(L):
    return Reverse(L,0)
def Reverse(L,n):
    if (int)(length(L,0)/2) == n:
        if L == []:
                return []
        if testList(L[n]) == True:
                L[n] = Reverse(L[n],0)
        return L
    if testList(L[-(1+n)]) == True:
        if L[-(1+n)] == []:
            L[-(1+n)]=[]
        else :
            L[-(1+n)] = Reverse(L[-(1+n)],0)
    temp = L[n]
    L[n]=L[-(1+n)]
    L[-(1+n)]=temp
    return Reverse(L,n+1)
def testList(x):
    return isinstance(x,list)
