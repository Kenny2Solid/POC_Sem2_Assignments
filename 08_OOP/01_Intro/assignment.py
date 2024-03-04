<<<<<<< HEAD
import math

class RightTriangle2:
=======
class RightTriangle:
>>>>>>> 9b7eb6846b03f7624879ecb73734bd880ac3d82f
    def __init__(self, base, height):
        self.base = base
        #YOUDO:  do the same for height
    
    def area(self):
<<<<<<< HEAD
       return (1/2 ) * self.base * self.height
    
    def hypotenuse(self):
        return math.hypot(self.height * self.base)
    
    def perimeter(self):
        return self.base + self.height + self.hypotenuse
    
class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
       return (1/2 ) * self.base * self.height
    
    def hypotenuse(self):
        return math.hypot(self.height * self.base)
    
    def perimeter(self):
        return self.base + self.height + self.hypotenuse



tri1 = RightTriangle(3, 4)
print("The base of tri1 is", tri1.base)
print("The height of tri1 is", tri1.height)
print("The area of tri1 is", tri1.area())


tri1l= RightTriangle2(5, 10)
print("The base of tri1 is", tri1.base)
print("The height of tri1 is", tri1.height)
print("The area of tri1 is", tri1.area())
=======
        #Youdo return the area which is 1/2 * base * height
        pass #Remove this pass when finished
>>>>>>> 9b7eb6846b03f7624879ecb73734bd880ac3d82f

triangle1 = RightTriangle(3, 4)
print("The area of triangle1 is", triangle1.area())

#YOUDO: make another rightTriangle called triangle2
#YOUDO:  and print its area.  

