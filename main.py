# Live Quadratic Plotter
# A Tkinter based GUI application for live plotting of quadratic functions using matplotlib.

from tkinter import *
from matplotlib import *

# Plotting Function
def plotFunction(s2, s1, s0):
    print("Value Changed")


# GUI Function
def gui():
    # Basic Window Parameters
    master = Tk()
    master.title("BMI Calculator")

    # Create GUI Variables
    s2 = StringVar()
    s2.set("")

    s1 = StringVar()
    s1.set("")

    s0 = StringVar()
    s0.set("")

    # Labels & Entries
    s2_label = Label(master, text="S²")
    s2_label.grid(row=0, column=0)
    s2_entery = Entry(
        master, width=15, borderwidth=3, textvariable=s2
    )  # The 'textvariable' parameter automatically updates variable
    s2_entery.grid(row=1, column=0)

    s1_label = Label(master, text="S¹")
    s1_label.grid(row=2, column=0)
    s1_entery = Entry(master, width=15, borderwidth=3, textvariable=s1)
    s1_entery.grid(row=4, column=0)

    s0_label = Label(master, text="S⁰")
    s0_label.grid(row=5, column=0)
    s0_entery = Entry(master, width=15, borderwidth=3, textvariable=s0)
    s0_entery.grid(row=6, column=0)

    # Trace Functions
    # Watch the values and execute the plotFunction on change
    s2.trace("w", plotFunction)
    s1.trace("w", plotFunction)
    s0.trace("w", plotFunction)

    master.mainloop()


# Start GUI
gui()