import sqlite3
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
db_path = os.path.join(parent_dir, "single_table.db")


conn = sqlite3.connect(db_path)
cur = conn.cursor()

query = "CREATE TABLE items(\
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,\
    item_name STRING,\
    price INTEGER)"

cur.execute(query)
conn.commit()
conn.close()
