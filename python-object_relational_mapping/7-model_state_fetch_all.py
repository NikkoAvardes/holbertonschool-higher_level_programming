#!/usr/bin/python3
# Liste tous les objets State avec SQLAlchemy triés par states.id
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":

    user_name = sys.argv[1]
    user_passwd = sys.argv[2]
    data_base = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user_name, user_passwd, data_base),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")
    finally:
        session.close()
