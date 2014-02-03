#!/usr/bin/python3

# Main pykart program
# Created on 21/12/13 by Michel Wolf
# version 0.1 

import pykartdb as kart, os, sys

os.system('clear')

print("pyKart program version 0.1")
print("Written by Michel Wolf")
print("------------------------")
print("\n")

# Functions

def mainMenu():
    #os.system("clear")
    print("------------------")
    print("    Main Menu")
    print("------------------")
    print("\n")
    print("(1) Track Menu")
    print("(2) Heat Menu")
    print("(3) Lap Menu")
    print("(5) Exit")
    print("\n")
    return input("Enter option: ")

def trackMenu():
    loop = 1
    while loop == 1:
        os.system("clear")
        print("------------------")
        print("    Track Menu")
        print("------------------")
        print("\n")
        print("(1) Select Track")
        print("(2) Show Track Details")
        print("(3) Add new Track")
        print("(4) Previous Menu")
        print("\n")
        return input("Enter option: ")

def selectTrack():
    """This function gets a list of all tracks, displays them on the screen and ask user 
    to select a track. It convert the user input to an integer and then returns the trackname. Lists start at 0 so the user input is distracted by 1"""
    loop = 1
    while loop == 1:
        os.system("clear")
        print("------------------")
        print("  Select a Track")
        print("------------------")
        trackList = kart.listAllTracks()
        y = 1
        for i in trackList:
            print(y, " ", i[1])
            y += 1
        choice = input("\nPlease your a track: ")
        track = int(choice)
        selectedTrack = trackList[track -1][1] 
        return selectedTrack

def addTrack():
    '''This function adds a track to the database using the addTrack function from pykartdb '''
    os.system("clear")
    print("------------------")
    print("   Add new track")
    print("------------------")
    trackName = input("\nName: ")
    trackLength = input("Length in meters: ")
    trackCity = input("City: ")
    kart.addTrack(trackName, trackLength, trackCity)
    print("Track added: ", trackName, " ", trackLength, " ", trackCity)
    os.system("sleep 2")

def heatMenu():
    print()

def lapMenu():
    print()



kart.connectDB()

loop = 1
option = 0

# Mail loop

while loop == 1:
    option = mainMenu()
    if option == '1':
            # Track Menu
            option = trackMenu()
            if option == '1':
                # Choose a track
                activeTrack = selectTrack()
                print("Selected track: " + activeTrack)
                os.system("sleep 2")
                trackMenu()
            if option == '2':
                # Show track details
                print(option)
            if option =='3':
                # Add track menu
                addTrack()
                # print("Track added")
            if option == '4':
                os.system('clear')
                mainMenu()
            
    elif option == '2':
        # Heat Menu
        print("You choosed heat menu")

    elif option == '3':
        # Lap Menu
        print("You choosed lap menu")

    elif option == '4':
        # Exit program
        kart.closeDB()
        print("Bye")
        print("\n")
        sys.exit()

