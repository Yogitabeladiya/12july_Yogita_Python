# copy one file to another file 
f=open("t11.txt","r")
f1=open("b1.txt","a")

for i in f:
    f1.write(i)