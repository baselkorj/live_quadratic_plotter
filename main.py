# Live Quadratic Plotter
# A Tkinter based GUI application for live plotting of quadratic functions using matplotlib.


from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Plotting Function
def plotFunction(a, b, c):

    x = np.linspace(-10, 10, num=1000)  # X limt and values
    y = [(a * i ** 2 + b * i + c) for i in x]  # Quadratic fucntion
    figure = plt.figure(
        figsize=(4, 3), dpi=100
    )  # plot the figure and define the size and resolution
    figure.add_subplot(111).plot(x, y)  # plot x and y
    chart = FigureCanvasTkAgg(figure, master)  # add the figure to the main window
    chart.get_tk_widget().grid(row=8, column=8)
    plt.grid()


# GUI Function
def gui():
    global s2, s1, s0, master
    # Basic Window Parameters
    master = Tk()
    master.title("LiveQuadraticPloter")
    master.geometry("800x650")

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

    Btton = Button(
        master,
        text="Graph it",
        command=lambda: plotFunction(
            int(s2_entery.get()), int(s1_entery.get()), int(s0_entery.get())
        ),
    )

    Btton.grid(row=4, column=1)

    # Trace Functions
    # Watch the values and execute the plotFunction on change

    # s2.trace("w", plotFunction)
    # s1.trace("w", plotFunction)
    # s0.trace("w", plotFunction)
    master.mainloop()


# try to push
# Start GUI
gui()
plotFunction()