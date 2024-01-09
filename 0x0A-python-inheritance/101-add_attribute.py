#!/usr/bin/python3
""" Documentation for the module """
def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute should be added.
        attr_name (str): The name of the attribute.
        attr_value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, '__dict__') or (hasattr(obj, '__slots__')
                                    and attr_name in obj.__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
