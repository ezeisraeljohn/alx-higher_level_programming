#!/usr/bin/python3

""" The Documentation for this module """

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create the declarative base instance
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Define the MySQL connection string
MYSQL_USER = 'ezeisraeljohn'
MYSQL_PASSWORD = '@israelEze12'
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DB = 'mydatabase'

DB_URI = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'

# Create the engine
engine = create_engine(DB_URI)

# WARNING: Import all classes before calling Base.metadata.create_all(engine)

if __name__ == "__main__":
    # Create the tables in the database
    Base.metadata.create_all(engine)
