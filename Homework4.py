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
__author__ = 'jstahle'
#Homework4_3
import os
import shelve

from datetime import datetime

def count_frequency (mylist):
    result={}

    for each_word in mylist:
        if result.get(each_word)==None:
            result[each_word]=1
        else:
            result [each_word] = result [each_word] +1
    return result

mylist=[1,2,11,1,3,2,11,3,7,11,1,2,11,1,3,1,11,3,7,11,1,2,11,1,3,2,11,3,7,11,1,2,11,1,3,2,11,3,7,1]

dt1 = datetime.now()
print(dt1)

count_frequency(mylist)

print(datetime.now()-dt1)

dt1 = datetime.now()
s = shelve.open("homework4")
s["flower"]=(1,2,11,1,3,2,11,3,7,11,1,2,11,1,3,1,11,3,7,11,1,2,11,1,3,2,11,3,7,11,1,2,11,1,3,2,11,3,7,1)
s.close()

print(datetime.now()-dt1)

