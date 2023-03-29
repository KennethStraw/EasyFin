import sqlite3

# Create/Connect to finances.db
conn = sqlite3.connect('finances.db')
# Create cursor
c = conn.cursor()
# Create table
c.execute("""CREATE TABLE costs (
    cost integer,
    spenddate integer,
    category text
)
""")