#!/usr/bin/python3

""" The module that queries a database it is connected to using sqlalchemy"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


def add_state(username, password, database):
    """ The function that queries the database and list all columns of
        of State

        Args:
            username: The username of the user in a host
            password: The passord of the user
            database: The database to use
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")

    Session = sessionmaker(engine)

    session = Session()

    louisiana = State(name="Louisiana")

    session.add(louisiana)

    session.commit()

    result = session.query(State).filter(State.name == "Louisiana").first()

    print(result.id)


if __name__ == '__main__':
    add_state(argv[1], argv[2], argv[3])
