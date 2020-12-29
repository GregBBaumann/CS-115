'''
Created on October 31, 2019
@author: Gregory Baumann
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Lab 9
'''

import sys
import importlib

Fibonacci = """
00 read r1
01 jeqzn r1 12
02 setn r2 0
03 setn r3 1
04 write r2
05 addn r1 -1
06 jeqzn r1 12
07 write r3
08 add r3 r3 r2
09 sub r2 r3 r2
10 addn r1 -1
11 jumpn 6
12 halt
"""
RunThis = Fibonacci
Mode = ['-n']
if __name__ == "__main__" : 
    import hmmmAssembler ; importlib.reload(hmmmAssembler)
    import hmmmSimulator ; importlib.reload(hmmmSimulator)
    hmmmAssembler.main(RunThis)
    hmmmSimulator.main(Mode)
    
    
