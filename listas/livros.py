#exercicío 1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
livros = ['It a Coisa', 'A Arte da Guerra', 'A Maldição do Tigre', 'Harry Potter']
print("Exercicío 1-")
print(livros)

#exercicío 2- Usando a lista livros, exiba apenas o primeiro e o último elemento.
print("\nExercicío 2-")
print(livros[0])
print(livros[2])

#exercicío 3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
livros.append('A Bússola de Ouro')
livros.append('O Chamado de Cthulhu')
print("\nExercicío 3-")
print(livros)

#exercicío 4-Insira o livro "Duna" na segunda posição da lista livros usando insert().
livros.insert(2, 'Duna')
print("\nExercicío 4-")
print(livros)

#exercicío 5-Remova o livro "Silêncio dos inocentes" da lista usando remove(). 
# Se ele não existir, exiba a mensagem "Livro não encontrado".
print("\nExercicío 5-")
if 'Silêncio dos inocentes' in livros:
    livros.remove('Silêncio dos inocentes')
else:
    print('Livro não encontrado.')
#exercicío 7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"
print("\nExercicío 7-")
for livro in livros:
  print(livro,'é muito interessante')


