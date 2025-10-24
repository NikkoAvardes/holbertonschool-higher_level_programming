#!/usr/bin/python3
"""
Delete all State objects containing the letter 'a' from MySQL database.

This script connects to a MySQL database and deletes all State objects
that contain the letter 'a' in their name. Uses SQLAlchemy ORM for safe
database operations and commits the changes to persist them.

Usage: python3 13-model_state_delete_a.py <username> <password> <database>
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

    states_delete = (session.query(State)
                     .filter(State.name.like('%a%'))
                     .order_by(State.id)
                     .all())

    for state in states_delete:
        session.delete(state)
    session.commit()
    session.close()
