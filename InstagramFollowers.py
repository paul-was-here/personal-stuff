#Identifies instagram users followed by an account who do not follow the account back

#Takes a CSV with Column 0 being FOLLOWERS, Column 1 being FOLLOWING, and like anything in Column 3
#(because i honestly dont care to do it another way)

#settings
directory = "/users/ /Downloads/"
filename = "followersfollowing.csv"
doublecheck = False

import tkinter
from tkinter import *

def DataRetrieval():
    file = open(directory+filename, "r", errors="ignore", encoding = "utf-8")
    followers = []
    following = []
    for line in file:
        if line != "\n":
            followers.append(line.split(',')[0]) 
            following.append(line.split(',')[1])
    return(followers,following)

def Comparison():
    fwers,fwing = DataRetrieval()
    display = tkinter.Tk(className="Not following back:")
    
    #attemps to sort of deal with repeated entries for each user (username + display name) by skipping one
    i = 0
    check = []
    while i < len(fwing):
        if fwing[i] not in fwers:
            label = Label(display,text=(fwing[i]+"\n"+fwing[i+1]))
            label.pack()
            #print(fwing[i]+"\n"+fwing[i+1]+"\n")
            check.append(fwing[i])
        i+=2
    display.mainloop()

    #check-step in case any the messy iteration missed any
    if doublecheck == True:
        for item in fwing:
            if (item not in fwers) and (item not in check):
                print("Missed: "+item)

Comparison()