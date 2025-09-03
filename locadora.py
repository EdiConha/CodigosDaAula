listaDeFilmes = ["e o vento levou", "hulk", "captão america"]
listaDeAlugDOS = []


print(" OPÇÃO: 1 LISTAR OS FILMES")
print(" OPÇÃO: 2 DEVOLVER UM FILME")
print(" OPÇÃO: 3 ALUGAR")
print(" OPÇÃO: 4 SAIR\n")

escolha = 0

while escolha != 4:
    escolha = int(input(" Digite uma opção: "))
    while True: # Das opções:
        
        if escolha == 1:
            for item in listaDeFilmes:
                print(f" Filme:{item}")
            
            break
        
        elif escolha == 2: #Devolver um filme
            filme = input(" Digite o nome do filme:").lower()
            if filme not in listaDeFilmes and filme in listaDeAlugDOS:
                listaDeAlugDOS.remove(filme)
                listaDeFilmes.append(filme)
                print(f" O filme {filme} foi devolvido, obrigado.\n")
                break
            else:
                print(" O filme q você está tentando devolver não está na lista para  alugar ainda!\n")
                break
        elif escolha == 3: #Alugar filme
            filme = input(" Digite o nome do filme:").lower()
            if filme not in listaDeAlugDOS:
                listaDeFilmes.remove(filme)
                listaDeAlugDOS.append(filme)
                print(" O seu filme foi alugado, obg.\n")
                break
        elif escolha == 4:
            print("saindo da locadora.\n")
            break
