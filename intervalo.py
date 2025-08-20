valor = float(input())

if valor > 0 and valor < 25.01:
	print(f"Intervalo (0,25]")
elif valor >= 25.01 and valor < 50.01:
	print(f"Intervalo (25,50]")
elif valor >= 50.01 and valor < 75.01:
	print(f"Intervalo (50,75]")
elif valor >= 75.01 and valor < 100.01:
	print(f"Intervalo (75,100]")
else:
	print(f"Fora de intervalo")