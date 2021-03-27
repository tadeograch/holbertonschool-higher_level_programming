#!/usr/bin/python3
"""
lists all State objects that contain the letter a from database hbtn_0e_6_usa
"""
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
        print("{}: {}".format(city.id, city.name))
    session.close()
