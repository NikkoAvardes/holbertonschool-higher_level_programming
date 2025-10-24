#!/usr/bin/python3
"""
Print all City objects grouped by state from MySQL database using SQLAlchemy.

This script connects to a MySQL database and retrieves all City objects
along with their associated State information. Results are sorted by
cities.id and displayed in the format 'state_name: (city_id) city_name'.

Usage: python3 14-model_city_fetch_by_state.py <username> <password> <database>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1],
                sys.argv[2],
                sys.argv[3]), pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).filter(
        City.state_id == State.id
    ).order_by(City.id).all()
    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
