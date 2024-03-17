#!/usr/bin/python3

""" Module that demonstrate the sqlalchemy """


from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """ Defines the table to be linked to the class """
    __tablename__ = 'states'

    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True,
        unique=True
        )
    name = Column(String(128), nullable=False)
