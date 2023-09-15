# Write a Python program to create a dictionary from a string. 

def dict(string):
  dict={}
  for char in string:
    if char in dict:
      dict[char]+=1
    else:
      dict[char]=1
  return dict
print(dict('w3resource'))


