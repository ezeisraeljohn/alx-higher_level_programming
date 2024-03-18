#!/usr/bin/python3

""" The module that queries a database it is connected to using sqlalchemy"""

from model_city import Base, City
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


def list_all_states_city(username, password, database):
    """ The function that queries the database and list all columns of
        of State
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)

    session = Session()

    city_ordered_by_id = session.query(State, City)\
        .join(City, State.id == City.state_id).all()

    for city in city_ordered_by_id:
        print(f"{city[0].name}: ({city[1].id}) {city[1].name}")


if __name__ == '__main__':
    list_all_states_city(argv[1], argv[2], argv[3])
