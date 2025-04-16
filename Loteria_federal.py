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
    return sorted(numeros_escolhidos)

def multiplicador_jogos(quantidade_jogos):
    cont = 0
    while quantidade_jogos >= 1:
        cont += 1
        print(f"Jogo {cont} | {jogos_loterica(menu_escolha)}")
        quantidade_jogos -= 1

print("1 - Mega Sena")
print("2 - Loto Fácil")
print("3 - Quina")
#print("4 - Sair")
menu_escolha = int(input("Escolha o número do jogo que deseja jogar: "))
while 0 > menu_escolha or menu_escolha > 4:
    menu_escolha = int(input("Escolha o número do jogo que deseja jogar: "))
jogos_loterica(menu_escolha)
numero_jogos = int(input("Quandos jogos deseja fazer? "))
while 1 > numero_jogos:
    numero_jogos = int(input("Quandos jogos deseja fazer? "))
multiplicador_jogos(numero_jogos)