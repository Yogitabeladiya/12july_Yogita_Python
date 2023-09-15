# write a python program smallest number in list


'''def small():
    
 list=[1,2,3,4,5,6,7]
 print(min(list))
small()'''

def smallest():
    list=[4,8,2,3,5]
    min=list[0]
    for x in list:
        if x<min: 
            min=x   
    return min
print(smallest())





