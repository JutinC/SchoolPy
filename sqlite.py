"""
Justin Choi
IDT Period 3
January, 19 2023
Sqlite link
"""

import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()
cur.execute("CREATE TABLE potata(ID, Name, Age)")
cur.execute()
