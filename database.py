import mysql.connector
import datetime
from users import *

def pullScoresFromDB():
    cnx = mysql.connector.connect(user='a4356275_admin', password='masterm1nd',
                                  host='server31.000webhost.com',
                                  database='a4356275_mmind')
    curs = cnx.cursor()
    try:
       curs.execute("SELECT * FROM scores")
       curs.commit()
    except:
       curs.rollback()
    return curs.fetchall()

def addHighScoreToDB(user, score):
    cnx = mysql.connector.connect(user='a4356275_admin', password='masterm1nd',
                                  host='server31.000webhost.com',
                                  database='a4356275_mmind')
    curs = cnx.cursor()
    try:
       cursor.execute('''INSERT into scores (User, Score, Difficulty, Date)
                  values (%s, %s, %s, &s)''',
                  (user.name, score, user.difficulty, datetime.datetime.now()))
       curs.commit()
    except:
       curs.rollback()