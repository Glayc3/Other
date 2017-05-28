try:
    from Tkinter import *              # Python 2
    import ttk
except ImportError:
    from tkinter import *   # Python 3
    print("Using P3 protocol")
from turtle import *
import time

ht()
pencolor("white")
getscreen().bgcolor("black")
getscreen().screensize(3000, 3000)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]

#-----------------------------------------------------------#

turn_angle = 90
forward_distance = 1
speed(0)

#-----------------------------------------------------------#

class stateMonitor:

    def __init__(self, master):
        self.master = master

        self.progress = IntVar(self.master)
        self.size = 0
        self.max = 0

        self.stateLabel = Label(master, text="State:")
        self.stateText = Label(master)

        self.levelLabel = Label(master, text="Level:")
        self.levelText = Label(master)

        self.progressLabel = Label(master, text="Progress:")
        self.progressBar = ttk.Progressbar(master, orient="horizontal", mode="determinate", length=200, variable=self.progress)
        self.progressText = Label(master)

        self.currentSizeLabel = Label(master, text="Current Size:")
        self.currentSizeText = Label(master)

        self.stateLabel.grid(row=1, column=0)
        self.stateText.grid(row=1, column=1)
        self.levelLabel.grid(row=2, column=0)
        self.levelText.grid(row=2, column=1)
        self.progressLabel.grid(row=3, column=0)
        self.progressBar.grid(row=3, column=1)
        self.progressText.grid(row=4, column=1)
        self.currentSizeLabel.grid(row=5, column=0)
        self.currentSizeText.grid(row=5, column=1)

    def setState(self, state):
        self.stateText.config(text=state)

    def setProgressTarget(self, level):
        self.levelText.config(text=str(level))
        self.max = 2**(level-1)-1
        self.progressBar.config(maximum=self.max)

        self.resetProgress()

    def incProgress(self):
        self.progress.set(self.progress.get()+1)
        self.size += 1

        self.progressText.config(text=str(self.progress.get())+"/"+str(self.max))
        self.currentSizeText.config(text=str(self.size))

    def resetProgress(self):
        self.progress.set(0)



def getNextFractalString(iterations):
    string = ""
    xstring = ""

    for i in range(iterations):
        prenewstring = string[::-1]
        newstring = ""

        for i in prenewstring:
            newstring = newstring + ("L" if i == "R" else "R")

        xstring = "R" + newstring
        string = string + xstring


    return xstring

root = Tk()
app = stateMonitor(root)

#-----------------------------------------------------------#
i = 0
color = 0

while True:
    root.update_idletasks()
    root.update()

    i += 1
    color = 0 if color == 6 else color + 1
    pencolor(colors[color])

    #print("Generating level " + str(i) + "...")
    app.setState("Generating Fractal String...")
    moves = getNextFractalString(i)
    app.setProgressTarget(i)
    #print("Doing level " + str(i) + " : Size " + str((2**i)/2+1) + " : Total Size " + str(2**i+1) + "...")
    app.setState("Drawing Fractal Level")

    for move in moves:
        root.update_idletasks()
        root.update()
        app.incProgress()

        fd(forward_distance)


        if move == "R":
            right(turn_angle)
        else:
            left(turn_angle)


    #print("Done")



#-----------------------------------------------------------#

while True:
    pass
