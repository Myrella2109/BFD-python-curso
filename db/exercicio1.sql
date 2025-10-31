.tables

.schema Aluno
.schema Turma
.schema Curso


SELECT
*
from 
  Aluno;


SELECT
  nome as nome_aluno,
  nota1
from 
  Aluno;


SELECT
  nome as nome_aluno,
  nota2
from 
  Aluno
WHERE 
  nota2 > 8;


SELECT
  nome as nome_aluno,
  data_nascimento
from 
  Aluno
WHERE 
  data_nascimento >= date(2000-01-01);


SELECT
  nome as nome_curso,
  mensalidade
from 
  Curso
WHERE 
  mensalidade > 600;


SELECT
  nome as nome_turma,
  ano
from 
  Turma
ORDER by 
  ano ASC;



SELECT
  ano,
  COUNT(*) AS qtd_turmas
FROM
  Turma
GROUP BY
  ano;



SELECT
  sum(nota1)/count(nota1) as media_alunos,
  id_turma
FROM
  Aluno
GROUP by id_turma 
ORDER by media_alunos DESC;   



SELECT
  count(nome) as qtd_turmas,
  ano
from 
  Turma
GROUP by ano
having qtd_turmas >2;


SELECT
  nome as nomes_cursos,
  mensalidade
from 
  Curso
ORDER by mensalidade DESC;