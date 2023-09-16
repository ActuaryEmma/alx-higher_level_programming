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

    state_list = State(name="Louisiana")
    session.add(state_list)
    session.commit()
    print("{}".format(state_list.id))
    session.close()
