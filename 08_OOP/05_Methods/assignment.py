class Rectangle:

    def __init__(self, base: float, height: float) -> None:
        if (base < 0):
            self.__base = 0
        else:
            self.__base = base

        if (height < 0):
            self.__height = 0
        else:
            self.__height = height

    def get_height(self) -> float:
        return self.__height
    
    def get_base(self) -> float:
        return self.__base


    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height

      def get_area(self) -> float:
        return self.__base * self.__height
    
    def __str__(self) -> str:
        # Rectangle of base:3, height:4
        return "Rectangle of base:" + self.__base + ", height:" + self.__height
        


