import mysql.connector
from db_config import db_config
 
def create_conn():
    conn = None
    try:
        # Establish a connection to the database using the configuration details
        conn = mysql.connector.connect(**db_config)
        # If the connection is successful, print a success message
        if conn.is_connected():
            print('Connected to MySQL database')  # Sample output: 'Connected to MySQL database'
    except:
        print(ConnectionError)
    return conn