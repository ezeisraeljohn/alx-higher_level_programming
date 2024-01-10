#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        Args:
            attrs (list, optional): List of attribute names to include.
                If None, include all attributes.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in
                attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
