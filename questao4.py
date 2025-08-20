#Questão 4

numero = float(input(" Digite um número: "))
if numero >= 0:

	raizDoNumero = numero**0.5 

	print(f" A raiz quadrada é: {raizDoNumero:.2f}")
else:
	print(f" Não existe raiz quadrada para números negativos")
