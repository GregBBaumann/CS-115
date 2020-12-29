'''
Created on 11/18/19
@author:   Gregory Baumann
Pledge:    I pledge my honor I have abided by the stevens honor system

CS115 - Hw 9
'''

def convert(userIn):
    userDic = {}
    for Length in userIn:
        userName = ''
        userNamev = True
        while userNamev == True:
            userName = userName + userIn[0][0]
            userIn[0] = userIn[0][1:]
            if userIn[0][0] == ':':
                userIn[0] = userIn[0][1:]
                userNamev = False
        userArtists = []
        userArtistsv = True
        Artist = ''
        while userArtistsv == True:
            if userIn[0] == "\n" or userIn[0] == '':
                userArtists = userArtists + [Artist]
                userArtistsv = False
            elif userIn[0][0] == ',':
                userArtists = userArtists + [Artist]
                Artist = ''
            else:
                Artist = Artist + userIn[0][0]
            userIn[0] = userIn[0][1:]
        userDic[(userName)] = userArtists
        userIn = userIn[1:]
        
    return userDic
                
        

def start():
    print("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    inFile = open('musicrecplus.txt')
    userInputs = inFile.readlines()
    userDic = convert(userInputs)
    user = input()
    
    menu(user,userDic)
def menu(user,userDic):
    print("Enter a letter to choose an option")
    print("e - Enter preferences")
    print("r - Get recommendations")
    print("p - Show most popular artitsts")
    print("h - How popular is the most popular")
    print("m - Which user has the most likes")
    print("q - Save and quit")
    newInput = input()
    
    if newInput == 'e':
        Preferences(user,userDic)

    elif newInput == 'r':
        menu()

    elif newInput == 'p':
        menu()

    elif newInput == 'h':
        menu()

    elif newInput == 'm':
        menu()

    elif newInput == 'q':
        menu()

def Preferences(user,userDic):
    Pref = []
    endPreferences = False
    while endPreferences == False:
        print("Enter an artist that you like (Enter to finish):")
        newPref == input()
        if newPref == '':
            endPreferences == True
        else:
            Pref == Pref + [newPref]
    userDic[(user)] = Pref
    menu(user,userDic)

def recomendations(user,userDic):
    userList = []
    for users in userDic:
        if users[-1:] != '$' or user != users:
            userList = userList + [users]
    for users in userList:
        usersList = userDic[(userList[users])]
        userList = userDic[(user)]
        common = 0
        recList = []
        while usersList != []
            for artist in userList:
                if userList[artist] ==  userList[0]:
                    common = common + 1
                else:
                    recList = recList + [
                    
        
            
        
    
    
    
