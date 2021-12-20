import sqlite3
from sqlite3.dbapi2 import connect
from tkinter import * 
from datetime import date, datetime, timedelta
import tkinter
import ttkbootstrap as ttk
from ttkbootstrap import window
from ttkbootstrap.constants import *
import os
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from ttkbootstrap.style import Bootstyle
from tkinter.messagebox import showinfo
from functools import partial

from ttkbootstrap.widgets import DateEntry
popup = ttk.Window(themename="morph")
today = date.today()
popup.title("View Subscriptions")
popup.minsize(1720,680)
popup.maxsize(2020,2000)
title_label = ttk.Label(popup, text="View Last Subscriptions", bootstyle="info", font=("",35))
title_label.pack()

columns = ("Start Date","End Date","Total Sub",  "Channel",  "URL", "ID")
sb = ttk.Scrollbar(popup, orient=ttk.VERTICAL)
sb.pack( side=RIGHT, fill=BOTH)

tree = ttk.Treeview(popup, height = 10, columns=columns, show="headings", bootstyle = SUCCESS)

tree.column("Start Date",  anchor=CENTER, minwidth=150)
tree.column("End Date",  anchor=CENTER, minwidth=150)
tree.column("Channel", anchor=CENTER,  minwidth=150)
#tree.column("Badge",  anchor=CENTER, minwidth=80)
tree.column("Total Sub",  anchor=CENTER, minwidth=200)
#tree.column("User Gifted", anchor=CENTER, minwidth=150)
tree.column("URL", anchor=CENTER, minwidth=200)
tree.column("ID", anchor=CENTER, minwidth=50)

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

def edit_subs():
  edit = ttk.Toplevel()
  edit.title("Edit Subscriptions")

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

  
  len_label = Label(edit, text="Subscription Length")
  len_label.pack()
  len_pick = Spinbox(edit, width=30, values=(1,3,6,12))
  len_pick.pack()


  channel_label = Label(edit, text="Channel")
  channel_label.pack()#grid(row = 2, column = 0)
  channel = Entry(edit, width = 30)
  channel.pack()#.grid(row=2, column = 1)

  total_label = Label(edit, text = "Total Subscriptions")
  total_label.pack()#grid(row=3,column=0)
  total = Entry(edit, width = 30)
  total.pack()#grid(row = 3, column = 1, padx=20)
  # badge_label = Label(edit, text="Badge")
  # badge_label.pack()#grid(row = 4, column = 0)

  # badge = Entry(edit, width = 30)
  # badge.pack()#grid(row = 4, column = 1, padx=20)
  
  # user_gifted_label = Label(edit, text="User Gifted")
  # user_gifted_label.pack()#grid(row = 5, column = 0)
  # user_gifted = Entry(edit, width = 30)
  # user_gifted.pack()#grid(row = 5, column = 1, padx=20)

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
        #badge.insert(0,sub[2])
        url.insert(0,sub[6])
        #user_gifted.insert(0,sub[5])
        
      # for sub in subs:
      #     print_subs +=  str(sub[3])   + " " + str(sub[4])  + " " + str(sub[5]) + "\n"   

      #query_label = Label(edit, text=print_subs)
     # query_label.grid(row = 3, columnspan = 2)

      conn.commit()
      conn.close()


  edit_query()

  
  def edit_end():
      edit.destroy()


 
  def update_query():
      conn = sqlite3.connect("subs.db")
      c = conn.cursor()
      
    #select_text.insert(0,sub[3])
      twitch_id = id#select_text.get()
      enddate = sdate.get()
      enddate = datetime.strptime(enddate, "%Y-%m-%d")

      c.execute("""UPDATE subs SET 
      start_date = :start,
      end_date = :end,
      channel = :channel,
      badge = :badge,
      url = :url,
      total_sub = :total,
      user_gifted = :user_gifted
    
      WHERE channel = :channel""",
      {
        'start':sdate.get(),
        'end': enddate.date() +  relativedelta(month=+int(len_pick.get())),
        'channel': channel.get(),
        #'badge': badge.get(),
        'total': total.get(),
        'url':  url.get(),#"twitch.tv/" + channel.get(),
        #'user_gifted': user_gifted.get(),
        'oid': twitch_id
      }
      )
      conn.commit()
      conn.close()
      edit.destroy()
  Update_window = ttk.Button(edit, text="Update", command=update_query)
  Update_window.pack(side=LEFT)

  close_window = ttk.Button(edit, text="Close", command=edit_end)
  close_window.pack(side=RIGHT)
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
      tree.insert("",  tkinter.END, values=(sub[0], sub[1], sub[3],  sub[4],sub[6], sub[7]))
  
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


select_label  =ttk.Label(popup, text = "Select Name:" )
select_label.pack()

select_text = Entry(popup, width = 20)
#select_text.insert(0, "1")
select_text.pack()#grid(row=  2,ipadx=0, sticky=S )
#select_text.configure(state=tkinter.DISABLED)
edit_btn = ttk.Button(popup, text="Edit Subscriptions", command=edit_subs, bootstyle=INFO ).pack(side=LEFT)

delete_btn = ttk.Button(popup, text="Delete Subscription",command=delete,  bootstyle = "danger").pack(side=RIGHT)#.grid(row = 3, sticky=E)


close_window = ttk.Button(popup, text="Close",  command=popup.quit, bootstyle = "info").pack(side=BOTTOM)



popup.mainloop()