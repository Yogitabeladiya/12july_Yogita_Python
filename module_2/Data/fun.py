import random

def getdata():
        x=random.randint(111,999)
        name=input("enter name")
        nm1=name.upper()
        sub=input("enetr sub")
        city=input("enetr city",city)
        print(x)
        print(name)
        print(sub)
        list=[x,nm1,sub,city]        
        print(list)

def st():
        
        for i in range(5):
         x=random.randint(111,999)
         nm=input("enter name ")
         sub=input("enter sub ")
         city=input("enyter city")

         print("name",nm)
         nm1=nm.upper()
         print("subect",sub)
         print("city",city)
         a=[x,nm1,sub,city]
         print(a)
