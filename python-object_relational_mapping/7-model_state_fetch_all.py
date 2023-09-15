#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <MySQL username> <MySQL password>"
              "<Database name> <State name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create a connection to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and sort by id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
