"""
Run from FileXfer_main.py after consulting README.txt
"""

import shutil
import sqlite3
import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
import datetime
import random, datetime
from tkinter import messagebox
import getpass
import FileXfer_main
import FileXfer_gui

def origDir(self): #choose dir to copy files from, default to customary
    origin = askdirectory(initialdir="..\FileXferAssign\WorkingFiles\\")
    if origin:
        self.varOrig.set(origin)

def destDir(self): #choose dir to copy files to, default to customary
    destination = askdirectory(initialdir="..\FileXferAssign\HomeOffice\\")
    if destination:
        self.varDest.set(destination)

def GetFiles(self): #store file names, location, and getmtime
    files = []
    logDb = {}
    origin = self.varOrig.get()
    destination = self.varDest.get()
    fileList = os.listdir(path=origin)

    for file in fileList:
            files.append(file)
            shutil.copy(os.path.join(origin,file),destination) #copy files from directory to destination
            for name in files: #create absolute path for getmtime
                dPath = os.path.join(destination, name)
                mTime = os.path.getmtime(dPath)
                logDb[name] = mTime
    createDb(self, logDb)

def createDb(self, logDb): #create DB and table, insert values in table
    user = getpass.getuser()
    conn = sqlite3.connect("FileXfer_log.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_HQxfers(\
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                    col_fileName TEXT,\
                    col_timeCopied REAL,\
                    col_copiedBy TEXT)")
        for file, value in logDb.items():
            cur.execute("INSERT INTO tbl_HQXfers (col_fileName, col_timeCopied, col_copiedBy) VALUES (?,?,?)",(file, logDb[file], user))
            conn.commit()
        cur.execute("SELECT col_fileName, col_copiedBy, col_timeCopied FROM tbl_HQXfers") #print session info in console
        rows = cur.fetchall()
        for session in rows:
            print(session)
    conn.close()
    messagebox.showinfo("Process complete!","Files from the selected directory were copied to: {}. Click 'OK' then 'Exit' to leave the application".format(self.varDest.get())) #confirms where files copied to

def closeApp(self):
    hour = datetime.datetime.now().hour
    greeting = "Have a nice day!" if hour<20 else "Good night!" #gives varied message depending on time of day/night
    messagebox.showinfo("See you next time.",random.choice([greeting]))
    self.master.destroy()
    os._exit(0)
 
if __name__ == "__main__":
    pass
