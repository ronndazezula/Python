"""
IMPORTANT - See README before running
"""
#! /usr/bin/python (sandbox: attempt to allow user to double-click to run)

from tkinter import *
import tkinter as tk
import FileXfer_gui
import FileXfer_func
import os

#app frame
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(520,200))
        self.master.title("Modified File Transfer (copy files to Corporate HQ)")
        self.master.config(bg='#b0c4de')

#gui functions | widgets
        FileXfer_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
