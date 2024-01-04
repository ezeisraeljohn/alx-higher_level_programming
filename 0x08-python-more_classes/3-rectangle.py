#!/usr/bin/python3

"""The Module that defines the Rectangle class

    Addition:
        Returns the perimeter of the Rectangle
        Returns the Area of the Rectangle
"""


class Rectangle():
    """The class that serves as a blue print for Rectangle objects

        Attributes:
            width(int): The width of the rectangle
            height(int): The height of the rectangle

        Methods:
            set_width(width:int)->None:
                Set the width of the Rectangle

            get_width()->int:
                This returns the width of the Rectangle

            set_height(height:int)->None:
                This sets the height of the Rectangle

            get_height()->int:
                This returns the height of the Rectangle
            perimeter()->int:
                This returns the perimeter of the Rectangle
            area()->int:
                Returns the area of the Rectangle

    """

    def __init__(self, width=0, height=0) -> None:
        """The Function that initializes the attribute of the class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Gets the width

            Returns: Returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width"""
        self.__width = value
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """ Gets the height

            Returns: Returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height """
        self.__height = value

        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")

        if self.__height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Function that calculates and returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Method that calculates and returns the perimeter of the rectangle"""
        return 2*self.__width + 2*self.__height

    def __str__(self) -> str:
        "Function that makes use of the string method"
        if self.__width == 0 and self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if i != self.__height - 1:
                print()
        return ""
