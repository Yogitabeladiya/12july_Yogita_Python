'''f1=open('new.file.txt','w')


for i in range(1,101):
    f1.write(f"{i}\n")'''

import datetime
x=datetime.datetime.now()

f1=open('file1.txt','w')

for i in range(4):
    id=input("enter number")
    name=input("enetr name ")
    city=input("enetr city ")
    f1.write(f"id :{id}\n name:{name}\n city:{city}\n{x}\n")