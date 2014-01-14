#!/usr/bin/python3

# pykartdb.py is the file that creates the database and tables if not exists
# This file also contains all the sql functions for the main program
# Created on 14/12/13 by Michel Wolf
# Version 0.1

import sqlite3

def connectDB():
    global con
    global cur    
    con = sqlite3.connect('''pykartdb.db''')
    cur = con.cursor()

    # Enable foreign key support
    cur.execute("PRAGMA foreign_keys = ON")


def listAllTracks():
    cur.execute('''SELECT * FROM tracks;''')
    tracklist = cur.fetchall()
    return tracklist

def addTrack(trackName, trackLength, trackCity):
    cur.execute('''INSERT INTO tracks (name, length, city) values ("{0}", "{1}", "{2}");'''.format(trackName, trackLength, trackCity))
    con.commit()

def getTrackID(trackName):
    # get the active tracks id number
    cur.execute('''SELECT * from tracks where name = "{0}";'''.format(trackName))
    trackDetails = cur.fetchone()
    trackID = trackDetails[0][0]
    return trackID       

def getTrackName(trackName):
    # get the name of the active track
    cur.execute('''SELECT * from tracks where name = "{0}";'''.format(trackName))
    trackDetails = cur.fetchone()
    trackName = trackDetails[0][1]
    return trackName

def getTrackLength(trackName):
    # get the length of the current track
    cur.execute('''SELECT * from tracks where name = "{0}";'''.format(trackName))
    trackDetails = cur.fetchone()
    trackLength = trackDetails[0][2]
    return trackLength

def getTrackCity(trackName):
    # get the city of the current track
    cur.execute('''SELECT * from tracks where name = "{0}";'''.format(trackName))
    trackDetails = cur.fetchone()
    trackCity = trackDetails[0][3]
    return trackCity
    
def totalLaps(trackName):
    # get total number of laps from active track
    # First get the current track_id
    trackID = getTrackID(trackName)
    


    # now query the tables for all the laps at the active track 
    
    
def fastestLap(trackName):
    # get fastest lap from active track
    cur.execute(''' SELECT ''')
def totalTrackTime(trackName):
    # Get total time spent on active track
    cur.execute(''' SELECT ''')
def totalTrackKM(trackName):
    # Get total km or m total driver on track
    cur.execute(''' SELECT ''')

# close the db connection
def closeDB():
  if con:
      con.close()


connectDB()
listAllTracks()
