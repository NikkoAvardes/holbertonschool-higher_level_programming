#!/usr/bin/python3
"""
List all State objects containing the letter 'a' from MySQL database.

This script connects to a MySQL database and retrieves all State objects
that contain the letter 'a' in their name. Results are sorted by states.id
in ascending order and displayed in the format 'id: name'.

Usage: python3 9-model_state_filter_a.py <username> <password> <database>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1],
                sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (session.query(State).filter
              (State.name.like('%a%'))
              .order_by(State.id).all())

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
