#Desafio do login

login = input(" Digite seu login: ").lower()
senha = input(" Digite sua senha: ").lower()

if login == "admin" and senha == "admin":
	print(f" Parabéns você está logado Administrador!")
elif login == "ana" and senha == "1234":
	print(f" Parabéns Ana, você está logada!")
elif login == "edi" and senha == "1234":
	print(f" Parabéns Edi, você está logado")
else:
	print(f"Usuário ou senha invalidas")