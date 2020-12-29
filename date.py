'''
Created on 11/21/19
@author:   Gregory Baumann
Pledge:    I pledge my honor I have abided by the stevens honor system.
CS115 - Hw 10 - Date class
'''
import copy
DIM = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False


    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    
    def equals(self, d2):
         '''Decides if self and d2 represent the same calendar date,
         whether or not they are the in the same place in memory.'''
         return self.year == d2.year and self.month == d2.month and \
         self.day == d2.day

    def tomorrow(self):
        self.day += 1
        if self.day > DIM[self.month]:
            if self.month == 2 and self.day == 29 and self.isLeapYear() == True:
                self.day = 29
            else:
                self.month += 1
                self.day = 1
            if self.month == 13:
                self.month = 1
                self.year += 1

    def yesterday(self):
        self.day -= 1
        if self.day == 0:
            self.month -= 1
            if self.isLeapYear() == True and self.month == 2:
                self.day = 29
            else:
                self.day = DIM[self.month]
            if self.month == 0:
                self.month = 12
                self.year -= 1
                self.day = DIM[12]

    def addNDays(self,n):
        print(self.__str__())
        for days in list(range(0,n)):
            self.tomorrow()
            print(self.__str__())

    def subNDays(self,n):
        print(self.__str__())
        for days in list(range(0,n)):
            self.yesterday()
            print(self.__str__())

    def isBefore(self,d2):
        if self.year > d2.year:
            return False
        elif self.year == d2.year and self.month > d2.month:
            return False
        elif self.year == d2.year and self.month == d2.month and self.day >= d2.day:
            return False
        return True

    def isAfter(self,d2):
        if self.year > d2.year:
            return True
        elif self.year == d2.year and self.month > d2.month:
            return True
        elif self.year == d2.year and self.month == d2.month and self.day > d2.day:
            return True
        return False

    def diff(self,d2):
       d1c = copy.deepcopy(self)
       d2c = copy.deepcopy(d2)
       days = 0
       if d1c.isBefore(d2c) == True:
           while d1c.equals(d2c) == False:
               d1c.tomorrow()
               days += 1
           return -1 * days
       elif d1c.isAfter(d2c) == True:
           while self.equals(d2c) == False:
               d1c.yesterday()
               days += 1
           return days
       return days

    def dow(self):
        dowL = ['Sunday','Saturday','Friday','Thursday','Wednesday','Tuesday','Monday']
        day = Date(11,24,2019)
        deter = self.diff(day)
        if deter < 0:
            deter = deter * -1
        return dowL[deter % 7]

        
           
            
            
