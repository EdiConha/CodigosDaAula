# Respostas da lista:

#Questão 1

num1 = int(input("Digite um número: "))
num2 = int(input("Digite o segundo: "))
num3 = int(input("Digite o terceiro: "))
num4 = int(input("Digite o quarto: "))
num5 = int(input("Digite o quinto: "))

print(f"Ordem de entrada: {num1},{num2},{num3},{num4},{num5}")
print()
print(f"Ordem invertida: {num5},{num4},{num3},{num2},{num1}")


#Questão 2

num1 = int(input("Digite um número: "))
num2 = int(input("Digite o segundo: "))


print(f"Diferença entre os dois números: {num1 - num2}")


#Questão 3

nota1 = float(input(" Digite a primeira nota: "))
nota2 = float(input(" Digite a segunda nota: "))
nota3 = float(input(" Digite a terceira nota: "))
nota4 = float(input(" Digite a quarta nota: "))

media = (nota1+nota2+nota3+nota4)/4


print(f"A sua primeira nota: {nota1:.2f}")
print(f"A sua segunda nota: {nota2:.2f}")
print(f"A sua terceira nota: {nota3:.2f}")
print(f"A sua quarta nota: {nota4:.2f}")
print(f"A média é: {media:.2f}")

#Questão 4

numero = float(input(" Digite um número: "))
if numero >= 0:

	raizDoNumero = numero**0.5 

	print(f" A raiz quadrada é: {raizDoNumero:.2f}")
else:
	print(f" Não existe raiz quadrada para números negativos")


#Questão 5

ladoDoQuadrado = float(input(" Digite o tamanho do lado do quadrado: "))

calcLado = ladoDoQuadrado**2
calcVol = ladoDoQuadrado**3

print(f"A área do quadrado: {calcLado:.2f}")
print(f"O volume do cubo: {calcVol:.2f}")


#Questão 6

quantGanhaHoraTrab = float(input(" Digite o preço da sua hora trabalhada: "))
horasTrabNoMes = float(input(" Digite quantas horas você trabalhou esse mês: "))

salarioTotal = quantGanhaHoraTrab * horasTrabNoMes

print(f"Seu salário é: R$ {salarioTotal}")


