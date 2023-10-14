# nnumber of line read 
f1=open("t11.txt","r+")
n=int(input("Enter n"))
for i in range(1,n+1):
  print(f1.readlines(i))