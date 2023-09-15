# multiple keys in exist or not


def cheak(dict,keys):
    return all(key in dict for key in keys)
my_dict={'name':'yogi','age':12,'city':'rjk'}
keys_to=['name','age']

if cheak(my_dict,keys_to):
    print("present")
else:
    print("not present")