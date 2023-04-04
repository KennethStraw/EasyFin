import sqlite3
from os.path import isfile, getsize

# Try open DB
def openDB(username):
    dbFilename = f'{username}_finances'
    try:
        if not isfile(dbFilename):
            return False
    except sqlite3.Error:
        print("Error open db.\n")
        return False
    return True

# Create/Connect to finances.db
def createDB(username):
    try :
        conn = sqlite3.connect(f'{username}_finances.db')
        # Create cursor
        c = conn.cursor()
        # Create table
        c.execute("""CREATE TABLE costs (
            cost integer,
            spenddate integer,
            category text
        )
        """)
        return True
    except :
        return False;
