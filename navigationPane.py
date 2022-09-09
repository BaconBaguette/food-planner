
import tkinter as tk
from tkinter import ttk

##      Navigation Pane      ##
class NavigationPane(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.nav_pane = ttk.Frame(master)
        self.nav_pane.grid(column=0, row=0)

        self.plan_meals_button = ttk.Button(self.nav_pane, text="Plan Meals")
        self.plan_meals_button.grid(column=0, row=0)