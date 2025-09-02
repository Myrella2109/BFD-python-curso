#exercicío 1-Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", 
# e preencha com valores fictícios.
print("Exercicío 1-")
aluno = { "Nome": "Carla", "Idade": 17, "Nota": 9}
print(aluno)

#exercicío 2- Dado o dicionário:
#produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
#Imprima o nome do produto e a quantidade em estoque.
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
print("\nExercicío 2-")
print("Nome do produto:", produto["nome"])
print("Quantidade em estoque:", produto["estoque"])

#exercicío 3-Dado o dicionário:
#pessoa = {"nome": "Carlos", "idade": 30}
#Adicione uma nova chave "cidade" com valor "São Paulo".
pessoa = {"Nome": "Carlos", "Idade": 30}
pessoa["Cidade"] = "São Paulo"
print("\nExercicío 3-")
print(pessoa)

#exercicío 4-Dado o dicionário:
#carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
#Remova a chave "ano" do dicionário.
carro = {"Marca": "Ford", "Modelo": "Fiesta", "Ano": 2010}
del carro["Ano"]
print("\nExercicío 4-")
print(carro)

#exercicío 5-Verifique se a chave "telefone" existe no dicionário:
#contato = {"nome": "Ana", "email": "ana@email.com"}
print("\nExercicío 5-")
contato = {"Nome": "Ana", "Email": "ana@email.com"}
if "Telefone" in contato:
    print("Telefone do contato:", contato["Telefone"])
else:
    print("Telefone não existente.")

#exercicío 6-Escreva uma função que receba uma lista de palavras e 
# retorne um dicionário com a contagem de cada palavra.
#palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
def contar_palavras(lista_palavras):
    contagem = {}
    for palavra in lista_palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem
palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
resultado = contar_palavras(palavras)
print("\nExercicío 6-")
print(resultado)

#exerciío 7-Dado o dicionário:
#d = {"a": 1, "b": 2, "c": 3}
#Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.
d = {"a": 1, "b": 2, "c": 3}
d_in = {}
for chave, valor in d.items():
    d_in[valor] = chave
print("\nExercicío 7-")
print(d_in)

#exerciío 8-Crie um dicionário onde cada chave é o nome de um aluno e 
# o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.
notas = {
    "Ana": [8, 7, 9],
    "Julia": [6, 7, 8],
    "Carla": [9, 8, 10]
}
print("\nExercicío 8-")
print("Médias dos alunos ->")
for aluno, notas in notas.items():
    media = sum(notas) / len(notas)
    print(f"Média de {aluno}: {media:.2f}")

#exrcicío 9-Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor.
#Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor.
def mesclar_dicionarios(d1, d2):
    resultado = d1.copy() 
    resultado.update(d2)   
    return resultado

livros_1 = {"Harry Potter": "ler", "Sangue e fogo": "lido", "A Bússola de Ouro": "ler"}
livros_2 = {"Harry Potter": "lido", "A Bússola de Ouro": "lido", "A Maldição do Tigre": "ler", "O grande livro das runas": "ler"}

livros_3 = mesclar_dicionarios(livros_1, livros_2)
print("\nExercicío 9-")
print(livros_1)
print(livros_3)

#exercicío 10- Dado o dicionário:
#pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
#Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
print("\nExercicío 10-")
ordem_ma_me = sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True)
for nome, pontuacao in ordem_ma_me:
    print(f"{nome}: {pontuacao}")
