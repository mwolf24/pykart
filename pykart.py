#!/usr/bin/python3

# Main pykart program
# Created on 21/12/13 by Michel Wolf
# version 0.1 

import pykartdb as kart, os, sys, time

os.system('clear')

# track Functions

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
        track = int(input("\nPlease choose a track: "))
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

# heat functions
def heatMenu():
    loop = 1
    while loop == 1:
        os.system("clear")
        print("------------------")
        print("    Heat Menu")
        print("------------------")
        print("\n")
        print("(1) Select Heat")
        print("(2) Show Heat Details")
        print("(3) Add new Heat")
        print("(4) Previous Menu")
        print("\n")
        return input("Enter option: ")

def selectHeat():
    ''' THis function gets a list of all available heats, display in date order and lets the user choose one from the list
    i[0] contains the heats.heat_id wich will be returned via selectedHeat variable '''
    heatlist = kart.listAllHeats()
    os.system('clear')
    print("------------------")
    print("  Select a Track")
    print("------------------")
    x = 1
    print("#", "Datum", "Kartbaan", "Heat Type", "Heat Comments")
    for i in heatlist:
        print(x, " ", i[1],", ", i[2], ", ", i[3], ", ", i[4])
        x += 1
    print
    heat = int(input("Plese choose a heat: "))
    selectedHeat = heatlist[heat -1][0]
    print("Selected heatID ", selectedHeat) # debugging
    print("Selected track: ", heatlist[heat -1][2]) # debugging
    return selectedHeat

# Main program

print("pyKart program version 0.1")
print("Written by Michel Wolf")
print("------------------------")
print("\n")

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
                print("Selected track: " + trackName) # debugging
                print("Current trackID: " + trackID)  # debugging
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
        option = heatMenu()
        if option == '1':
            #Choose a heat
            selectHeat()
            time.sleep(10)

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

