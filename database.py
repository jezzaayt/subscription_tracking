import sqlite3
import os.path


conn = sqlite3.connect("subs.db")
c = conn.cursor()
# create database if does not exist 
c.execute("""CREATE Table IF NOT exists subs
 (start_date date, end_date date, badge text, total_sub integer, channel text, user_gifted text, url text ) """ )
if os.path.isfile("subs.db"):
    print("") # print nothing so that the else works
else:
    print("database created")

