import sqlite3
from tkinter import * 
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS
from ttkbootstrap.style import Bootstyle
from tkinter.ttk import Combobox

popup = ttk.Window(themename="morph")
today = date.today()
popup.title("New Services")

sites = ("Twitch", "YouTube", "Streaming Services", "Other")

title_label = ttk.Label(popup, text="Add New Services", bootstyle="info", font=("", 15))
title_label.grid(row = 0, columnspan=2)

title_label = ttk.Label(popup, text="Type of Service", bootstyle="info", font=(15))
title_label.grid(row = 1, column=0)
services = Entry(popup, width=15)
services.grid(row=1, column=1)

def end():
    popup.quit()
    popup.destroy()

def add_listing():
    conn = sqlite3.connect("subs.db")
    c = conn.cursor()

    c.execute("INSERT INTO SERVICES VALUES (:service)",{
            'service': services.get()
        })
    conn.commit()
    conn.close()
    end()
def delete_listing():
  conn = sqlite3.connect("subs.db")
  c = conn.cursor()
  c.execute("DELETE from SERVICES WHERE service = '" + services.get() + "'")
  conn.commit()
  conn.close()
  end()

add_btn = ttk.Button(popup, text = "Add Type Service", command=add_listing)
add_btn.grid(row = 2, column=0)
close_window = ttk.Button(popup, text="Close Window", command=end)
close_window.grid(row=3, column = 0, columnspan=2)
del_btn = ttk.Button(popup, text = "Delete Service Type", command=delete_listing, bootstyle="DANGER")
del_btn.grid(row = 2,column=1)
popup.mainloop()
    #print(today + timedelta(days=30))