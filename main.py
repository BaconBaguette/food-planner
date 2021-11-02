
import tkinter as tk
from tkinter import ttk

##      Food Planner      ##

class FoodPlanner:
    def __init__(self):
        self.root = tk.Tk()

        self.window_w = 1440
        self.window_h = 900
        self.screen_w = self.root.winfo_screenwidth() 
        self.screen_h = self.root.winfo_screenheight()
        self.window_x = (self.screen_w/2) - (self.window_w/2)
        self.window_y = (self.screen_h/2) - (self.window_h/2)
        self.root.geometry("%dx%d+%d+%d" % (self.window_w, self.window_h, self.window_x, self.window_y))

        self.root.mainloop()

if __name__ == "__main__":
    app = FoodPlanner()