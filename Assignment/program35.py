'''Write a Python program to combine two dictionary adding values for 
common keys. 
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400} 
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300}). '''


dict1 = {'a': 100, 'b': 200, 'c':300} 
dict2= {'a': 300, 'b': 200,'d':400} 
print(dict1.keys())
for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
    else:
        pass
         
print(dict2)


'''dict1 = {'a': 100, 'b': 200, 'c':300} 
dict2 = {'a': 300, 'b': 200,'d':400} 



c = {i: dict1.get(i, 0) + dict2.get(i, 0)

     for i in set(dict1).union(dict2)}

print(dict(c))

'''

