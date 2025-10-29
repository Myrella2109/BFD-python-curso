import sqlite3
from pathlib import Path

db_connection = sqlite3.connect('db/escola_v2.db')

cursor = db_connection.cursor()
cursor.execute("""SELECT* FROM Aluno""")

query_result =  cursor.fetchall()
print(query_result)

