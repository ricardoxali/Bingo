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
        while len(coluna1) < 3:
            n = random.randint(1, 10)
            if n not in coluna1:
                coluna1.append(n)
        while len(coluna2) < 3:
            n = random.randint(11, 20)
            if n not in coluna2:
                coluna2.append(n)
        while len(coluna3) < 3:
            n = random.randint(21, 30)
            if n not in coluna3:
                coluna3.append(n)
        while len(coluna4) < 3:
            n = random.randint(31, 40)
            if n not in coluna4:
                coluna4.append(n)
        cartela = [[coluna1[i], coluna2[i], coluna3[i], coluna4[i]] for i in range(3)]
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
            
def vitoria(c):
    sort = 0
    if modo == 0: # Modo rápido
        for linha in c:
            for e in linha:
                if e in anteriores:
                    sort += 1
                    if sort == 6:
                        return True
        return False

    if modo == 1: # Modo demorado
        for linha in c:
            for e in linha:
                if e in anteriores:
                    sort += 1
                    if sort == 12:
                        return True
        return False

print("Indique o modo do jogo: \n0 - RÁPIDO \n1 - DEMORADO")
modo = int(input())
anteriores = []
primeira_vez = True

jogador_1 = cartela_back(modo)
jogador_2 = cartela_back(modo)

if modo == 1: # Modo demorado
    jogador_3 = cartela_back(modo)
    jogador_4 = cartela_back(modo)

while True:
    print("Jogador 1:")
    cartela_front(jogador_1)
    print()
    print("Jogador 2:")
    cartela_front(jogador_2)

    if modo == 1: # Modo demorado
        print()
        print("Jogador 3:")
        cartela_front(jogador_3)
        print()
        print("Jogador 4:")
        cartela_front(jogador_4)

    if not primeira_vez:
        input("\nDigite ENTER para continuar")
    else:
        print()
    primeira_vez = False

    vencedores = []

    if vitoria(jogador_1):
        vencedores.append("1")
    if vitoria(jogador_2):
        vencedores.append("2")
        
    if modo == 1: # Modo demorado
        if vitoria(jogador_3):
            vencedores.append("3")
        if vitoria(jogador_4):
            vencedores.append("4")
    
    if len(vencedores) == 1:
        print(f"\nJogador {vencedores[0]} é o ganhador! \\o/")
    elif len(vencedores) == 2:
        print(f"\nJogadores {vencedores[0]} e {vencedores[1]} são os ganhadores! \\o/")
    elif len(vencedores) == 3:
        print(f"\nJogadores {vencedores[0]}, {vencedores[1]} e {vencedores[2]} são os ganhadores! \\o/")
    elif len(vencedores) == 4:
        print("\nTodos os jogadores são os ganhadores! \\o/")
    else:
        sorteio(anteriores)

    if len(vencedores) != 0:
        break
    print()