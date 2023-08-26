import datetime
t=datetime.datetime.now()
def y1():
   f1=open('v1.txt','a')
   Name=input("\tPython E-Note Generator Name:-")
   if Name.isalpha():
    f1.write(f"Name:-{Name}\n")
    print("sucessfully enter name ") 
   else:
     print("error")
     print("pls enetr aplhabet")
     Name=input("\tPython E-Note Generator Name:-")

   Title=input("\tPython E-Note Book Title:-:")
   if Title.isupper():
    f1.write(f"Title:-{Title}\n")
   else:
      print("invalid")
      Title=input("\tPython E-Note Book Title:-:")

   Content=input("\tPython E-Note Book Content:-:")
   if Content.islower():
      f1.write(f"Content:-{Content}\n {t}\n")
   else:
     print("invalid ")
     Content=input("\tPython E-Note Book Content:-:")


   '''print("\tPython E-Note Generator Name:- ",Name)
   print("\tPython E-Note Book Title:- ",Title)
   print("\tPython E-Note Book Content:- ",Content)'''
   '''if Name.isalnum:
    f1.write(f"Name:-{Name}\n")
    print("Python E-Note Generator Name:-")
   else:
     print("error : invalid ")'''
   '''if Title.isupper():
    f1.write(f"Title:-{Title}\n")
   else:
      print("invalid")'''
   '''if Content.islower():
      f1.write(f"Content:-{Content}\n {t}\n")
   else:
     print("invalid ")
'''
def view():
   f1=open('v1.txt','r')
   print(f1.read())


