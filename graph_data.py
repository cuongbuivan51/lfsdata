import sqlite3
from sqlite3 import Error
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation as animate
import math
fig = plt.figure()
YawGraph = fig.add_subplot(2,2,1)
ax = []
ay = []
def Yaw_Graph_animate(heading,time):
    xs = ax.append(time)
    ys = ay.append(heading)
    YawGraph.plot(xs,ys)
    plt.title("Du lieu Yaw")
    plt.xlabel("Time")
    plt.ylabel("Yaw")
    return ax,ay
def main():
    database = "LFS.db"
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        print("Collected to database sqlite")
    except Error:
        print("Cannot query",Error)
    # All Data
    cur.execute("SELECT * FROM datas")
    records = cur.fetchall()
    for row in records:
       print(row)
    # Yaw graph
    cur.execute("SELECT Heading, time FROM datas")
    for row1 in cur.fetchall():
        Yaw_Graph_animate(math.degrees(row1[0]),row1[1])
    ani = animate.FuncAnimation(fig,animate,fargs=(ax,ay),interval=1)
if __name__ == '__main__':
    main()

