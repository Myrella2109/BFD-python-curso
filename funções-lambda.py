from functools import reduce
print("Exercicío 1-")
lista = [1,2,3,4,5]
print(list(map(lambda num: num*2, lista)))


print("\nExercicío 2-")
idade = [10, 15, 20, 25, 30]
print(list(filter(lambda num: num % 2 == 0, idade)))


print("\nExercicío 3-")
num = [1,2,3,4,5]
print(reduce(lambda x, y: x + y, num))


print("\nExercicío 4-")
frutas = ["uva", "banana", "maçã", "laranja"]
print(sorted(frutas, key=lambda x: len(x)))


print("\nExercicío 5-")
nom = ["ana", "pedro", "maria"]
print(list(map(lambda x: x.capitalize(), nom)))

print("\nExercicío 6-")
nume = [1,2,3,4,5]
print(reduce(lambda x, y: x*y, nume))


print("\nExercicío 7-")
frut = ["uva", "banana", "maçã", "laranja"]
print(sorted(frut, key=lambda x: x[-1]))
