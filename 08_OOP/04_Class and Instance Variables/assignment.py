class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        if(base < 0):
            self.__base = 0
        else:
            self.__base = base
            self.__height = height
        
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self) -> float:
        return self.__base
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return self.__base * self.__height
 

rectangle1 = Rectangle(3, 4)
print("The base of Rectangle1 is", rectangle1.get_base())
print("The height of Rectangle1 is", rectangle1.get_height())
print("The perimeter of Rectangle1 is", rectangle1.get_perimeter())
print("The area of Rectangle1 is", rectangle1.get_area())


rectangle2 =  Rectangle(6, 4)
print("The base of Rectangle2 is", rectangle2.get_base())
print("The height of Rectangle2 is", rectangle2.get_height())
print("The perimeter of Rectangle2 is", rectangle2.get_perimeter())
print("The area of Rectangle2 is", rectangle2.get_area())