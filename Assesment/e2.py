import datetime
t=datetime.datetime.now()

def y1():
   f1=open('v1.txt','a')
   Title=input("\tPython E-Note Book Title:-:")
   if Title.isupper():
     f1.write(f" Time:-{t}\n Title:-{Title}\n")
   else:
     print(" Error... : Enter in uppercase")
     y1()
   
def y2():
     f1=open('v1.txt','a')
     Content=input("\tPython E-Note Book Content:-:")
     if Content.islower():
      f1.write(f"Content:-{Content}\n")
     else:
       print(" Error.... : Enter content in lower ")
       y2()

def y3():
     f1=open('v1.txt','a')
     Name=input("\tPython E-Note Generator Name:-")
     if Name.isalpha()or Name.isspace():
          f1.write(f"\t          Name:-{Name}\n")
          f1.write("\n-------------------------------\n")
     else:
         print("Error... Enter name only alpha ")
         y3()
   
def y4():

   User=input("Enter Choice  User Add Content or exit ")
   if User=='add':
    y1()
    y2()
    y3()
   else:
      print("exit")

def y5():
    for i in range(5):
      y4()
   
def view():
   f1=open('v1.txt','r')
   print(f1.read())


