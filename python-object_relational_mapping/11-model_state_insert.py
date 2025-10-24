#!/usr/bin/python3
"""
Add a new State object "Louisiana" to MySQL database using SQLAlchemy ORM.

This script connects to a MySQL database and creates a new State object
with the name "Louisiana". After creation, it prints the new state's ID
and commits the transaction to the database.

Usage: python3 11-model_state_insert.py <username> <password> <database>
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()
