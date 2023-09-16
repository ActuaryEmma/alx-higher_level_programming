#!/usr/bin/python3
"""python file that contains the class definition of a State"""
from sqlalchemy import create_engine
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # create a sesssion
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    state = session.query(State).filter(State.name == sys.argv[4]).order_by(
            State.id).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
