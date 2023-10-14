# raise odd 

while True:
    try:
        num = int(input("Enter an odd number: "))
        if num % 2 == 0:
            raise ValueError("You entered an even number!")
        break
    except ValueError as e:
        print(e)