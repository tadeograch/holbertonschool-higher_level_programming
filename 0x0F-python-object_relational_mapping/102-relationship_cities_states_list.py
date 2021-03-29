#!/usr/bin/python3
"""lists all State objects, and corresponding City objects"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    for s in session.query(State).order_by(State.id):
        for c in s.cities:
            print("{}: {} -> {}".format(c.id, c.name, s.name))
    session.close()
