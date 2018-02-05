import os
import sys
import time
import pybase64
import csv
Username = str(input("Enter Username: "))
LUser = str.lower(Username)
contents = []
Names = []
def RFile():
    F = open("Usernames.txt","r")
    if F.mode == "r":
        global contents
        contents = F.readlines()
    else:
        print("Fail")
        sys.exit
    F.close
def NSpace():
    for names in contents:
        Names.append(names.rstrip())
def Shutdown():
    print("Shutdown in 10")
    time.sleep(1)
    print("9")
    time.sleep(1)
    print("8")
    time.sleep(1)
    print("7")
    time.sleep(1)
    print("6")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
RFile()
NSpace()
def UsernameCheck():
    for x in Names:
        if LUser == x:
            if LUser == "circlegame" or LUser == "circle_game":
                print("Nice Try")
                print("""
              _ _
           .-/ / )
           |/ / /
           /.' /
          // .---.
         /   .--._\ 
        /    `--' /
       /     .---'
      /    .'
          /
                """)
                Shutdown()
            else:
                print("Invalid Username")
                Shutdown()
        else:
            None