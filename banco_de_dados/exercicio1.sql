.tables

.schema Aluno
.schema Turma
.schema Curso

--Mostra todos os registros da tabela Aluno.
SELECT
*
from 
  Aluno;


--Exibe apenas o nome e a nota1 de todos os alunos.
SELECT
  nome as nome_aluno,
  nota1
from 
  Aluno;


--Lista todos os alunos cuja nota2 seja maior que 8.
SELECT
  nome as nome_aluno,
  nota2
from 
  Aluno
WHERE 
  nota2 > 8;


--Mostra os alunos que nasceram após o ano de 2000.
SELECT
  nome as nome_aluno,
  data_nascimento
from 
  Aluno
WHERE 
  data_nascimento >= date(2000-01-01);


--Exibe o nome e a mensalidade de todos os cursos que custam mais de 600 reais.
SELECT
  nome as nome_curso,
  mensalidade
from 
  Curso
WHERE 
  mensalidade > 600;


--Mostra o nome das turmas e o ano correspondente, ordenados pelo ano em ordem crescente.
SELECT
  nome as nome_turma,
  ano
from 
  Turma
ORDER by 
  ano ASC;


--Lista o ano das turmas e a quantidade de turmas por ano.
SELECT
  ano,
  COUNT(*) AS qtd_turmas
FROM
  Turma
GROUP BY
  ano;


--Calcula a média da nota1 dos alunos por turma_id.
SELECT
  sum(nota1)/count(nota1) as media_alunos,
  id_turma
FROM
  Aluno
GROUP by id_turma 
ORDER by media_alunos DESC;   


--Mostra o ano e a quantidade de turmas apenas para os anos que têm mais de 2 turmas.
SELECT
  count(nome) as qtd_turmas,
  ano
from 
  Turma
GROUP by ano
having qtd_turmas >2;


--Exiba o nome dos cursos e suas mensalidades, ordenando primeiro pela mensalidade (decrescente).
SELECT
  nome as nomes_cursos,
  mensalidade
from 
  Curso
ORDER by mensalidade DESC;