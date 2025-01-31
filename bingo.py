import random

def cartela_back(m): # Cartela base
    coluna1, coluna2, coluna3, coluna4 = [], [], [], []

    if m == 0:  # Modo rápido
        while len(coluna1) < 2:
            n = random.randint(1, 10)
            if n not in coluna1:
                coluna1.append(n)
        while len(coluna2) < 2:
            n = random.randint(11, 20)
            if n not in coluna2:
                coluna2.append(n)
        while len(coluna3) < 2:
            n = random.randint(21, 30)
            if n not in coluna3:
                coluna3.append(n)
        cartela = [[coluna1[i], coluna2[i], coluna3[i]] for i in range(2)]

    if m == 1:  # Modo demorado
        while len(coluna1) < 2:
            n = random.randint(1, 10)
            if n not in coluna1:
                coluna1.append(n)
        while len(coluna2) < 2:
            n = random.randint(11, 20)
            if n not in coluna2:
                coluna2.append(n)
        while len(coluna3) < 2:
            n = random.randint(21, 30)
            if n not in coluna3:
                coluna3.append(n)
        while len(coluna4) < 2:
            n = random.randint(31, 40)
            if n not in coluna4:
                coluna4.append(n)
        cartela = [[coluna1[i], coluna2[i], coluna3[i], coluna4[i]] for i in range(2)]
    return cartela

def cartela_front(c): # Cartela mostrada
    for linha in c:
        for num in linha:
            if num in anteriores:
                print(f"({num:02})", end='')
            else:
                print(f" {num:02}", end=' ')
        print()

def sorteio(a): # Sorteia o número
    print()
    if modo == 0: # Modo rápido
        sorteado = random.randint(1, 30)
        while sorteado in a:
            sorteado = random.randint(1, 30)
        a.append(sorteado)
        print(f"=> Última dezena sorteada: {sorteado:02}")
        print("Dezenas sorteadas até o momento:", end=' ')
        for num in range(30):
            for e in a:
                if e == num:
                    print(f"{e:02}", end=' ')

    if modo == 1: # Modo demorado
        sorteado = random.randint(1, 40)
        while sorteado in a:
            sorteado = random.randint(1, 40)
        a.append(sorteado)
        print(f"=> Última dezena sorteada: {sorteado:02}")
        print("Dezenas sorteadas até o momento:", end=' ')
        for num in range(40):
            for e in a:
                if e == num:
                    print(f"{e:02}", end=' ')
            

print("Indique o modo do jogo: \n0 - RÁPIDO \n1 - DEMORADO")
modo = int(input())
anteriores = []

if modo == 0: # Modo rápido
    jogador_1 = cartela_back(modo)
    jogador_2 = cartela_back(modo)

if modo == 1: # Modo demorado
    jogador_1 = cartela_back(modo)
    jogador_2 = cartela_back(modo)
    jogador_3 = cartela_back(modo)
    jogador_4 = cartela_back(modo)

running = True
while running:
    if modo == 0: # Modo rápido
        print("Jogador 1:")
        cartela_front(jogador_1)
        print()
        print("Jogador 2:")
        cartela_front(jogador_2)
    if modo == 1: # Modo demorado
        print("Jogador 1:")
        cartela_front(jogador_1)
        print()
        print("Jogador 2:")
        cartela_front(jogador_2)
        print()
        print("Jogador 3:")
        cartela_front(jogador_3)
        print()
        print("Jogador 4:")
        cartela_front(jogador_4)

    sorteio(anteriores)
    input("\nDigite ENTER para continuar")
