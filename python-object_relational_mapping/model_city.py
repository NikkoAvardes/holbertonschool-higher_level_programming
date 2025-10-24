#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)

    name = Column(String(128),
                  nullable=False)

    state_id = Column(Integer, ForeignKey('state.id'), nullable=False,)
