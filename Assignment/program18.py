# replce last value in list

tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 0
new_list = [t[:-1] + (new_value,) for t in tuples_list]
print(new_list)

'''t=[28,(1,2,3,4),(5,6,7,8),(9,10)]
print(t)
print(len(t))
t[0],t[-1]=t[-1],t[0]
print(t)
'''