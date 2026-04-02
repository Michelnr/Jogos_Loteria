# Programa criado para criar numeras aleatorios para jogar nos jogos da loteria federal.

def jogos_loterica(escolha):
    from random import randint
    
    numeros_escolhidos = []
    
    # Números para Mega Sena.
    if escolha == 1:
        while len(numeros_escolhidos) < 6:
            numero = randint(1,60)
            if numero not in numeros_escolhidos:
                numeros_escolhidos.append(numero)
    
    # Números Loto Fácil
    elif escolha == 2:
        while len(numeros_escolhidos) < 15:
            numero = randint(1,25)
            if numero not in numeros_escolhidos:
                numeros_escolhidos.append(numero)
    
    # Números da Quina
    else:
        while len(numeros_escolhidos) < 5:
            numero = randint(1,80)
            if numero not in numeros_escolhidos:
                numeros_escolhidos.append(numero)
    
    return sorted(numeros_escolhidos)

def multiplica_jogos(quantidade_jogos):
    cont = 0
    while quantidade_jogos > cont:
        numeros = jogos_loterica(menu_escolha)
        cont += 1
        print(f"Jogo {cont} | {numeros}")
    print(40*'-')


while True:
    print("1 - Mega Sena")
    print("2 - Loto Fácil")
    print("3 - Quina")
    print("4 - Sair")

    menu_escolha = int(input("Escolha o número do jogo que deseja jogar: "))
    
    if menu_escolha == 4:
        break

    if 1 > menu_escolha > 4:
        print('Escolha invalida, escolha entre 1 e 4!!!')
        continue

    numero_jogos = int(input("Quandos jogos deseja fazer? "))

    if type(numero_jogos) != int:
        print('NUMERO INVALIDO, Por favor, informa um numero inteiro!')
        continue

    
    multiplica_jogos(numero_jogos)