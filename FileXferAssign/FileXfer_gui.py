"""
Run from FileXfer_main.py after consulting README.txt
"""

import tkinter as tk
from tkinter import *
import os
import FileXfer_main
import FileXfer_func

#create: browse buttons, entry fields, copy button, and exit button
def load_gui(self):

    self.varOrig = StringVar()
    self.varDest = StringVar()

#button for source directory (choose files to copy)
    self.btn_selOrig = Button(self.master,width=12,height=1,text='Get files from...',command=lambda:FileXfer_func.origDir(self)) #directory browse button
    self.btn_selOrig.grid(row=2,column=0,padx=(20,0),pady=(45,10),sticky=N+W)
#shows source directory (entry field)
    self.txt_origDir = tk.Entry(self.master,text=self.varOrig,width=60)
    self.txt_origDir.grid(row=2,column=1,columnspan=2,padx=(15,0),pady=(40,7))

#button for destination directory (copy files to)
    self.btn_selDest = Button(self.master,width=12,height=1,text='Copy files to...',command=lambda:FileXfer_func.destDir(self)) #destination browse button
    self.btn_selDest.grid(row=3,column=0,padx=(20,0),sticky=N+W)
#shows destination directory (entry field)
    self.txt_destDir = tk.Entry(self.master,text=self.varDest, width=60)
    self.txt_destDir.grid(row=3,column=1,columnspan=2,padx=(15,0),pady=(0,10))

#button to fire copy
    self.btn_copyFiles = Button(self.master,width=12,height=2,text='Copy files...', command=lambda:FileXfer_func.GetFiles(self)) #transfer button
    self.btn_copyFiles.grid(row=4,column=0,padx=(20,0),pady=(5,0),sticky=N+W)

#button to exit app
    self.btn_exit = Button(self.master,width=12,height=2,text='Exit',command=lambda:FileXfer_func.closeApp(self)) #close button
    self.btn_exit.grid(row=4,column=2,padx=(285,0))

if __name__ == "__main__":
    pass
