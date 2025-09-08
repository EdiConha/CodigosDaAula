#1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela

livros = ["Aprendendo Python", "A interpretação dos sonhos", "Admirável mundo novo"]

print(livros)

#2

print(f" O primeiro elemento: {livros[0]}")
print(f" O ultimo elemento: {livros[len(livros)-1]}")

#3

livros.append("O guia do mochileiro das galáxias")
livros.append("Waking life")
print(f" Lista atualizada: {livros}")

#4

livros.insert(1, "Duna")
print(livros)

#5

if "Silêncio dos inocentes" in livros:
	livros.remove("Silêncio dos inocentes")
else:
	print("Livro não encontrado")


#6

numeros = [1, 2, 3, 2, 4, 2, 5]
print(f"O número 2 aparece {numeros.count(2)} vezes na lista.")

#7

for item in livros:
	print(f"O livro {item} é interessante")


#8

lista_idades = [12, 18, 25, 14, 30]
for idade in lista_idades:
	if idade >= 18:
		print(idade)
		
#9

lista_valores = [10, 20, 30, 40]
soma = 0
for val in lista_valores:
	soma += val

print(soma)

#10

aluno_1_notas = []
aluno_2_notas = []
notas = []

nota1, nota2, nota3 = input("Digite as notas do aluno 1: ").split()
aluno_1_notas.append(float(nota1))
aluno_1_notas.append(float(nota2))
aluno_1_notas.append(float(nota3))

nota4, nota5, nota6 = input("Digite as notas do aluno 2: ").split()
aluno_2_notas.append(float(nota4))
aluno_2_notas.append(float(nota5))
aluno_2_notas.append(float(nota6))

notas.append(aluno_1_notas)
notas.append(aluno_2_notas)

media_aluno1 = (aluno_1_notas[0]+aluno_1_notas[1]+aluno_1_notas[2])/3
media_aluno2 = (aluno_2_notas[0]+aluno_2_notas[1]+aluno_2_notas[2])/3

print(notas)
print(f"A média do aluno 1: {media_aluno1:.2f}")
print(f"A média do aluno 2: {media_aluno2:.2f}")