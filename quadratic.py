'''
Created on 11/14/19
@author:   Gregory Baumann
Pledge:    I pledge my honor I have abided by the stevens honor system

CS115 - Lab 10
'''
import math
class QuadraticEquation:
    def __init__(self,a,b,c):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        a = float(a)
        b = float(b)
        c = float(c)
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b
    
    @property
    def c(self):
        return self._c
    
    def __str__(self):
        string = ''
        if self.a < 0:
            if self.a == -1:
                string = string + '-x^2'
            else:
                string = string + '-' + str((self.a*-1)) + 'x^2'
        else:
            if self.a == 1:
                 string = string + 'x^2'
            else:
                string = string + str((self.a)) + 'x^2'
        if self.b != 0:
            if self.b < 0:
                if self.b == -1:
                    string = string + ' - ' + 'x'
                else:
                    string = string + ' - ' + str((self.b*-1)) + 'x'
            else:
                if self.b == 1:
                    string = string + ' + ' + 'x'
                else:
                    string = string + ' + ' + str(self.b) + 'x'
        if self.c != 0:
            if self.c < 0:
                string = string + ' - ' + str((self.c*-1))
            else:
                string = string + ' + ' + str((self.c))
        return string + ' = 0'


    def discriminant(self):
        return ((self.b*self.b)-(4*self.a*self.c))

    def root1(self):
        if ((self.b*self.b)-(4*self.a*self.c)) < 0:
            return None
        return (-(self.b)+ math.sqrt(((self.b*self.b)-(4*self.a*self.c))))/(2*self.a)

    def root2(self):
        if ((self.b*self.b)-(4*self.a*self.c)) < 0:
            return None
        return (-(self.b)- math.sqrt(((self.b*self.b)-(4*self.a*self.c))))/(2*self.a)
