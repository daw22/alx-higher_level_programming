#!/usr/bin/python3
"""
contains the class definition of a State and
an instance Base = declarative_base()
"""


from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """
    states model
    -links to the City table
    """
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)
    cities = relationship('City', cascade='delete, save-update, merge', backref='State')
