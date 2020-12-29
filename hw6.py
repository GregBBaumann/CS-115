'''
Created on 10/22/19
@author:   Gregory Baumann
Pledge:   I pledge my honor I have abided by the stevens honor system

CS115 - Hw 6
'''

def numToBase(N,B):
    if N == 0:
        return '0'
    else:
        if N//B == 0:
            return str(N%B)
        else:
            return numToBase(N//B,B) + str(N%B)

def baseBToNum(S,B):
    if S == '':
        return 0
    else:
        return (int(S[0])*(B**(len(S)-1))) + baseBToNum(S [1:],B)

def baseToBase(B1,B2,SinB1):
    return  numToBase(baseBToNum(SinB1,B1),B2)
    
def add(S,T):
    return numToBase(baseBToNum(S,2)+baseBToNum(T,2),2)

def addB(S,T):
    return addBAssit(S,T,'0')
def addBAssit(S,T,carry):
    if S == '' and T == '':
        if carry == '1':
            return '1'
        else:
            return ''
    elif S == '':
        if T[-1] == '1' and carry == '1':
            return addBAssit(S,T[:-1],'1') + '0'
        elif T[-1] == '1' or carry == '1':
            return addBAssit(S,T[:-1],'0') + '1'
        else:
            return addBAssit(S,T[:-1],'0') + '0'
    elif T == '':
        if S[-1] == '1' and carry == '1':
            return addBAssit(S[:-1],T,'1') + '0'
        elif S[-1] == '1' or carry == '1':
            return addBAssit(S[:-1],T,'0') + '1'
        else:
            return addBAssit(S[:-1],T,'0') + '0'
    elif S[-1] == '1' and T[-1] =='1' and carry == '1':
        return addBAssit(S[:-1],T[:-1],'1') + '1'
    elif (S[-1] == '1' and T[-1] == '0' and carry == '0') or (S[-1] == '0' and T[-1] == '1' and carry == '0') or (S[-1] == '0' and T[-1] == '0' and carry == '1'):
        return addBAssit(S[:-1],T[:-1],'0') + '1'
    else:
        return addBAssit(S[:-1],T[:-1],'1') + '0'
