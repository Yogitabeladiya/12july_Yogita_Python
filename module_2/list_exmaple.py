city=['rajkot','amd','jamnagar','surat']
'''
print(city)
print(city[:3])
print(city[1:])
print(city[1:2])
print(city[-2])'''




'''if 'rajkot' in city:
    print("yes.....")
else:
    print("no....")
'''

'''for i in city:
    print(i) '''

'''for i in city:
   print(f"{city.index(i)} --{i}")
    '''
'''n=0
for i in city:
    print(f"{n}-{i}")
    n+=1'''

city=['rajkot','amd','jamnagar','surat']     
print(city)                                      
city.append("gondal")                            
print(city)                                    
city.insert(3,'atk')                             
print(city)                                     
city.pop()                                       
print(city)                                        
city.pop(2)                                        
print(city)                                      
city.remove('surat')                                 
print(city)                                            
city.sort()                                             
print(city)
city.reverse()
print(city)
city.clear()
print(city)
del city
print(city)



'''city=['rajkot','amd','jamnagar','surat']
newcity=city.copy()
print(newcity)
q       


city=['rajkot','amd','jamnagar','surat']
newcity=['atk','jmd','amd']

newcity.extend(city)
print(newcity)

a=city+newcity
print(a)
'''