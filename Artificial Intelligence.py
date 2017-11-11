import time
import glob
import os

x = 1

used = input("Have you used this Database before, Y/N? ")
time.sleep(x)
if used == ('Y'):
    usernamecheck = 0
    while usernamecheck == 0:
        username = input("What name was your account entered under? ")
        if username == ("restart"):
            break
            python 
        if os.path.exists(username + '.txt'):
            print("Found an account under the name " + username)
            f = open(username + '.txt', 'r')
            name = f.readline()
            age = f.readline()
            colour = f.readline()
            print("Your name is " + name + "and you're " + str(age) + " ")
            print("Your favourite colour is " + colour)
            correct = input("Is this the correct account? Y/N ")
            if correct == ('Y'):
                print("I thought so...")
                usernamecheck = usernamecheck + 1
            else:
                print("Sorry")
    else:
        print("No results were found for " + username)
        print("Please reload the program and try again or make a new account")

else:
    name = input("What's your name? ")
    time.sleep(x)

    print("Nice to meet you " + name + "!")
    f = open(name + '.txt', 'w')
    f.write(name + '\n')
    time.sleep(x)

    age = input("What's your age? ")
    time.sleep(x)

    print("You are already " + str(age) + " years old!")
    f.write(str(age) + '\n')
    time.sleep(x)

    colour = input("So, " + name + " , what's your favourite colour? ")
    time.sleep(x)

    print("I really love " + colour + " too !")
    f.write(colour + '\n')
    f.close()

