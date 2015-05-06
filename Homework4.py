__author__ = 'jstahle'
#Jay Stahle
#Homework4
#Problem1

import os

def traverse(path, promptedFile):
    #print(path)
    l=os.listdir(path)
    for f in l:
        if f == promptedFile:
            print(os.path.join(path,f))
            break
        elif os.path.isdir(os.path.join(path,f)):
            traverse(os.path.join(path,f),promptedFile)

path=input("Please enter the start path")
promptedFile=input("Please enter the search file")

traverse(path,promptedFile)

#Problem 2

__author__ = 'jstahle'
#Jay Stahle
#Homework4_2

import os

filename=input("Please enter fullpath for filename to read")

isfound=False

with open(filename,"r") as f:
    for line in f:
        if "password=" in line:
            isfound=True
            break

if isfound:
    print("Security is bad")
else:
    print("Security is good")

#Problem 3

