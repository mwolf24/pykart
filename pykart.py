#!/usr/bin/python3

# Main pykart program
# Created on 21/12/13 by Michel Wolf
# version 0.1 

import pykartdb as kart, os, sys, time

os.system('clear')

print("pyKart program version 0.1")
print("Written by Michel Wolf")
print("------------------------")
print("\n")

# Functions

def mainMenu():
    os.system("clear")
    print("------------------")
    print("    Main Menu")
    print("------------------")
    print("\n")
    print("(1) Track Menu")
    print("(2) Heat Menu")
    print("(3) Lap Menu")
    print("(4) Exit")
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
        choice = input("\nPlease choose a track: ")
        track = int(choice)
        selectedTrack = trackList[track -1][1] 
        return selectedTrack

def showTrackDetails(trackID):
    # Show track details
    trackName = kart.getTrackName(trackID)
    trackLength = kart.getTrackLength(trackID)
    trackCity = kart.getTrackCity(trackID)
    totalLaps = kart.totalLaps(trackID)
    fastestLap = kart.fastestLap(trackID)
    trackTime = kart.totalTrackTime(trackID)
    trackKM = kart.totalTrackKM(trackID)
    os.system('clear')
    loop = 1
    while loop == 1:
        print("-------------")
        print("Track details")
        print("-------------")
        print("\n")
        print("Track configuration:")
        print("\n")
        print("Name: ", trackName)
        print("Length: ", trackLength)
        print("City: ", trackCity)
        print("Total numbers of laps: ", totalLaps)
        print("Fastest lap: ", fastestLap)
        print("Total track time in minutes: ", trackTime)
        print("Total kilometer driven: ", trackKM)
        print("\n")
        print("\nPress q to quit")
        choice = input("Press l to see all the tracks laps: ")
        
        if choice == "q" or choice == "Q":
            loop = 0
        elif choice == "l" or choice == "L":
            showAllLaps(trackID)
        else:
            os.system("clear")
            loop = 1
    trackMenu()

def showAllLaps(trackID):
    os.system("clear")
    trackName = kart.getTrackName(trackID)
    allLaps = kart.allLaps(trackID)
    loop = 1
    while loop == 1:
        print("------------------------------------------------")
        print("Showing all laps for track:", trackName)
        print("------------------------------------------------")
        print("\n")
        y = 1
        c = 0
        for i in allLaps:
            print(y, ' ', allLaps[c][0])
            y += 1
            c += 1
        choice = input('\nPress q to quit: ')
        if choice == "q" or  choice == "Q":
            os.system('clear')
            loop = 0
        else:
            os.system('clear')
            loop = 1


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
    time.sleep(2)


trackID = 0
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
                trackName = selectTrack()
                trackID = kart.getTrackID(trackName)
                print("Selected track: " + trackName)
                print("Current trackID: " + trackID)
                time.sleep(2)
                trackMenu()
            elif option == '2':
                if trackID != 0:
                    showTrackDetails(trackID)
                else:
                    # if no track is active show the track menu
                    trackMenu()
            elif option =='3':
                # Add track menu
                addTrack()
                # print("Track added")
            elif option == '4':
                os.system('clear')
                mainMenu()
            else:
                trackMenu()
            
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
    else:
        mainMenu()

