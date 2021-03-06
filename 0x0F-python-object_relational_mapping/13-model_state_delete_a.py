#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(State).filter(State.name.like('%a%')):
        session.delete(city)
    session.commit()
    session.close()
