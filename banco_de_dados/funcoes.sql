.tables

.schema Aluno
.schema Turma
.schema Curso

-- 1- COUNT: Mostre quantos alunos estão cadastrados na tabela Aluno.
SELECT COUNT(*) AS total_alunos FROM Aluno;

-- 2- MIN: Mostre a menor mensalidade entre todos os cursos cadastrados.
SELECT MIN(mensalidade) AS menor_mensalidade FROM Curso;

-- 3- MAX: Mostre a maior nota1 registrada entre todos os alunos.
SELECT MAX(nota1) AS maior_nota1 FROM Aluno;

-- 4- SUM: Calcule o valor total das mensalidades de todos os cursos.
SELECT SUM(mensalidade) AS total_mensalidades FROM Curso;

-- 5- AVG: Mostre a média geral da nota2 dos alunos.
SELECT AVG(nota2) AS media_nota2 FROM Aluno;