import e2

print("\t   WELCOME TO PYTHON E-NOTEBOOK: \n")

print("\t   Press  1 for Generate E-NoteBook")
print("\t   Press  2 for View NoteBook")
print("\t   Press  3 for Exit\n")

Choice=input("Enter Choice....")

if Choice=='1': 
  e2.y1()
  e2.y2()
  e2.y3()
  print(" Enter sucessfully.......")
  n=input("if user add new data Yes or no ....")
  if n=='yes':
     e2.y5()
  else:
     print("No...")
elif Choice=='2':
    e2.view()
    print("view sucessfully........")
else:
  exit()

