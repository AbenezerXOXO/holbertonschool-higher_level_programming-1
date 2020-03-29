#!/usr/bin/python3
""" a script that all State objects, and corresponding City objects
from the database hbtn_0e_100_usa """
import sys
from relationship_state import Base, State, City
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def main(argv):
    """ main function """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for st in session.query(State).order_by(asc(State.id)):
        print("{}: {}".format(st.id, st.name))
        for c in st.cities:
            print("\t{}: {}".format(c.id, c.name))
    session.close()


if __name__ == '__main__' and len(sys.argv) == 4:
    main(sys.argv)
