# last n number of line 
f=open("t11.txt","r")
n=int(input("Enter last line of code "))
for i in range(1,n):
    print(f.read())
