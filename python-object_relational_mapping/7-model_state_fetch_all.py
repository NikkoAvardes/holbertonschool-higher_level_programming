#!/usr/bin/python3
"""
List all State objects from MySQL database using SQLAlchemy ORM.

This script connects to a MySQL database and retrieves all State objects
sorted by their id in ascending order. Uses SQLAlchemy ORM for database
operations instead of raw SQL queries.

Usage: python3 7-model_state_fetch_all.py <username> <password> <database>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """Connect to MySQL database and display State objects ordered by id."""
    user_name = sys.argv[1]
    user_passwd = sys.argv[2]
    data_base = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user_name, user_passwd, data_base),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    main()
