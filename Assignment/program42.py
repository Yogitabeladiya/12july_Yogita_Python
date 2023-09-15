
# divisor 
'''def sum_div(number):
    divisor=[1]
    for i in range(2,number):
        if (number%i)==0:
            divisor.append(i)
    return sum(divisor)
print(sum(8))
'''

def sum_div(number):
    for i in range(1,number):
        if number%i ==0:
           print(i)
    return (i)
print(sum_div(8))

