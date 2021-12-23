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
popup.title("New Subscription")

sites = ("Twitch", "YouTube", "Streaming Services", "Other")

title_label = ttk.Label(popup, text="Add New Subscription", bootstyle="info", font=(15))
title_label.grid(row = 0, columnspan=2)

channel = Entry(popup, width = 30)
channel.grid(row=1, column = 1)
channel_label = Label(popup, text="Service")
channel_label.grid(row = 1, column = 0)
services_label = Label(popup, text="Type of Service:")
services_label.grid(row=2, column=0, padx=20)
services = Combobox(popup, width=30, values=sites, textvariable=sites)
services["state"] = "readonly"
services.current(0)
services.grid(row=2, column=1)



total = Entry(popup, width = 30)
total.grid(row = 3, column = 1, padx=10)
total_label = Label(popup, text = "Total Subscriptions")
total_label.grid(row=3,column=0)
def callback(event):
    print("Changed")
    print(event)
    print("T")
    print(services.get())
    service = services.get()
    if service != "Twitch":
        badge_label.grid_forget()
        badge.grid_forget()
        user_gifted.forget()
        user_gifted_label.forget()
    else:
        
        badge_label.grid(row = 4, column = 0, padx=20)
        badge.grid(row = 4, column = 1)
        user_gifted_label.grid(row=5, column=0)
        user_gifted.grid(row = 5, column = 1)
        url_label.forget()
        url_label.grid(row = 6, column = 0)
        url.forget()
        url.grid(row = 6, column = 1)
        add_btn.forget()
        add_btn.grid(row = 8, column=0)
        close_window.forget()
        close_window.grid(row=8, column = 1)

badge = Entry(popup, width = 30)
badge.grid(row = 4, column = 1, padx=20)
badge_label = Label(popup, text="Badge")
badge_label.grid(row = 4, column = 0)

user_gifted = Entry(popup, width = 30)
user_gifted.grid(row = 5, column = 1, padx=20)
user_gifted_label = Label(popup, text="User Gifted")
user_gifted_label.grid(row = 5, column = 0)

url_label = Label(popup, text="URL")
url_label.grid(row = 6, column = 0)
url = Entry(popup, width = 30)
url.grid(row = 6, column = 1)

len_label = Label(popup, text="Subscription Length")
len_label.grid(row = 7, column=0)
len_pick = Spinbox(popup, width=30, values=(1,3,6,12))
len_pick.grid(row = 7, column = 1)

services.bind("<<ComboboxSelected>>", callback)
def add_listing():
    conn = sqlite3.connect("subs.db")
    c = conn.cursor()

    c.execute("INSERT INTO subs VALUES (:start_date, :end_date, :badge, :total_sub, :channel, :user_gifted, :url, :service)",{
            'start_date':  today,
            'end_date':today+relativedelta(month=+int(len_pick.get())),
            'badge': badge.get(),
            'total_sub': total.get(),
            'channel': channel.get(),
            'user_gifted':  user_gifted.get(),
            'url': url.get(),#"twitch.tv/" + channel.get()
            'service': services.get()
        })
    conn.commit()
    conn.close()
    #badge.delete(0,END)
    total.delete(0,END)
    channel.delete(0,END)
    #user_gifted.delete(0,END)
    print(len_pick.get())


def end():
    popup.quit()
    popup.destroy()
add_btn = ttk.Button(popup, text = "Add Subscription", command=add_listing)
add_btn.grid(row = 8, column=0)
close_window = ttk.Button(popup, text="Close", command=end)
close_window.grid(row=8, column = 1)

popup.mainloop()
    #print(today + timedelta(days=30))