#Write a Python program to unzip a list of tuples into individual lists.

l = [(1,2), (3,4), (8,9)]

# unzip the list of tuples
a, b = zip(*l)

# print the individual lists
print(a) # (1, 3, 8)
print(b) # (2, 4, 9)