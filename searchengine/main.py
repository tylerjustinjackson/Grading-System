
import csv
import pandas as pd
import subprocess
from tkinter import *
from tkinter import filedialog
#This creates a window to prompt the user to select the file they choose to search

#this reads the CSV file with the format of first and second columns are each first and last name
#This is a bare bones search engine, will tune it to suite our specific needs later

data = []
#this takes the .csv library and makes it into a list called data
def openFile():
    filepath = filedialog.askopenfilename()
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
window = Tk()
button = Button(text='Open', command=openFile)
button.pack()
window.mainloop()
# #print(data)
def searchfile():
    name = input("Enter students name: ")
    col = [x[0] for x in data]
    if name in col:
        for x in range(0,len(data)):
            if name == data[x][0]:
                print(data[x])
    else: 
        print("Name does not exist.")
window = Tk()
button = Button(text='Open', command=openFile)
button.pack()
searchfile()
window.mainloop()