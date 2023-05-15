
import csv
import pandas as pd
import subprocess

#this reads the CSV file with the format of first and second columns are each first and last name
#This is a bare bones search engine, will tune it to suite our specific needs later
data = []
#this takes the .csv library and makes it into a list called data
with open("/Users/garrett/Documents/GitHub/Grading-System/searchengine/details.csv",'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)
#print(data)
name = input("Enter students name: ")
col = [x[0] for x in data]
if name in col:
    for x in range(0,len(data)):
        if name == data[x][0]:
            print(data[x])
else: 
    print("Name does not exist.")