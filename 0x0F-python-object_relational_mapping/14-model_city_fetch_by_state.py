#!/usr/bin/python3

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    sid = State.id
    csid = City.state_id
    f = session.query(City, State).filter(sid == csid).order_by(City.id)
    for c, s in f:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
