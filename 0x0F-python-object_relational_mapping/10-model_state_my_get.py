#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    ins = session.query(State).filter(State.name == sys.argv[4]).first()
    if not ins:
        print("Not found")
    else:
        print("{}".format(ins.id))
    session.close()
