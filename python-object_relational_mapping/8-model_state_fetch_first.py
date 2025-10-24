#!/usr/bin/python3
"""
Print the first State object from MySQL database using SQLAlchemy ORM.

This script connects to a MySQL database and retrieves the first State object
ordered by states.id. If the table is empty, prints "Nothing".
Uses SQLAlchemy ORM to avoid fetching all states before displaying result.

Usage: python3 8-model_state_fetch_first.py <username> <password> <database>
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

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    session.close()
