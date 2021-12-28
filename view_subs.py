import sqlite3
from sqlite3.dbapi2 import SQLITE_DROP_VTABLE, connect
from tkinter import * 
from datetime import date, datetime, timedelta
import tkinter
from tkinter.ttk import Combobox
from numpy import right_shift, timedelta64
import ttkbootstrap as ttk
from ttkbootstrap import window
from ttkbootstrap.constants import *
import os
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from ttkbootstrap.style import Bootstyle
from tkinter.messagebox import showinfo
from functools import partial
import webbrowser
from win10toast import ToastNotifier
from ttkbootstrap.widgets import DateEntry

toaster = ToastNotifier()
popup = ttk.Window(themename="morph")
today = date.today()
popup.title("View Subscriptions")
popup.minsize(1720,680)
popup.maxsize(2020,2000)
title_label = ttk.Label(popup, text="View Last Subscriptions", bootstyle="info", font=("",35))
title_label.pack()

columns = ("ID", "Start Date","End Date","Total Subscription Length",  "Channel",  "URL", "Service Type")
sb = ttk.Scrollbar(popup, orient=ttk.VERTICAL)
sb.pack( side=RIGHT, fill=BOTH)

tree = ttk.Treeview(popup, height = 10, columns=columns, show="headings", bootstyle = SUCCESS)

tree.column("Start Date",  anchor=CENTER, minwidth=150)
tree.column("End Date",  anchor=CENTER, minwidth=150)
tree.column("Channel", anchor=CENTER,  minwidth=150)
#tree.column("Badge",  anchor=CENTER, minwidth=80)
tree.column("Total Subscription Length",  anchor=CENTER, minwidth=300)
#tree.column("User Gifted", anchor=CENTER, minwidth=150)
tree.column("URL", anchor=CENTER, minwidth=200)
tree.column("ID", anchor=CENTER, minwidth=50)
tree.column("Service Type", anchor=CENTER, minwidth=50)

tree.pack(expand=YES, fill = BOTH)
sb.config(command=tree.yview)
selected = tree.focus()
id = "1"
# This was selecting the ID but issues when put in the ORDER BY code as was not selecting the ID clicked on. 
# def tree_select(event):
#   #select_text.configure(state=tkinter.NORMAL)
#   select_text.delete(0, "end")
#   for select in tree.selection():
#     select in tree.item(select)
#     sub = str(select)
#     #print(sub[3])
#     id = sub[3]
#     select_text.insert(0,sub[3])
#    # select_text.configure(state=tkinter.DISABLED)
#     showinfo(title="Information", message=",".join(sub))

#tree.bind("<<TreeviewSelect>>", tree_select)
sites = []
def get_serives():
    #connect to db 
    conn = sqlite3.connect("subs.db")
    c = conn.cursor()
    #select all
    c.execute ("SELECT *, oid FROM SERVICES")
    services = c.fetchall()
    for s in services:
      #print(s)      
      sites.append(s[0]) 
   #print(sites)

    conn.commit()
    conn.close()

  


def edit_subs():
  get_serives()
  edit = ttk.Toplevel()
  edit.title("Edit Subscriptions")
  #sites = ("Twitch", "YouTube", "Streaming Services", "Other")
  print(sites)
  title_label = ttk.Label(edit, text="Edit Subscriptions", bootstyle="info", font=(15))
  title_label.pack()#.grid(row = 0, columnspan=2)

  sdate_label = Label(edit, text = "Start Date")#.grid(row = 1, column = 0)
  sdate_label.pack()
  sdate= Entry(edit,width=30)
  sdate.pack()#grid(row=1, column = 1)
  
  # edate_label = Label(edit, text="End Date")
  # edate_label.pack()
  # edate = Entry(edit, width=30)
  # edate.pack()
  lengths = (1,3,6,12)
  
  len_label = Label(edit, text="Subscription Length")
  len_label.pack()
  len_pick = Spinbox(edit, width=30, values=lengths)
  len_pick.pack()


  
  channel_label = Label(edit, text="Service")
  channel_label.pack()#grid(row = 2, column = 0)
  channel = Entry(edit, width = 30)
  channel.pack()#.grid(row=2, column = 1)
  services_label = Label(edit, text="Type of Service:")
  services_label.pack()
  services = Combobox(edit, width=30, values=sites, textvariable=sites)
  services["state"] = "readonly"
  #services.current(0)
  services.pack()

  total_label = Label(edit, text = "Total Subscriptions")
  total_label.pack()#grid(row=3,column=0)
  total = Entry(edit, width = 30)
  total.pack()#grid(row = 3, column = 1, padx=20)

  
  badge_label = Label(edit, text="Badge")
  badge_label.pack()#grid(row = 4, column = 0)
  badge = Entry(edit, width = 30)
  badge.pack()#grid(row = 4, column = 1, padx=20)
  
  
  user_gifted_label = Label(edit, text="User Gifted")
  user_gifted_label.pack()#grid(row = 5, column = 0)
  user_gifted = Entry(edit, width = 30)
  user_gifted.pack()#grid(row = 5, column = 1, padx=20)



  global service 
  def checkType():
    service = services.get()
    if service != "Twitch":
      badge_label.forget()
      badge.forget()
      user_gifted.forget()
      user_gifted_label.forget()
    else:
      badge_label.pack()
      badge.pack()
      user_gifted_label.pack()
      user_gifted.pack()
      url_label.forget()
      url_label.pack()
      url.forget()
      url.pack()
      Update_window.forget()
      Update_window.pack(side=LEFT)
      close_window.forget()
      close_window.pack(side=RIGHT)



  def callback(event):
    checkType()


    






 
 

  url_label = Label(edit, text="URL")
  url_label.pack()#grid(row = 5, column = 0)
  url = Entry(edit, width = 30)
  url.pack()#grid(row = 5, column = 1, padx=20)
  sub_name = select_text.get()

  def edit_query():
      #connect to db 
      conn = sqlite3.connect("subs.db")
      c = conn.cursor()
      #select all
      c.execute ("SELECT * FROM subs WHERE channel = '" + sub_name + "' ")
      #loop results
      print_subs = ''    
      subs = c.fetchall()
      for sub in subs:
        sdate.insert(0,sub[0])
       # edate.insert(0,sub[1])
        channel.insert(0,sub[4])
        total.insert(0,sub[3])
        badge.insert(0,sub[2])
        url.insert(0,sub[6])
        user_gifted.insert(0,sub[5])
        services.insert(0,sub[7])
        services.set(sub[7])
        services.insert(0,sub[7])
      
      conn.commit()
      conn.close()
      


  edit_query()

  services.bind("<<ComboboxSelected>>", callback)
  def edit_end():
      edit.destroy()


 
  def update_query():
      conn = sqlite3.connect("subs.db")
      c = conn.cursor()
      
      
    #select_text.insert(0,sub[3])
      twitch_id = id#select_text.get()
      enddate = sdate.get()
      enddate = datetime.strptime(enddate, "%Y-%m-%d")
      get_new_end = relativedelta(month=int(len_pick.get()))
      end_new = enddate + get_new_end
      if end_new.month < enddate.month or end_new.month == enddate.month:
       
        end_new = end_new +  relativedelta(year=end_new.year + 1)
        end_new = end_new.date()
        
      c.execute("""UPDATE subs SET 
      start_date = :start,
      end_date = :end,
      channel = :channel,
      badge = :badge,
      url = :url,
      total_sub = :total,
      user_gifted = :user_gifted,
      service = :service
      
      WHERE channel = :channel""",
      {
        'start':sdate.get(),
        'end': end_new,#enddate.date() +  relativedelta(month=int(len_pick.get())),
        'channel': channel.get(),
        'badge': badge.get(),
        'total': total.get(),
        'url':  url.get(),#"twitch.tv/" + channel.get(),
        'user_gifted': user_gifted.get(),
        'oid': twitch_id,
        'service': services.get()
      }
      )
      
      conn.commit()
      conn.close()
      edit.destroy()
  Update_window = ttk.Button(edit, text="Update", command=update_query)
  Update_window.pack(side=LEFT)

  close_window = ttk.Button(edit, text="Close", command=edit_end)
  close_window.pack(side=RIGHT)
  checkType()
def query():
    #connect to db 
    conn = sqlite3.connect("subs.db")
    c = conn.cursor()
    #select all
    c.execute ("SELECT *, oid FROM subs ORDER BY End_date DESC")
    subs = c.fetchall()

    # get headings for the treelist
    for col in columns:
      tree.heading(col, text=col)
      tree.column(col, width = 100, anchor=ttk.CENTER)
    #put data into tree list
    for sub in subs:
      print(sub)
      tree.insert("",  tkinter.END, values=(sub[8], sub[0], sub[1], sub[3],  sub[4],sub[6], sub[7]))
  
    #sb.grid(row = 1, column=10, sticky="ns")
    tree.config(yscrollcommand=sb.set)

    conn.commit()
    conn.close()

query()
# 
# def moveDown():
#   item = tree.selection()
#   for i in reversed(item):
#     tree.move(i, tree.parent(i), tree.index(i)+1)

# def moveUp():
#   item = tree.selection()
#   for i in reversed(item):
#     tree.move(i, tree.parent(i), tree.index(i)-1)
def delete():
  conn = sqlite3.connect("subs.db")
  c = conn.cursor()
  c.execute("DELETE from subs WHERE channel = '" + select_text.get() + "'")
  conn.commit()
  conn.close()
  for i in tree.get_children():
    tree.delete(i)
    
  query()

def selectURL():
    item = tree.selection()
    for i in item:
      print(tree.item(i,"values")[5])
      webbrowser.open(tree.item(i,"values")[5])



select_label  =ttk.Label(popup, text = "Select Name:" )
select_label.pack()

select_text = Entry(popup, width = 20)
#select_text.insert(0, "1")
select_text.pack()#grid(row=  2,ipadx=0, sticky=S )

go_to_website_btn = ttk.Button(popup,command=selectURL, text="Visit Subscription Website", bootstyle="INFO-outline").pack()
#select_text.configure(state=tkinter.DISABLED)
edit_btn = ttk.Button(popup, text="Edit Subscriptions", command=edit_subs, bootstyle="info-outline").pack(side=LEFT, fill="both")
delete_btn = ttk.Button(popup, text="Delete Subscription",command=delete,  bootstyle = "danger-outline").pack(side=RIGHT)#.grid(row = 3, sticky=E)


close_window = ttk.Button(popup, text="Close",  command=popup.quit, bootstyle = "info-outline").pack(side=BOTTOM)




popup.mainloop()