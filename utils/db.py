import sqlite3
import random
from datetime import datetime

DB_FILE="./data/api.db"

def create_db():
    '''
    Creates the db.
    '''
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #creates user directory
    c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS searches(username TEXT, search TEXT, time TEXT)")

    db.commit()
    db.close()

def isUser(user):
    #returns boolean of whether user is already in the database
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT username FROM users WHERE username = '{0}'".format(user))
    name = c.fetchone()
    db.commit()
    db.close()
    if name != None and len(name) > 0:
        return True
    return False

def getPw(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    # returns passwords of specific user
    c.execute("SELECT password FROM users WHERE username = '{0}'".format(user))
    x = c.fetchone()
    db.commit()
    db.close()
    return x[0]

def getSearches(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    # returns all searches of a specific user
    c.execute("SELECT search FROM searches WHERE username = '{0}'".format(user))
    x = c.fetchall()
    db.commit()
    db.close()
    return x

def register(user, pw):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    # inputs username and password into the users database
    c.execute("INSERT INTO users VALUES('{0}','{1}')".format(user,pw))
    db.commit()
    db.close()

def addSearch(user, search):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    # creates entry in searches database of search text, username, and timestamp
    c.execute("INSERT INTO searches VALUES ('{0}', '{1}', '{2}')".format(user, search, datetime.utcnow()))
    db.commit()
    db.close()
