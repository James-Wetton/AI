import time
import random
import csv
import os
import sys
from sys import argv
import pybase64
import getpass
from string import ascii_lowercase
from string import punctuation
from collections import Counter
csvNames = []
UserPass = ""
usernamecheck = 0
UserID = ""
def getCSV():
    with open("AI-datatemplate.csv","r") as csv_file:
        reader = csv.reader(csv_file)
        for x in reader:
            for y in x:
                if y == "Username":
                    global csvNames
                    csvNames = x
                else:
                    None
def getCSV():
    dataCounter = 1
    rowCounter = 0
    limitSwitch1 = False
    with open("AI-datatemplate.csv","r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            for data in row:
                if data == UserPass:
                    limitSwitch1 = True
                elif data != UserPass and limitSwitch1 == False:
                    dataCounter = dataCounter + 1
                else:
                    None
        csv_file.close
    with open("AI-datatemplate.csv","r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            rowCounter = rowCounter + 1
            if rowCounter == 2:
                for data in row:
                    if dataCounter == 0:
                        global Pass
                        Pass = data
                    else:
                        dataCounter = dataCounter - 1
getCSV()
x = 1 #timer variable
print(csvNames)
while usernamecheck == 0:
    try:
        print("To restart, type \'quit()\' in any field")
        time.sleep(x)
        foo = ['Have we spoken before? ', 'Wait, have we spoken before? ', 'Have we met? ', 'Hey there! Do I know you? ', 'Do I know you? ']
        ask = random.choice(foo)
        used = input(ask)
        time.sleep(x)
        if used == ('quit()'):
            break
        if used in ('Y', 'Yes', 'y', 'yes', 'Yeah', 'yeah'):
            randomqu = ['What\'s your name? ', 'What\'s your name again? ', 'I Don\'t remember your name! What is it again? ']
            username = input(random.choice(randomqu))
            for x in csvNames:
                if username == x:
                    UserID = x
                    usernamecheck = 1
                    UserPass = str(input("Insert Password: "))
                else:
                    None
        else:
            randomqn = ['What\'s your name? ', 'So, what\'s your name? ', '']
            name = input("What's your name? ")
            time.sleep(x)
            if name == ('quit()'):
                pass
            else:
                print("Nice to meet you " + name + "!")
                f = open(name + '.txt', 'w')
                f.write(name + '\n')
                time.sleep(x)

                age = input("How old are you? ")
                time.sleep(x)

                print("You are already " + str(age) + " years old!")
                f.write(str(age) + '\n')
                time.sleep(x)

                colour = input("So, " + name + " , what's your favourite colour? ")
                time.sleep(x)
                f.close()

                f = open('colour.txt', 'r')
                all_lines = f.readlines()
                colour = colour + '\n'
                if colour.lower() in all_lines:
                    if all_lines.count(colour) > 1:
                        amount = "people"
                        like = "like"
                    else:
                        amount = "person"
                        like = "likes"
                    colour = colour.lower()
                    print("I know " + str(all_lines.count(colour)) , amount, "who", like, "the colour " + colour[:-1] + "!")
                else:
                    print("You have good tastes!")
                time.sleep(x)
                print("I really love " + colour[:-1] + " too !")
                f.close
                f = open('colour.txt', 'a')
                f.write(colour + '\n')
                f.close()
                f = open(name + '.txt', 'a')
                f.write(colour + '\n')

                time.sleep(2)

                print("Hey, I think to keep your data secure, we should add a password.")
                makepass = 0
                while makepass == 0:
                    f = open(name + '_password.txt', 'w')
                    time.sleep(2)
                    password = str(input("What would you like your password to be? \nP.S. make it something you will remember...\nmake it at least 5 letters long "))
                    f.write(password)
                    f.close()
                    f = open(name + '_password.txt', 'r')
                    characters = 0
                    for line in f:
                        characters = characters + len(line)

                    if characters > 4:
                        print("Great! I don't think anyone will crack that one...")
                        f.close()
                        makepass = 1
                        time.sleep(x)
                    else:
                        time.sleep(x)
                        print("I think that is going to be to easy to crack! Please make it at least 5 letters long")
                        pass
                f = open(name + '_password.txt', 'w')
                encodedpass = password.encode('utf-8')
                cr = pybase64.standard_b64encode(encodedpass)
                cr = cr.decode('utf-8')
                print("Encrypting password...")
                f.write(cr)
                f.write('\n')
                time.sleep(x)
                f.close()
                print()

    except KeyboardInterrupt:
        break
