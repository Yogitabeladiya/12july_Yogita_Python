a=34  #global 
b=60

def production():
    global a,b
    a=34
    b=12
    print("mal",a*b)

print("sum",a+b)
production()