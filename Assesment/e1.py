import e2

print("\t   WELCOME TO PYTHON E-NOTEBOOK: \n")

print("\t   Press  1 for Generate E-NoteBook")
print("\t   Press  2 for View NoteBook")
print("\t   Press  3 for Exit\n")

Choice=input("Enter Choice")

if Choice=='1': 
  e2.y1()
  print("sucessfully enetr data")
  User=input("Enter Choice  User Add Content or exit")
  if User=='Add':
    e2.y1()
    print("Add user record sucessfully ")
  else:
    exit()
elif Choice=='2':
  e2.view()
  print("view sucessfully")
else:
  exit()

