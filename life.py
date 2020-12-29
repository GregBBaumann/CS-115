#
# life.py - Game of Life lab
#
# Name: Gregory Baumann
# Pledge: I pledge my honor I have abided by the stevens honor system
#

import random
import sys

def printBoard(A):
 """ this function prints the 2d list-of-lists
 A without spaces (using sys.stdout.write)
 """
 for row in A:
     for col in row:
         sys.stdout.write( str(col) )
     sys.stdout.write( '\n' )

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row
def createBoard(width,height):
    A=[]
    for row in range(height):
        A += [createOneRow(width)]
    return A

def diagonalize(width,height):
     """ creates an empty board and then modifies it
     so that it has a diagonal strip of "on" cells.
     """
     A = createBoard( width, height )

     for row in range(height):
         for col in range(width):
             if row == col:
                 A[row][col] = 1
             else:
                 A[row][col] = 0
     return A

def innerCells(width,height):
    A = createBoard(width,height)

    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A

def randomCells(width,height):
    A = createBoard(width,height)

    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1])
    return A

def copy(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width,height)

    for row in range(height):
        for col in range(width):
            newA[row][col] = A[row][col]
    return newA

def innerReverse(A):
    newA = copy(A)
    height = len(A)
    width = len(A[0])
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                newA[row][col] = 0
            else:
                if newA[row][col] == 1:
                    newA[row][col] = 0
                else:
                    newA[row][col] = 1
    return newA

def next_life_generation(A):
    newA = copy(A)
    height = len(A)
    width = len(A[0])
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                newA[row][col] = 0
            else:
                if A[row][col] == 1:
                    neighbor = neighbors(A,row,col)
                    if 2 > neighbor or neighbor > 3:
                        newA[row][col] = 0
                else:
                    neighbor = neighbors(A,row,col)
                    if neighbor == 3:
                        newA[row][col] = 1
    return newA

def neighbors(A,row,col):
    neighbors = 0
    for countNeighbors in range(-1,3,2):
       if A[row+countNeighbors][col] == 1:
           neighbors += 1
       if A[row][col+countNeighbors] == 1:
           neighbors += 1
       if A[row+countNeighbors][col+countNeighbors] == 1:
           neighbors += 1
       if A[row+countNeighbors][col-countNeighbors] == 1:
           neighbors += 1
    return neighbors







    
