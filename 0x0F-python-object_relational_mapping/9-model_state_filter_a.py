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

    state_list = session.query(State).filter(State.name.like('%a%')).order_by(
                    State.id).all()
    for state in state_list:
        print("{}: {}".format(state.id, state.name))
    session.close()
