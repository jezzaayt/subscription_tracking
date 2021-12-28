import sqlite3
import os.path


#sites = ("Twitch", "YouTube", "Streaming Services", "Other")

conn = sqlite3.connect("subs.db")
c = conn.cursor()
# create database if does not exist 
c.execute("""CREATE Table IF NOT exists subs
 (start_date date, end_date date, badge text, total_sub integer, channel text, user_gifted text, url text, service text) """ )
c.execute("""CREATE Table IF NOT exists SERVICES
(service text) """ )
if os.path.isfile("subs.db"):
    print("") # print nothing so that the else works
else:
    print("database created")
    c.execute("INSERT INTO SERVICES (service) VALUES (Twitch) ")




c.close()
