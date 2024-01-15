#!/usr/bin/python3

"""The square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ The Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size

    def update(self, *args, **kwargs):
        """ Updating attributes methods

        Args:
            args(int): The integer arguements to update attribute with

        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for attr, value in zip(attrs, args):
                if hasattr(self, attr):
                    setattr(self, attr, value)

        else:
            for attr, value in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, value)

    def to_dictionary(self):
        """ Return the dictionary of an instance"""
        attrs = ['id', 'size', 'x', 'y']
        return {attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)}
