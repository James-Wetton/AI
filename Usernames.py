import time
import os
FileUser = open("Usernames.txt","r")
#Lines = FileUser.readlines(1)
print(Lines)
CUser = str(input("Username: "))
cuser = str.lower(CUser)
for x in FileUser:
    if x == cuser:
        if cuser == "circlegame" or cuser == "circle_game":
            print("Nice try")
            print("""
               `+mmho/-  
            `/hNMMMMMMd. 
        `-+hNMMMMMMMMM-  
    `:yhdMMMMMMMMMMMMd   
  -sdMMMMMMMNsydMMMMm.   
 .oohMMMMMMM:  `sMMM-    
  +mmodMNMMM+`  hMMy     
 smo`oMm--odNdo+MMd.     
 `` /Mm.   `./sdNs`      
    dd.        ``
""")
        else:
            print("Invalid Username")
    else:
        print("null")
time.sleep(100)
