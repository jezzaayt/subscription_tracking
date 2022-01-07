
import matplotlib 
from matplotlib.figure import Figure
import database as db
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
import random 
import decimal

     
def query():
    #connect to db 
    conn = sqlite3.connect("subs.db")
    c = conn.cursor()
    #select all
    c.execute ("SELECT *, oid FROM subs ORDER BY total_sub DESC")
    global subs
    subs = c.fetchall()
    conn.commit()
    conn.close()
query()
sub_length = []
channels = []
spacing = 0.200
type = []
def plot():
    for sub in subs:
        print(sub)
        if sub[3] == "":
            print("exit")
            continue
        else:
            length = sub[3]
            sub_length.append(sub[3])
            channels.append(sub[4])
            type.append(sub[7])
        print(length)
       # plt.hist(sub)
    plt.figure(num="Subscriptions Graph")
    rand = decimal.Decimal(random.randrange(2,5))/10
    #mean = [np.mean(sub_length)]*len(sub_length)    
    bar = plt.bar(channels, sub_length)
    plt.title("Subscriptions and Subscription length")
    plt.xlabel("Subscription Channels")
    plt.ylabel("Length (Months)")
    #plt.xticks(np.arange(0, len(sub_length)+5, 1))
    def autolabel(rects):
        for idx, rect in enumerate(bar):
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width()/2, rand*height,
            type[idx],
            ha="center", va="bottom", rotation=90)
    autolabel(bar)
    plt.xticks( fontsize=8)
    plt.plot(channels, sub_length, alpha=0.1)
    #plt.tick_params(axis="x", which="major",pad= 20)
    
    plt.tight_layout()
    plt.show()
    #print(mean) 
    



# plot_btn = ttk.Button(graph, text="Plot button",  command=plot, bootstyle = "info").pack(side=LEFT)

# close_window = ttk.Button(graph, text="Close",  command=graph.quit, bootstyle = "info").pack(side=RIGHT)


