
import tkinter as tk
from tkinter import ttk
from navigationPane import NavigationPane

##      Food Planner      ##

class FoodPlanner:
    def __init__(self):
        self.root = tk.Tk()

        # Set up window geometry #
        self.window_with = 1440
        self.window_height = 900
        self.screen_w = self.root.winfo_screenwidth() 
        self.screen_h = self.root.winfo_screenheight()
        self.window_x = (self.screen_w/2) - (self.window_with/2)
        self.window_y = (self.screen_h/2) - (self.window_height/2)
        self.root.geometry("%dx%d+%d+%d" % (self.window_with, self.window_height, self.window_x, self.window_y))

        # Start building window content #
        self.root_frame = ttk.Frame(self.root)
        self.root_frame.grid(column=0, row=0)

        self.navigation_pane = NavigationPane(self.root_frame)
        self.navigation_pane.grid(column=0, row=0)

        self.root.mainloop()

if __name__ == "__main__":
    app = FoodPlanner()