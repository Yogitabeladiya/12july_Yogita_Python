'''tup=('ios','android','python','java')
print(tup)
print(tup[:2])
print(tup[1:3])
print(tup[-3])
print(len(tup))
print(tup.count('ios'))
print(tup.index('ios'))
'''

'''
tup=('ios','android','python','java')

if 'ios'in tup:
    print("yes,....")
else:
    print("no....")'''


'''for i in tup:
  print(i)'''

'''for i in tup:
    print(f"{tup.index(i)} -{i}")

'''
tup=[]
n=int(input("enter input number"))

for i in range(n):
    x=input("enter tuple")
    tup.append(x)
print(tuple(tup))
