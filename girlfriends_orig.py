#!/usr/bin/env python3
#Girlfriends 1:
name = input("Enter your name: ")

if name is "Ashley":
    print("Hey there cutie.")
elif name is "Melissa":
    print("Screw you.")
elif name is "Patty":
    print("Hello little devil.")
else:
    print(name + ", idk who you are.")

#Girlfriends 2:
resp = input("What is your name? ")

if "Ashley" in resp:
    print  ("Hey there cutie.")
elif "Melissa" in resp:
    print ("Screw you.")
elif "Patty" in resp:
    print ("Hello little devil.")
else:
    print (resp + ", idk who you are.")
