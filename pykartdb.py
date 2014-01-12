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


def listAllTracks():
    cur.execute('''SELECT * FROM tracks;''')
    tracklist = cur.fetchall()
    return tracklist

def addTrack(trackName, trackLength, trackCity):
    cur.execute('''INSERT INTO tracks (name, length, city) values ("{0}", "{1}", "{2}");'''.format(trackName, trackLength, trackCity))
    con.commit()
    

def listTrackDetails(trackName):
    # get the track details
    cur.execute('''SELECT * from tracks where name = "{0}";'''.format(trackName)
    trackDetails = cur.fetchone()
    trackID = trackDetails[0][0]
    trackLength = trackDetails[0][2]
    trackCity = trackDetails[0][3]
    
    # get total number of laps
    cur.execute(''' SELECT ''')
    
    # get fastest lap

    # Get total time spent on track

    # Get total km or m total driver on track

    #return all the values in a named tuple?
    return trackLength

# close the db connection
def closeDB():
  if con:
      con.close()


connectDB()
listAllTracks()
