
#Write a Python program to read a random line from a file. 

import random
f1= open("y2.txt",'r') 
lines=f1.readlines()
print(random.choices(lines))