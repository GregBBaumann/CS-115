
import random

Bingo = "BINGO"
Card = {}
for count in range(0,5):
    possibleNum = list(range((count*15)+1,((count+1)*15)+1))
    for number in range(1,6):
        randomint= random.randint(0,len(possibleNum)-1)
        Card[(Bingo[count],number)] = possibleNum[randomint]
        possibleNum= possibleNum[:randomint] + possibleNum[randomint+1:]

print(Card)

