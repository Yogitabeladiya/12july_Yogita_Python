dict={'id':1,'name':'yogita','city':'rajkot'}

print(dict)
print(dict['id'])
print(dict['name'])
print(dict.get('name'))
print(len(dict))
print(dict.keys())
print(dict.values())
dict.pop('id')
del dict['name']
dict['id']=2
dict['city']='rajkot'
dict.clear()
print(dict)

ndict=dict.copy()
print(ndict)

'''if 'name' in dict:
    print("yes ...")
else:
    print("nooo")

'''

'''for i in dict:
    print(i)

for i in dict.values():
    print(i)

for i in dict.items():
   print(i)

if 'yogita' in dict.values():
    print("yes")
else:
    print("nooo")

if 'id' in dict.keys():
    print("ys")
else:
    print("noo")'''