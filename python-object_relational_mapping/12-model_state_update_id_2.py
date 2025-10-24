#!/usr/bin/python3
"""
Update State object name in MySQL database using SQLAlchemy ORM.

This script connects to a MySQL database and changes the name of the State
object with id=2 to "New Mexico". Uses SQLAlchemy ORM for safe database
operations and commits the changes to persist them.

Usage: python3 12-model_state_update_id_2.py <username> <password> <database>
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
                sys.argv[3]), pool_pre_ping=True
    )
    new_id = 2
    new_name = "New Mexico"
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=new_id).first()
    if state:
        state.name = new_name  # type: ignore
        session.commit()
    session.close()
