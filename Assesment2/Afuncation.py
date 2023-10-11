import re 
import pymysql
from datetime import datetime

'''user_input = input("Enter a date in YYYY-MM-DD format: ")
my_date = datetime(user_input, "%Y-%m-%d").date()
print("My date:", my_date)'''
con=pymysql.connect(host="localhost",user="root",password='',database="assesment")
print("connected")

# create medicine table 
create="create table medicine (no integer auto_increment primary key, Medicinename text, Qty integer , Date  integer, Addedby integer, Price integer)"
try:
  
  cr=con.cursor()
  cr.execute(create)
  print("created...")
except Exception as e:
    print(e)
   
# add Medicine funcation 
class medicin:
   medicinename=''
   name=''
   __Qty__=''
   Date=''
   Addedby=''
   price=''

   def  medi(self):
      self.medicinename=input("Enter medicin name ")
      self.__Qty__=input("Enter qty")

      self.Date=input("Enter a date in YYYY-MM-DD format: ")
      pattern = r"\d{4}-\d{2}-\d{2}"

      self.Date1= re.match(pattern, self.Date)
      self.Addedby=input("adde by")
      self.price=input("Enter price")
      insert= f"insert into medicine (Medicinename,Qty,Date,Addedby,Price) values('{self.medicinename}',{self.__Qty__},'{self.Date}','{self.Addedby}','{self.price}')"
      try:
         cr.execute(insert)
         con.commit()
         print("Medicine Added")     
      except Exception as e:
         print(e) 

add=medicin()  
#add.medi()

# view medicine table 
class medicinview:
    
    def view(self):
        select="select * from medicine"
        cr=con.cursor()
        cr.execute(select)
        s=cr.fetchall()
        for i in s:
         print(i)

m=medicinview()
#m.view()


# delete medicine table 
class dele:
    def  delete(self):
        n=input("what do you want to delete ")
        delete=f"delete from medicine where=id{n} "
        try:
          cr.execute(delete)
          con.commit()
          print("Delete Medicine")
        except Exception as e:
          print(e)

d=dele()
#d.delete()




# create manager table     
create="create table Manager(no integer auto_increment primary key, Managername text, Phramacyname text)"
try:
  
  cr=con.cursor()
  cr.execute(create)
  print("created...")
except Exception as e:
    print(e)
   
class manager:
   def man(self):
      self.Managername=input("Enter manager name ")
      self.Phramacyname=input("Enter Phramacy name")
      insert=f"insert into Manager (Managername,Phramacyname) values ('{self.Managername}','{self.Phramacyname}')"
      try:
         cr.execute(insert)
         con.commit()
         print("manager added")
      except Exception as e:
         print(e)
a=manager()
#a.man()



# view manager table 
class managerview:
   
    def view1(self):
        select="select * from Manager"
        cr=con.cursor()
        cr.execute(select)
        s=cr.fetchall()
        for i in s:
         print(i)
m1=managerview()
#m1.view1()

create="create table Registration (no integer auto_increment primary key, firstname text, lastname text, username text, email text, password integer)"
try:
  
  cr=con.cursor()
  cr.execute(create)
  print("created...")
except Exception as e:
    print(e)

# registration 
class Registration:

    firstname=''
    lastname=''
    username=''
    email=''
    password=''

    def reg(self):
        self.firstname=''
        self.lastname=''
        self.username=''
        self.firstname=input("Enter your first name")
        self.lastname=input("Enter lastname")
        self.username=input("Enter username ")
        self.email=input("Enter your email")

        e_p="^[a-z0-9]+[@]+[a-z]+[\.]+[a-z]"
        x=re.findall(e_p,self.email)

        if x:
         self.password=input("Enter password")
         insert=f"insert into  Registration (firstname,lastname,username,email,password) values ('{self.firstname}','{self.lastname}','{self.username}','{self.email}',{self.password})"
         cr.execute(insert)
         con.commit()
         print("Registration sucessfully")
        else:
          print("invalid")
          r.reg()

r=Registration()
#r.reg()


# login 
class log:
 def loginn(self):
        
        username=input("Enter your username ")
        password=input("Enter password")
        select=f"select * from Registration  where username='{username}' and password='{password}' "
        cr=con.cursor()
        cr.execute(select)
        s=cr.fetchone()
        if s is not None :
            print("login Suceessfully")
        else:
            print("Invalid Username and Password ")
            l.loginn()
l=log()
#l.loginn()



# admin funcation 
class Admin:
    def admin(self):
        print("Admin:")
        print("\t Can Registration")
        print("\t Can Login")
        print("\t Can View All Medicine")
        print("\t Can View All Manager")
        n=input("Enter Choice")
        if n=='1':
           r.reg()
        elif n=='2':
           l.loginn()
        elif n=='3':
           print("First Of All You Have To Login After View Medicine Table ")
           l.loginn()
           print("Medicine Table ")
           m.view()
        elif n=='4':
           print("First Of All You Have To Login After Viwe Manager Table ")
           l.loginn()
           print("Manager Table ")
           m1.view1()
        else:
           exit
         
A=Admin()

# manager funcation 
class manager:
    def Manager(self):
        print("Phacarmacy Manager:")
        print("\t  Can Registration")
        print("\t  Can Login")
        print("\t  Can Add All Medicine")
        print("\t  Can View All Medicine")
        print("\t  Can Delete Medicine")
        n=input("Enter Choice ")
        if n=='1':
           r.reg()
        elif n=='2':
           l.loginn()
        elif n=='3':
           print("First Of All You Have To Login After That You Can Add Medicine ")
           l.loginn()
           print("Add Medicine Now")
           add.medi()
        elif n=='4':
           print("First Of All You Have To Login After That You Can View All Medicine ")
           l.loginn()
           print("Now You Can View All Medicine ")
           m.view()
        elif n=='5':
           print("First Of All You Have To Login After That Delete ")
           l.loginn()
           print("Now delete")
           d.delete()
        else:
           exit()       
           
M=manager()

