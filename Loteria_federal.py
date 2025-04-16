# Programa criado para criar numeras aleatorios para jogar nos jogos da loteria federal.

from random import randint

def jogos_loterica(escolha):
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
    elif escolha == 3:
        while len(numeros_escolhidos) < 5:
            numero = randint(1,80)
            if numero not in numeros_escolhidos:
                numeros_escolhidos.append(numero)
    else:
        print("1 - Mega Sena")
        print("2 - Loto Fácil")
        print("3 - Quina")
        escolha = int(input("Escolha o número do jogo que deseja jogar: "))
    return sorted(numeros_escolhidos)

print("1 - Mega Sena")
print("2 - Loto Fácil")
print("3 - Quina")
menu_escolha = input("Escolha o número do jogo que deseja jogar: ")
if 0 > menu_escolha > 4 or menu_escolha is not int:
    menu_escolha = input("Escolha o número do jogo que deseja jogar: ")
numero_jogos = input("Quandos jogos deseja fazer? ")
if 0 > menu_escolha or menu_escolha is not int:
    numero_jogos = input("Quandos jogos deseja fazer? ")

if numero_jogos >= 1:
    cont = 0
    while numero_jogos >= 1:
        cont += 1
        print(f"Jogo {cont} | {jogos_loterica(menu_escolha)}")
        numero_jogos -= 1