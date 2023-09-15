# removw empy tuple from tuple 

'''def Remove(tuples):
	for i in tuples:
		if(len(i) == 0):
			tuples.remove(i)
	return tuples
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
		('krishna', 'akbar', '45'), ('', ''), ()]
print(Remove(tuples))
'''



'''def remove(tuples):
    for i in tuples:
        if (len (i)== 0):
              tuples.remove(i)
    return tuples
tuples=[(),(2,1,34,5),(),(4,5),()]
print(remove(tuples))
'''


def remove(tuples):
     for i in tuples:
          if (len(i)==0):
               tuples.remove(i)
     return tuples
tuples=[(),(2,3,4),(),(4,5),()]
print(remove(tuples))
