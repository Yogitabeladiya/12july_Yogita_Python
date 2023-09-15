#map two list in dictionary
values=['yogita','rinkal','yogi']
keys=[1,2,3]
print(str(keys))
print(str(values))

d={}
for key in keys:
    for value in values:
        d[key]=value
        values.remove(value)
        break
print(str(d))


name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
 
mapped = zip(name, roll_no)
 
print(dict(mapped))