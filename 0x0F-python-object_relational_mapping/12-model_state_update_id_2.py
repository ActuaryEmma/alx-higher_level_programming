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

    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()
    else:
        print("Not found")
    session.close()
