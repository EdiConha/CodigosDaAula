#

idade = int(input(" Qual a sua idade: "))
ingresso = input(" Você possui ingresso: ").lower()
listaDeRespostas =  ["s", "sim"]

if idade >=18 and ingresso in listaDeRespostas:
	print(f"Parabéns você possui idade e ingresso! Pode entrar.")
elif idade < 18 and ingresso not in listaDeRespostas:
	print(f"Sinto muito mas você não é de maior e nem tem ingresso!")
elif idade < 18 and ingresso in listaDeRespostas:
	print(f"Você não é de maior mas possui ingresso.")
elif idade >= 18 and ingresso not in listaDeRespostas:
	print(f"Você é de maior mas não possui ingresso.")
else:
	print(f"Você digitou algo errado.")