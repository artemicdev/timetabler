from datetime import datetime
import threading
from time import sleep
from time import strftime
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu
import csv

#root settings
root = tk.Tk()
style = ttk.Style(root)
root.title("Hello world!")
root.geometry("400x100")
root.configure(bg="dark blue")
style.theme_use("clam")

destination = tk.StringVar()
nextstop = tk.StringVar()
destination.set("Destination station")
nextstop.set("Next station")

stationNumber = 0
stations = []
arrivetimes = []
stoplengths = []

buttonText = tk.StringVar()

#Create dest & next stop labels
destinationLabel = tk.Label(root, textvariable=destination, font="Arial 12 bold", fg='yellow', bg="dark blue", anchor="w")
destinationLabel.place(relwidth=0.5, relheight=0.2, relx=0,rely=0)
nextstopLabel = tk.Label(root, textvariable=nextstop, font="Arial 20 bold", fg='white', bg="dark blue", anchor="w")
nextstopLabel.place(relwidth=0.5, relheight=0.3, relx=0,rely=0.2)

#Clock ticker
def tick():
    clockstr = strftime("%T")
    hour = strftime("%H")
    minute = strftime("%M")
    second = strftime("%S")
    clock.config(text=clockstr)
    root.after(100, lambda: tick())

#Create clock
clock = tk.Label(root, font="Arial 20 bold", fg='white', bg="dark blue")
clock.pack(anchor="ne")
tick()

#Button & function
def onClick():
    global stationNumber

    stationNumber += 1

    try:
        nextstop.set(stations[stationNumber])
    except IndexError:
        destination.set("No route set")
        nextstop.set("---")
    procBtn["text"] = "Clicked!"

procBtn = tk.Button(text="Click to begin route",command=onClick)
procBtn.place(relx=0.5, rely=0.75, anchor="center")



#File dialogue function
def fileOpen():
    global stationNumber, stations, arrivetimes, stoplengths

    stationNumber = 0

    filetypes = [("Timetable files", "*.csv")]
    timetableFile = filedialog.askopenfile(filetypes=filetypes) # Request file

    timetable = csv.reader(timetableFile, delimiter=',') # Get file and read

    next(timetable) # Remove header row from data
    for row in timetable: # Create lists
        stations.append(row[0])
        arrivetimes.append(row[1])
        stoplengths.append(row[2])

    destination.set(stations[-1])
    nextstop.set(stations[stationNumber])

#Create menubar
menubar = Menu(root)
root.config(menu=menubar)

#Create open button in menu
menubar.add_cascade(
    label="Open",
    command=fileOpen
)

#Create exit button in menu
menubar.add_cascade(
    label="Exit",
    command=root.destroy
)

#Label
#hello = tk.Label(text="Hello world!")
#hello.place(relwidth=0.5, relheight=0.1, relx=0,rely=0.5)

tk.mainloop()
