#!/usr/bin/python3
"""
City model module for SQLAlchemy ORM.

This module defines the City class that represents a city in the database.
City objects are linked to State objects through a foreign key relationship.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that represents a city in the database.

    Attributes:
        id (int): Auto-generated unique primary key
        name (str): City name, max 128 characters
        state_id (int): Foreign key reference to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)

    name = Column(String(128),
                  nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
