#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <MySQL username> <MySQL password> <Database name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Establish a connection to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Create a cursor object
        cur = db.cursor()

        # Execute the SQL query to retrieve states
        cur.execute("SELECT * FROM states ORDER BY states.id")

        # Fetch and display the results
        results = cur.fetchall()
        for row in results:
            print(row)

        # Close the cursor and the database connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)
