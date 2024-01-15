#!/usr/bin/python3

""" The Rectangle Module"""


from models.base import Base


class Rectangle(Base):
    """ The Rectangle Class

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
            x(int): The x coordinate of the rectangle
            y(int): The y coordinate of the rectangle

        methods:
            update: This function overwrite the already existing attribute
            dictionary: That returns the dictionary of an instance

        Raises:
            TypeError: This is raised when any of the attribute is not integer
            ValueError: Raised when x or y is less than zero or weight or
                        height is less than or equal to zero
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializer method """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ The width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ The height getter"""
        return self.__height

    @width.setter
    def height(self, value):
        """ The height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ The x gettter """
        return self.__x

    @x.setter
    def x(self, value):
        """ The x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ The y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """ The y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Area that calculates the area of Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Function that prints area of the rectangle with Hashes"""
        if self.__width and self.__height and self.__x and self.__y == 0:
            print(end="")

        for i in range(self.__y):
            print()

        for _ in range(self.__height):
            for _ in range(self.__width):
                for _ in range(self.__x):
                    print(" ", end="")
                print("#", end="")
            print()

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """ Updating attributes methods

        Args:
            args(int): The integer arguements to update attribute with

        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attrs, args):
                if hasattr(self, attr):
                    setattr(self, attr, value)

        else:
            for attr, value in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, value)

    def to_dictionary(self):
        """ Return the dictionary of an instance"""
        dic = {}
