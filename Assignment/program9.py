# add list to file 
l1=["hello","tops","technology"]
f=open("t11.txt","r+")
for l in l1:
  f.write(f"{l}\n")
  print(f.read())
print("print sucessfully")

