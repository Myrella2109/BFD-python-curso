#exercicío 6-Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.
numeros = [1, 2, 3, 2, 4, 2, 5]
repeticoes = numeros.count(2)
print("Exercicío 6-")
print(f"O número 2 aparece {repeticoes} vezes na lista")

#exercicío 8-Dada a lista idades = [12, 18, 25, 14, 30], 
# use um laço para exibir somente as idades maiores ou iguais a 18.
print("\nExercicío 8-")
idades = [12, 18, 25, 14, 30]
for idade in idades:
    if idade >= 18:
     print(idade)

#exercicío 9-Crie uma lista valores = [10, 20, 30, 40]. 
# Use um laço for para calcular manualmente a soma de todos os valores.
print("\nExercicío 9-")
valores = [10, 20, 30, 40]
soma = 0
for numeros in valores:
   soma += numeros
   print(f'O resultado da soma é:',soma)

#exercicío 10-Use input para receber 3 notas de dois alunos. 
# As notas de cada aluno precisam ser armazenadas em uma lista separada 
# que deve ser armazenada dentro de outra lista chamada notas. No fim, imprima a média de cada aluno.
print("\nExercicío 10-")
notas = []

for i in range(2):
    notas_aluno = []
    print(f"    Aluno {i+1}   ")
    for j in range(3):
        while True:
            try:
                nota = float(input(f"Digite a {j+1}ª nota: "))
                notas_aluno.append(nota)
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            
    notas.append(notas_aluno)

print("\nMédias dos alunos:")
for i, aluno_notas in enumerate(notas):
    media = sum(aluno_notas) / len(aluno_notas)
    print(f"Média do Aluno {i+1}: {media:.2f}")