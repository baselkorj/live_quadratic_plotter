# Live Quadratic Plotter
# A Tkinter based GUI application for live plotting of quadratic functions using matplotlib.
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Creating Variables

        self.s2 = tk.StringVar()
        self.s1 = tk.StringVar()
        self.s0 = tk.StringVar()

        # Trace Function
        self.s2.trace("w", self.plotFunction)
        self.s1.trace("w", self.plotFunction)
        self.s0.trace("w", self.plotFunction)

        # Setting Default Values to 0
        self.s2.set(0)
        self.s1.set(0)
        self.s0.set(0)

        # Labels & Entries
        self.s2_label = tk.Label(self, text="S²").grid(row=0, column=0, columnspan=1)
        self.s2_entry = tk.Entry(
            self, width=15, borderwidth=3, textvariable=self.s2
        ).grid(row=1, column=0)

        self.s1_label = tk.Label(self, text="S¹").grid(row=2, column=0)
        self.s1_entry = tk.Entry(
            self, width=15, borderwidth=3, textvariable=self.s1
        ).grid(row=3, column=0)

        self.s0_label = tk.Label(self, text="S⁰").grid(row=4, column=0)
        self.s0_entry = tk.Entry(
            self, width=15, borderwidth=3, textvariable=self.s0
        ).grid(row=5, column=0)

    # Defining Plot Function
    def plotFunction(self, *args):
        # Get Variables
        s2_plot = int(self.s2.get())
        s1_plot = int(self.s1.get())
        s0_plot = int(self.s0.get())

        x = np.linspace(-10, 10, num=1000)  # X limit and values
        y = [
            (s2_plot * i ** 2 + s1_plot * i + s0_plot) for i in x
        ]  # Quadratic function
        figure = plt.figure(
            figsize=(4, 3), dpi=100
        )  # plot the figure and define the size and resolution
        figure.add_subplot(111).plot(x, y)  # plot x and y
        chart = FigureCanvasTkAgg(figure, self)  # add the figure to the main window
        chart.get_tk_widget().place(x=150, y=89)
        plt.grid()


if __name__ == "__main__":
    app = App()
    app.geometry("600x600+120+120")
    app.mainloop()
