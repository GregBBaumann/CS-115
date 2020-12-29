'''
Created on 10/1/19
@author:   Gregory Baumann
Pledge:    I pledge my honor that I have abided by the stevens honor system

CS115 - Lab 5
'''
import time
from cs115 import map

words = []
HITS = 10

D = {}
def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    if (first,second) in D:
        return D[(first,second)]
    elif first == second:
        return 0
    elif first == "":
        return len(second)
    elif second == "":
        return len(first)
    elif first[0]==second[0]:
        return fastED(first[1:],second[1:])
    else:
        deleteFirst = 1 + fastED(first[1:],second)
        D[(first[1:],second)] = deleteFirst -1
        deleteSecond = 1 + fastED(first,second[1:])
        D[(first,second[1:])] = deleteSecond - 1
        deleteBoth = 1 + fastED(first[1:],second[1:])
        D[(first[1:],second[1:])] = deleteBoth - 1
        return min(deleteFirst,deleteSecond,deleteBoth)
    pass  # TODO


def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda s:(fastED(user_input,s),s), words)
    pass  # TODO

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.
    
    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
