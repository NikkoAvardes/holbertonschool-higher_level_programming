#!/usr/bin/python3
"""
Print State object ID by name from MySQL database using SQLAlchemy ORM.

This script connects to a MySQL database and searches for a State object
with the specified name. If found, prints the state ID. If not found,
prints "Not found". SQL injection safe using SQLAlchemy ORM queries.

Usage:
    python3 10-model_state_my_get.py <username> <password> <db> <state_name>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    states_names = sys.argv[4]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1],
                sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == states_names).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    session.close()
