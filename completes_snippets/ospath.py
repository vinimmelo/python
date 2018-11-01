# -*- coding: utf-8 -*-
"""
Created on September 15

@author: vinimmelo

Training the use of OS library.
"""

import os, shelve

boringStuff = os.path.join('C:\\', 'Users', 'vinimmelo', 'OneDrive - NESTLE', 'Importante', 'Programs', 'Python', 'BoringStuff')
deskDir = r'C:\Users\vinimmelo\Desktop\\'

def os_samples():
  print(os.getcwd()) #get the actual working directory
  os.chdir(boringStuff) #change the directory
  print(os.getcwd()) #Get the current working directory
  print(os.listdir()) #Show the files in directory
  print(os.path.getsize(boringStuff)) #Verify size of path/file
  print(os.path.exists(boringStuff))  #Verify if the path exist
  print(os.path.isdir(boringStuff)) #verify if is directory
  print(os.path.isfile(boringStuff)) #Verify if is a file
  return None


def files_handling():
    #print(os.path.isfile(deskDir))
    baconFile = open(deskDir + r'bacon.txt', 'w') #open file
    baconFile.write('Hello World!\n')
    baconFile.close()

    baconFile = open(deskDir + 'bacon.txt', 'a')
    baconFile.write('Bacon is not a vegetable')
    baconFile.close()

    baconFile = open(deskDir + 'bacon.txt', 'r')
    content = baconFile.read()
    baconFile.close()
    print(content)
    #os.read() #read file
    #os.read() #write file
    #os.close() #close file

def shelve_test(): #used to save variables and data used in the program (VERY GOOD)
    shelveFile = shelve.open(deskDir + 'mydata') #save in 3 different files.
    cats = ['Zophie', 'Pooka', 'Simon']
    shelveFile['cats'] = cats
    shelveFile.close()
    shelveT = shelve.open(deskDir + 'mydata')
    print(type(shelveT))
    print(shelveT['cats'])
    print(list(shelveT.items()))
    print(list(shelveT.values()))
    shelveT.close()



if __name__ == '__main__':
    shelve_test()
