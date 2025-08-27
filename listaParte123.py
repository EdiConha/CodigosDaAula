#Aluno:Edielson Miranda Diniz
#BOLSA FUTURO DIGITAL
#Atividade Loops e Função

#Parte 1 - Loop While

#Questão 1:

soma = 0

while True:
	numeros = int(input(" Digite números, depois digite 0 para somá-los: "))
	
	if numeros != 0:
		soma = soma + numeros
	else:
		break

print(f" A soma dos núemros é: {soma}")

#Questão 2:

while True:
	senha = input(" Digite a senha correta: ")
	if senha != "python123":
		print(" Senha incorreta!")
	else:
		print(" Bem vindo(a) ao sistema.")
		break
		
#Questão 3:

escolha = int(input(" Digite um número para ver a tabuada dele: "))
print()
x = 1

while x <= 10:
	print(f" {escolha} x {x} = {escolha*x} \n")
	x = x + 1

#Parte 2 - Loop For

#Questão 4:

listaDePares = []
for x in range(1,21):
	if x%2==0:
		listaDePares.append(x)

print(f" A lista de números pares é: {listaDePares}")

#Questão 5:

#Algoritmo para descobrir qual número é o maior:
#Funciona apenas com números positivos

lista = []

num1 = int(input(" Digite um número: "))
lista.append(num1)
num2 = int(input(" Digite um número: "))
lista.append(num2)
num3 = int(input(" Digite um número: "))
lista.append(num3)
num4 = int(input(" Digite um número: "))
lista.append(num4)
num5 = int(input(" Digite um número: "))
lista.append(num5)

max = 0

for num in lista:
	if num > max:
		max = num

print(f" Teoricamente esse é o maior número: {max}")


#Questão 6:

palavra = input(" Digite uma palavra: ")
vogais = ["a", "e", "i", "o", "u"]
numDeVogais = 0
for letra in palavra:
	if letra in vogais:
		numDeVogais += 1

#Só funciona para palavras sem acentos
print(f" O número de vogais na palavra: {numDeVogais}")

#Parte 3 - Funções

#Questão 7:

def soma(num1, num2):
	oper = num1 + num2
	return oper

print(soma(2,4))

#Questão 8:

def parOrImpa(num):
	if num%2==0:
		return True
	else:
		return False
		
numero = int(input(" Digite um número: "))
print(parOrImpa(numero))

#Questão 9:

lista = [2,4,5,6,7,8,9]

def mediaDaLista(lista):
	somaDosNums = 0
	quant = 0
	for num in lista:
		somaDosNums += num
		quant += 1
	media = somaDosNums/quant
	return media

print(f" A media dos números dessa lista é: {mediaDaLista(lista):.2f}")


#Questão 10:

def saudacao(nome):
	print(f" Olá, {nome}! Seja bem-vindo(a)!")

	
nome = input(" Digite seu nome: ")
saudacao(nome)
	








	

