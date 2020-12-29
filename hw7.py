'''
Created on 10/24/19
@author:   Gregory Baumann
Pledge:    I pledge my honor I have abided by the stevens honor system

CS115 - Hw 7
'''

def TcToNum(S):
    if S[0] == "0":
        N = 0
    else:
        N = -128
    S = S[1:]
    return TcToNumAssit(S,N)
def TcToNumAssit(S,N):
    if S[1:] == "":
        return N + int(S[0])
    else:
        return TcToNumAssit(S[1:],N+((int(S[0])*2)**(len(S)-1)))

def NumToTc(N):
    if -129 < N < 128:
        if N == 0:
            return '00000000'
        if N > 0:
            return '0' + NumToTcAssit(N,0)
        else:
            N = N+1
            if N == 0:
                return '11111111'
            else:
                return '1' + Inverse(NumToTcAssit(-1*N,0))    
    else:
        return 'Error'
def NumToTcAssit(N,L):
    if N == 0:
        return ''
    else:
        if N//2 == 0:
            return '0'*(6-L) + str(N%2)
        else:
            return NumToTcAssit(N//2,L+1) + str(N%2)
def Inverse(S):
    if S == '':
        return ''
    elif S[0] == '0':
        return '1' + Inverse(S[1:])
    else:
        return '0' + Inverse(S[1:])

