#1
lista_quadrados = [x**2 for x in range(1,21)]
print(lista_quadrados)

#2
lista_pares = [x for x in range(0,50) if x%2==0]
print(lista_pares)

#3
palavra = "comprehension"
vogais = ["a","e","i","o","u"]
lista_vogais = [letra for letra in palavra if letra in vogais]
print(lista_vogais)

#4
multiplos_de_3 = [num for num in range(0, 31) if num%3==0]
print(multiplos_de_3)

#5
lista_tuplas = [(n, n**2) for n in range(1,11)]
print(lista_tuplas)

