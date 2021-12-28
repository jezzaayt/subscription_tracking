from tkinter import * 
from tkinter import ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Bootstyle
import database as db
import ttkbootstrap as ttk
import os 
import view_graph as graph
import win32gui, win32con
# Using ttkbootstrap  theme
# https://github.com/israel-dryer/ttkbootstrap/

def new_sub():
  os.system("add_new.py")
def new_service():
  os.system("add_services.py")
  print("")
def view_subs():
  os.system("view_subs.py")
def view_graph():
  os.system("view_graph.py")
  #os.system("view_graph.py")
  graph.plot()
root = ttk.Window(themename="morph")
root.title("Manual Subscription Tracker")
root.geometry("400x228")
add_btn = ttk.Button(root, text="New Sub", command=new_sub, width = 30, bootstyle=SUCCESS )
add_btn.pack()
add_service = ttk.Button(root, text="New Service Type", command=new_service, width=30, bootstyle=SUCCESS)
add_service.pack()

view_btn = ttk.Button(root, text="View All Subscriptions", command=view_subs, width = 30, bootstyle=INFO ).pack()
graph_btn = ttk.Button(root, text="View Graph", command=view_graph, width=30, bootstyle=WARNING).pack()

quit_btn = ttk.Button(root, text = "Quit", command=root.quit, width = 30 ).pack()

# hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(hide, win32con.SW_HIDE)


root.mainloop()