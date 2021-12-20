from tkinter import * 
from tkinter import ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Bootstyle
import database as db
import ttkbootstrap as ttk
import os 

import win32gui, win32con
# Using ttkbootstrap  theme
# https://github.com/israel-dryer/ttkbootstrap/

def new_sub():
  os.system("add_new.py")

def view_subs():
  os.system("view_subs.py")
root = ttk.Window(themename="morph")
root.title("Twitch Manual Subscription Tracker")

add_btn = ttk.Button(root, text="New Sub", command=new_sub, width = 30, bootstyle=SUCCESS )
add_btn.pack()

view_btn = ttk.Button(root, text="View All Subscriptions", command=view_subs, width = 30, bootstyle=INFO ).pack()


quit_btn = ttk.Button(root, text = "Quit", command=root.quit, width = 30 ).pack()

#hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide, win32con.SW_HIDE)


root.mainloop()