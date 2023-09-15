# Python code to check if two lists

'''set1 ={1, 3, 4, 55}
list2 = {2, 3, 90, 22}

i=set1.intersection(list2)
print(list(i))
if i:
	print("True")
else :
	print("False")

'''
list1 =[1, 3, 4, 55]
list2 = [2, 3, 90, 22]

out = set(list1) & set(list2)
print(out)

if out:
   print("true")
else :
	print("False")


