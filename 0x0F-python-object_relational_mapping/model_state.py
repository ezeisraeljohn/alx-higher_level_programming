#!/usr/bin/python3

""" Module that demonstrate the sqlalchemy """


from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)


engine = create_engine('mysql+mysqldb://localhost:3306', pool_pre_ping=True)
