#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    s = State(name="California")
    c = City(name="San Francisco")
    s.cities.append(c)
    session.add(s)
    session.add(c)
    session.commit()
    session.close()
