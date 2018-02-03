import os
import sys
Username = str(input("Enter Username: "))
LUser = str.lower(Username)
contents = []
def RFile():
    F = open("Username.txt","r")
    if F.mode == "r":
        content = F.readlines() """Wont go outside function"""
        print(content)
        return contents
    else:
        print("Fail")
        sys.exit
    F.close
RFile()

print(contents)
print(LUser)
os.system("pause")


for x in contents:
    print(x)
    os.system("pause")
    if x == LUser:
        if LUser == "circlegame" or LUser == "circle_game":
            print("Nice Try")
        else:
            print("Invalid Username")
    else:
        print("Fail")
        os.system("pause")