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
    # get the active track id number
    cur.execute('''SELECT track_id FROM tracks WHERE name = "{0}";'''.format(trackName))
    trackDetails = cur.fetchone()
    trackID = str(trackDetails[0])
    return trackID       

def getTrackName(trackName):
    # ??? Not needed ???
    cur.execute('''SELECT * FROM tracks WHERE name = "{0}";'''.format(trackName))
    trackDetails = cur.fetchone()
    trackName = trackDetails[0][1]
    return trackName

def getTrackLength(trackID):
    # get the length of the current track
    cur.execute('''SELECT length FROM tracks WHERE track_id = "{0}";'''.format(trackID))
    trackDetails = cur.fetchone()
    trackLength = float(trackDetails[0])
    return trackLength

def getTrackCity(trackID):
    # get the city of the current track
    cur.execute('''SELECT city FROM tracks WHERE track_id = "{0}";'''.format(trackID))
    trackDetails = cur.fetchone()
    trackCity = str(trackDetails[0])
    return trackCity
    
def totalLaps(trackID):
    # get total number of laps from active track
    cur.execute('''SELECT 
    COUNT(laps.laptime)
    FROM laps
    INNER JOIN heats ON laps.heat_id = heats.heat_id 
    INNER JOIN tracks ON tracks.track_id = heats.track_id
    WHERE tracks.track_id = "{0}"; '''.format(trackID))
    laps = cur.fetchone()
    totalLaps = int(laps[0])
    return totalLaps    

def getAlllaps(trackID):
    # Get all driven laps from a track
    cur.execute('''SELECT
    laps.laptime
    FROM laps
    INNER JOIN heats ON laps.heat_id = heats.heat_id 
    INNER JOIN tracks ON tracks.track_id = heats.track_id
    WHERE tracks.track_id = "{0}"; '''.format(trackID))
    allLaps = cur.fetchall()
    return allLaps
   
def fastestLap(trackID):
    # get fastest lap from active track
    cur.execute('''SELECT
    MIN(laps.laptime)
    FROM laps
    INNER JOIN heats ON laps.heat_id = heats.heat_id
    INNER JOIN tracks ON tracks.track_id = heats.track_id
    WHERE tracks.track_id = "{0}"; '''.format(trackID))
    fastest = cur.fetchone()
    return fastest

def totalTrackTime(trackID):
    # Get total time spent on active track
    # the query gives total time in seconds
    # first convert the query output to a float in times
    # then calculate to minutes in timem
    cur.execute(''' SELECT
    SUM(laps.laptime)
    FROM laps
    INNER JOIN heats ON laps.heat_id = heats.heat_id
    INNER JOIN tracks ON tracks.track_id = heats.track_id
    WHERE tracks.track_id = "{0}"; '''.format(trackID))
    seconds = cur.fetchone()
    minutes = float(seconds[0]) / 60
    return minutes

def totalTrackKM(trackID):
    # Get total km driver on a track
    # First get total number of laps on current active track and make it an int
    laps = totalLaps(trackID)
    # Now get the tracklength and make it a float
    length = getTrackLength(trackID)    
    # Now calculate the total km on the track
    km = laps * length / 1000
    return km

# close the db connection
def closeDB():
  if con:
      con.close()


