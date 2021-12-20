import sqlite3
from tkinter import * 
from datetime import date, timedelta
import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS
import select_id
edit = Tk()
today = date.today()
edit.title("Edit Subscriptions")

title_label = ttk.Label(edit, text="Edit Subscriptions", bootstyle="info", font=(15))
title_label.grid(row = 0, columnspan=2)



channel = Entry(edit, width = 30)
channel.grid(row=1, column = 1)
channel_label = Label(edit, text="Channel")
channel_label.grid(row = 1, column = 0)

total = Entry(edit, width = 30)
total.grid(row = 2, column = 1, padx=20)
total_label = Label(edit, text = "Total Subscriptions")
total_label.grid(row=2,column=0)


badge = Entry(edit, width = 30)
badge.grid(row = 3, column = 1, padx=20)
badge_label = Label(edit, text="Badge")
badge_label.grid(row = 3, column = 0)

user_gifted = Entry(edit, width = 30)
user_gifted.grid(row = 4, column = 1, padx=20)
user_gifted_label = Label(edit, text="User Gifted")
user_gifted_label.grid(row = 4, column = 0)


print("TEST")
print(select_id.sub_id)

def query():
    #connect to db 
    conn = sqlite3.connect("twitch_subs.db")
    c = conn.cursor()
    #select all
    c.execute ("SELECT * FROM twitch_subs WHERE oid = ")
    #loop results
    print_subs = ''    
    subs = c.fetchall()
    for sub in subs:
        print_subs +=  str(sub[3])   + " " + str(sub[4])  + " " + str(sub[5]) + "\n"   

    query_label = Label(edit, text=print_subs)
    query_label.grid(row = 3, columnspan = 2)

    conn.commit()
    conn.close()


# query()
def end():
    edit.quit()
    edit.destroy()

def update():


    end()
Update_window = ttk.Button(edit, text="Update", command=update).grid(row=5, columnspan=1)

close_window = ttk.Button(edit, text="Close", command=end)
close_window.grid(row=5, columnspan=  1, column = 1)
edit.mainloop()