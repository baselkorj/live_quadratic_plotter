# Live Quadratic Plotter
# A Tkinter based GUI application for live plotting of quadratic functions using matplotlib.
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Creating Variables

        self.s2 = tk.IntVar()
        self.s1 = tk.IntVar()
        self.s0 = tk.IntVar()

        # Trace Function
        self.s2.trace("w", self.plotFunction)
        self.s1.trace("w", self.plotFunction)
        self.s0.trace("w", self.plotFunction)

        # Setting Default Values to 0
        self.s2.set(0)
        self.s1.set(0)
        self.s0.set(0)

        # Labels & Entries
        self.s2_label = tk.Label(self, text="S²").place(x=10, y=1)
        self.s2_entry = tk.Entry(
            self, width=15, borderwidth=3, textvariable=self.s2
        ).place(x=10, y=21)

        self.s1_label = tk.Label(self, text="S¹").place(x=10, y=56)
        self.s1_entry = tk.Entry(
            self, width=15, borderwidth=3, textvariable=self.s1
        ).place(x=10, y=76)

        self.s0_label = tk.Label(self, text="S⁰").place(x=10, y=111)
        self.s0_entry = tk.Entry(
            self, width=15, borderwidth=3, textvariable=self.s0
        ).place(x=10, y=131)

        # Trace Function
        if self.s2 == None or self.s1 == None or self.s0 == None:
            self.s2.set(0)
            self.s1.set(0)
            self.s0.set(0)

            print("wating for input: ")

        else:
            self.s2.trace("w", self.plotFunction)
            self.s1.trace("w", self.plotFunction)
            self.s0.trace("w", self.plotFunction)

    # Defining Plot Function
    def plotFunction(self, *args):
        # Get Variables
        s2_plot = self.s2.get()
        s1_plot = self.s1.get()
        s0_plot = self.s0.get()

        s2 = int(s2_plot)
        s1 = int(s1_plot)
        s0 = int(s0_plot)
        x = np.linspace(-10, 10, num=1000)  # X limit and values
        y = [(s2 * i ** 2 + s1 * i + s0) for i in x]  # Quadratic function
        figure = plt.figure(
            figsize=(4, 3), dpi=100
        )  # plot the figure and define the size and resolution
        figure.add_subplot(111).plot(x, y)  # plot x and y
        chart = FigureCanvasTkAgg(figure, self)  # add the figure to the main window
        chart.get_tk_widget().place(x=155, y=10)
        plt.grid()


if __name__ == "__main__":
    app = App()
    app.title("Live Quadratic Plotter")
    app.geometry("560x320")
    app.mainloop()
