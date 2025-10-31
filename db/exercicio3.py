import sqlite3

conn = sqlite3.connect("escola_v2.db")
cursor = conn.cursor()

cursor.execute("SELECT* FROM Aluno")

query_result =cursor.fetchall()

print(query_result)

conn.close()


cursor.execute(
    "SELECT nome,(nota1+nota2)/2 as media_alunos  from Aluno order by media_alunos desc limit 10;"
)
query_result = cursor.fetchall()

print(query_result)

conn.close()


cursor.execute(
    "SELECT * from Aluno left join Turma on Aluno.id_Turma = Turma.id;"
)
query_result = cursor.fetchall()

print(query_result)

conn.close()

cursor.execute(
    "SELECT * from Aluno left join Turma on Aluno.id_Turma = Turma.id where Turma.id = 2;"
)
query_result = cursor.fetchall()

print(query_result)

conn.close()