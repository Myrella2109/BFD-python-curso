import sqlite3

# 1 - Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db
conn = sqlite3.connect('escola_v2.db')
cursor = conn.cursor()

# 2 - Faça a query para pegar toda a tabela alunos e imprima na tela.
cursor.execute("SELECT * FROM aluno")
alunos = cursor.fetchall()
print("Tabela Alunos:")
for aluno in alunos:
    print(aluno)

# 3 - Obtenha a media entre nota1 e nota2 dos alunos, ordene em ordem decrescente e retorne apenas os 10 maiores notas. No fim imprima na tela a lista desses alunos e suas médias.
cursor.execute("""
    SELECT nome, (nota1 + nota2) / 2.0 AS media
    FROM aluno
    ORDER BY media DESC
    LIMIT 10
""")
top_alunos = cursor.fetchall()
print("\nTop 10 alunos por média (nota1 + nota2)/2, em ordem decrescente:")
for aluno in top_alunos:
    print(f"Nome: {aluno[0]}, Média: {aluno[1]:.2f}")

# 4 - Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.
cursor.execute("""
    SELECT *
    FROM aluno
    LEFT JOIN turma ON aluno.id_turma = turma.id
""")
alunos_turmas = cursor.fetchall()
print("\nLeft Join entre Aluno e Turma:")
for row in alunos_turmas:
    print(row)

# 5 - Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela.
cursor.execute("""
    SELECT *
    FROM aluno
    LEFT JOIN turma ON aluno.id_turma = turma.id
    WHERE turma.id = 2
""")
alunos_turma_2 = cursor.fetchall()
print("\nAlunos da turma 2 (Left Join com filtro):")
for row in alunos_turma_2:
    print(row)


conn.close()
