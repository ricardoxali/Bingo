import random

def cartela(m):
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
        return [[coluna1[i], coluna2[i], coluna3[i]] for i in range(2)]

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
        return [[coluna1[i], coluna2[i], coluna3[i], coluna4[i]] for i in range(2)]

def mostrar_cartela(cartela):
    for linha in cartela:
        for num in linha:
            print(f"{num:02}", end='    ')
        print()

def sorteio(a):
    print()
    if modo == 0: # Modo rápido
        sorteado = random.randint(1, 30)
        while sorteado in a:
            sorteado = random.randint(1, 30)
        a.append(sorteado)
        print(f"=> Última dezena sorteada: {sorteado:02}")
        print("Dezenas sorteadas até o momento:", end=' ')
        for e in a:
            print(f"{e:02}", end=' ')

    if modo == 1: # Modo demorado
        sorteado = random.randint(1, 40)
        while sorteado in a:
            sorteado = random.randint(1, 40)
        a.append(sorteado)
        print(f"=> Última dezena sorteada: {sorteado:02}")
        print("Dezenas sorteadas até o momento:", end=' ')
        for e in a:
            print(f"{e:02}", end=' ')
            

print("Indique o modo do jogo: \n0 - RÁPIDO \n1 - DEMORADO")
modo = int(input())
anteriores = []

running = True
while running:
    if modo == 0: # Modo rápido
        jogador = 1
        while jogador < 3:
            print(f"\nJogador {jogador}:")
            cartela_jogador = cartela(modo)
            mostrar_cartela(cartela_jogador)
            jogador += 1
    if modo == 1: # Modo demorado
        jogador = 1
        while jogador < 5:
            print(f"\nJogador {jogador}:")
            cartela_jogador = cartela(modo)
            mostrar_cartela(cartela_jogador)
            jogador += 1
    sorteio(anteriores)
    input("\nDigite ENTER para continuar")
