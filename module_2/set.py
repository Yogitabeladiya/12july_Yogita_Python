myset={'a','b','c','d','a'}
print(myset)
print(len(myset))
myset.add('g')
print(myset)
myset.update('i','j','k','l')
print(myset)
myset.pop()
print(myset)
myset.discard('I')
print(myset)

newset={'y','z','x','a'}
#a=myset.union(newset)
a=myset.intersection(newset)
print(a)

myset={'a','b','c','d','e'}
