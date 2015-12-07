import mysql.connector
import datetime
from users import *

def pullScoresFromDB():
    cnx = mysql.connector.connect(user='romanowskitj', password='masterm1nd',
                                  host='db4free.net',
                                  database='mastermind')
    curs = cnx.cursor()
    try:
       curs.execute("SELECT * FROM scores")
       cnx.commit()
    except:
       cnx.rollback()
    return curs.fetchall()

def addHighScoreToDB(user, score):
    cnx = mysql.connector.connect(user='romanowskitj', password='masterm1nd',
                                  host='db4free.net',
                                  database='mastermind')
    curs = cnx.cursor()
    try:
       curs.execute('''INSERT into scores (User, Score, Difficulty, Date)
                  values (%s, %s, %s, %s)''',
                  (user.name, score, user.difficulty, datetime.datetime.now()))
       cnx.commit()
    except:
       cnx.rollback()
