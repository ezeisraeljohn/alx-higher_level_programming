#!/usr/bin/python3

""" The module that queries a database it is connected to using sqlalchemy"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


def list_all_states(username, password, database):
    """ The function that queries the database and list all columns of
        of State
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")

    Session = sessionmaker(engine)

    session = Session()

    states_ordered_by_id = session.query(State).order_by(State.id).all()

    for state in states_ordered_by_id:
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    list_all_states(argv[1], argv[2], argv[3])
