import sqlite3
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
db_path = os.path.join(parent_dir, "single_table.db")


conn = sqlite3.connect(db_path)
cur = conn.cursor()

query = "SELECT * FROM items"
# 取得するだけでデータベースは変わらない

cur.execute(query)
print(cur.fetchall())
conn.commit()
conn.close()
