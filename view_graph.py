
import matplotlib 
from matplotlib.figure import Figure
import database as db
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
# graph = ttk.Window(themename="morph")

     
def query():
    #connect to db 
    conn = sqlite3.connect("subs.db")
    c = conn.cursor()
    #select all
    c.execute ("SELECT *, oid FROM subs ORDER BY End_date DESC")
    global subs
    subs = c.fetchall()
      #tree.insert("",  tkinter.END, values=(sub[7], sub[0], sub[1], sub[3],  sub[4],sub[6]))
    conn.commit()
    conn.close()
query()
sub_length = []
channels = []
spacing = 0.200
def plot():
    for sub in subs:
        print(sub)
        length = sub[3]
        sub_length.append(sub[3])
        channels.append(sub[4])
        print(length)
       # plt.hist(sub)
    
    mean = [np.mean(sub_length)]*len(sub_length)    
    plt.bar(channels, sub_length)
    plt.title("Subscriptions and Subscription length")
    plt.xlabel("Subscription Channels")
    plt.ylabel("Length (Months)")
    #plt.xticks(np.arange(0, len(sub_length)+5, 1))
    plt.xticks( fontsize=8)
    plt.plot(channels, mean, color = "red")
    #plt.tick_params(axis="x", which="major",pad= 20)
    plt.show()
    print(mean) 
    



# plot_btn = ttk.Button(graph, text="Plot button",  command=plot, bootstyle = "info").pack(side=LEFT)

# close_window = ttk.Button(graph, text="Close",  command=graph.quit, bootstyle = "info").pack(side=RIGHT)


