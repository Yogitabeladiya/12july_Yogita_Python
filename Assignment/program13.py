'''Write a Python class named Circle constructed by a radius and two 
methods which will compute the area and the perimeter of a circle'''


class circle:
    def __init__(self,radius) :
        self.radius=radius  

    def area(self):
        return self.radius ** 2 * 3.14
    
    
    def pera(self):
        return 2* self.radius * 3.14
    

c=circle(8)
print(c.area())
print(c.pera())       



