from random import shuffle
from random import choice


def njogadores():
    quantidade_jogadores = int(input('Digite a quantidade de jogadores: '))
    return quantidade_jogadores

def jogador():
    nome = input('Digite o nome por qual você deseja ser chamado: ')
    pontuacao = 0
    pares_obtidos = ''
    return nome, pontuacao, pares_obtidos

def criar_grade(grade, tamanho_da_grade):
    print('-------------------------')
    for l in range(0,tamanho_da_grade):
        linhas_grade = '|'
        for c in range(0,6):
            linhas_grade = linhas_grade + f' {grade[l][c]} ' + '|'
        print(f'{linhas_grade}' '\n-------------------------')

grade_inicial = [
['?', '?', '?', '?', '?', '?'], 
['?', '?', '?', '?', '?', '?'], 
['?', '?', '?', '?', '?', '?'], 
['?', '?', '?', '?', '?', '?']
]

grade_vazio = [
[' ', ' ', ' ', ' ', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ']
]

def entrada(quantidade, jogadas_feitas):
    while True:
        escolha = input('Digite qual casa deseja selecionar: ').upper()
        escolha.split()
        colunas = ['1','2','3','4','5','6']
        if quantidade_jogadores == 2:
            linhas = ['A','B']
        elif quantidade_jogadores == 3:
            linhas = ['A','B','C','D']
        if len(escolha) != 2:
            print('Jogada Inválida, tente novamente')
            continue
        elif (escolha[0] not in linhas) or (escolha[1] not in colunas):
            print('Jogada Inválida, tente novamente')
            continue
        coluna_escolhida = colunas.index(escolha[1])
        linha_escolhida = linhas.index(escolha[0])
        posicao = (linha_escolhida, coluna_escolhida)
        if posicao in jogadas_feitas:
            print('Jogada Inválida, peça do local já foi pega, tente novamente')
            continue
        return linha_escolhida, coluna_escolhida

def criar_pilha():
    n = len(caracteres)
    shuffle(caracteres)
    pilha_de_caracteres = caracteres[0:n]
    return pilha_de_caracteres

def criar_grade_simbolos():
    if quantidade_jogadores == 2:
        linha1 = caracteres[0:6]
        linha2 = caracteres[6:12]
        grade_simbolos = [
            (linha1),
            (linha2)
        ]
    elif quantidade_jogadores == 3:
        linha1 = caracteres[0:6]
        linha2 = caracteres[6:12]
        linha3 = caracteres[12:18]
        linha4 = caracteres[18:24]
        grade_simbolos = [
            (linha1),
            (linha2),
            (linha3),
            (linha4)
        ]
    return grade_simbolos

def dois_jogadores():
    print('Será impresso uma grade de 6x2, as linhas são referenciadas por letras (A ou B) e as colunas são referenciadas por números (1, 2, 3, 4, 5 ou 6). Seu objetivo é encontrar o par do caractere que está vísivel. Para selecionar a casa, em que você acredita estar o par, digite a letra correspondente e o número (A1, C2, ...). Ganha o jogo, o usuário que obtiver a maiorquantidade de pares. \nBom Jogo!') # Imprime um tutorial para o jogador    
    # Aqui é o começo do loop caso a peça seja revelada
    peca_revelada = True
    turno1 = turno2 = turno3 = 0
    pontjogador1 = pontjogador2 = pontjogador3 = 0
    parjogador1 = parjogador2 = parjogador3 = ''
    jogadas_feitas = []
    # jogada = True
    while peca_revelada == True:
        peca = peca_aleatoria()
        if peca == None:
            print(fim_de_jogo(pontjogador1, pontjogador2, 0, parjogador1, parjogador2, 0))
            break
        peca_revelada = False
        # Aqui é pra começar o loop de turno caso a peça não seja revelada
        while peca_revelada == False:
            vez, turno1, turno2 = turno(turno1, turno2, turno3)
            print(f'É a sua vez {vez}')
            criar_grade(grade_inicial, 2)
            print(f'O par que você deve buscar é: {peca}')
            linha_escolhida, coluna_escolhida = entrada(2,jogadas_feitas)
            grade_simbolos = criar_grade_simbolos()
            simbolo_revelado = grade_simbolos[linha_escolhida][coluna_escolhida]
            grade_inicial[linha_escolhida][coluna_escolhida] = simbolo_revelado
            if simbolo_revelado == peca:
                grade_inicial[linha_escolhida][coluna_escolhida] = grade_vazio[linha_escolhida][coluna_escolhida]
                peca_revelada = True
                criar_grade(grade_inicial, 2)
                jogadas_feitas += [((linha_escolhida),(coluna_escolhida))]
                if vez == jogador1:
                    pontjogador1 += 1
                    parjogador1 = parjogador1 + f'{simbolo_revelado}'
                elif vez == jogador2:
                    pontjogador2 += 1
                    parjogador2 = parjogador2 + f'{simbolo_revelado}'
            else:
                criar_grade(grade_inicial, 2)
                grade_inicial[linha_escolhida][coluna_escolhida] = '?'
            print(f'{jogador1}: {pontjogador1} -> Pares obtidos: {parjogador1}')
            print(f'{jogador2}: {pontjogador2} -> Pares obtidos: {parjogador2}')
            fim_de_turno()

def peca_aleatoria():
    if len(pilha_de_caracteres) == 0:
        return None
    peca = choice(pilha_de_caracteres)
    pilha_de_caracteres.remove(peca)
    return peca

def tres_jogadores():
    print('Será impresso uma grade de 6x6, as linhas são referenciadas por letras (A, B, C ou D) e as colunas são referenciadas por números (1, 2, 3, 4, 5 ou 6). Seu objetivo é encontrar o par do caractere que está vísivel. Para selecionar a casa, em que você acredita estar o par, digite a letra correspondente e o número (A1, C2, ...). Ganha o jogo, o usuário que obtiver a maiorquantidade de pares. \nBom Jogo!') # Imprime um tutorial para o jogador
    # Aqui é o começo do loop caso a peça seja revelada
    peca_revelada = True
    turno1 = turno2 = turno3 = 0
    pontjogador1 = pontjogador2 = pontjogador3 = 0
    parjogador1 = parjogador2 = parjogador3 = ''
    jogadas_feitas = []
    # jogada = True
    while peca_revelada == True:
        peca = peca_aleatoria()
        if peca == None:
            print(fim_de_jogo(pontjogador1, pontjogador2, pontjogador3, parjogador1, parjogador2, parjogador3))
            break
        peca_revelada = False
        # Aqui é pra começar o loop de turno caso a peça não seja revelada
        while peca_revelada == False:
            vez, turno1, turno2, turno3 = turno(turno1, turno2, turno3)
            print(f'É a sua vez {vez}')
            criar_grade(grade_inicial, 4)
            print(f'O par que você deve buscar é: {peca}')
            linha_escolhida, coluna_escolhida = entrada(3,jogadas_feitas)
            grade_simbolos = criar_grade_simbolos()
            simbolo_revelado = grade_simbolos[linha_escolhida][coluna_escolhida]
            grade_inicial[linha_escolhida][coluna_escolhida] = simbolo_revelado
            if simbolo_revelado == peca:
                grade_inicial[linha_escolhida][coluna_escolhida] = grade_vazio[linha_escolhida][coluna_escolhida]
                peca_revelada = True
                criar_grade(grade_inicial, 4)
                jogadas_feitas += [((linha_escolhida),(coluna_escolhida))]
                if vez == jogador1:
                    pontjogador1 += 1
                    parjogador1 = parjogador1 + f'{simbolo_revelado}'
                elif vez == jogador2:
                    pontjogador2 += 1
                    parjogador2 = parjogador2 + f'{simbolo_revelado}'
                elif vez == jogador3:
                    pontjogador3 += 1
                    parjogador3 = parjogador3 + f'{simbolo_revelado}'
            else:
                criar_grade(grade_inicial, 4)
                grade_inicial[linha_escolhida][coluna_escolhida] = '?'
            print(f'{jogador1}: {pontjogador1} -> Pares obtidos: {parjogador1}')
            print(f'{jogador2}: {pontjogador2} -> Pares obtidos: {parjogador2}')
            print(f'{jogador3}: {pontjogador3} -> Pares obtidos: {parjogador3}')
            fim_de_turno()

def turno(turno1,turno2,turno3):
    if quantidade_jogadores == 3:
        if turno1 <= turno2 and turno1 <= turno3:
            vez = jogador1
            turno1 += 1
        elif turno2 <= turno1 and turno2 <= turno3:
            vez = jogador2
            turno2 += 1
        else:
            vez = jogador3
            turno3 += 1
        return vez, turno1, turno2, turno3
    elif quantidade_jogadores == 2:
        if turno1 <= turno2:
            vez = jogador1
            turno1 += 1
        elif turno2 <= turno1:
            vez = jogador2
            turno2 += 1
        return vez, turno1, turno2

def fim_de_turno():
    input('Aperte ENTER para ir para o próximo jogador') # Imput para avançar para o próximo turno
    for i in range(0, 50): # Imprime as 50 linhas em branco
        print(' ')

def calcular_vencedor(x,y,z):
    if quantidade_jogadores == 3:
        lista = [x,y,z]
        lista.sort(reverse=True)
        return lista
    else:
        lista = [x,y]
        lista.sort(reverse=True)
        return lista
    
def fim_de_jogo(x,y,z,a,b,c):
    pontjogador1 = x
    pontjogador2 = y
    pontjogador3 = 0
    parjogador1 = a
    parjogador2 = b
    parjogador3 = ''
    if quantidade_jogadores == 3:
        pontjogador3 = z
        parjogador3 = c
    lista = calcular_vencedor(pontjogador1, pontjogador2, pontjogador3)
    mensagemfinal = f''
    if pontjogador1 == pontjogador2 == pontjogador3:
        mensagemfinal = f'Ocorreu um empate TRIPLO! entre {jogador1}, {jogador2} e {jogador3}, todos ficaram com {pontjogador1} pontos!'
    elif pontjogador1 == pontjogador2 or pontjogador3 == pontjogador1 or pontjogador2 == pontjogador3:
        if lista[0] != lista[1]:
            if pontjogador1 == lista[0]:
                mensagemfinal = f'{jogador1} é o vencedor com {pontjogador1} -> {parjogador1}\n'
            elif pontjogador2 == lista[0]:
                mensagemfinal = f'{jogador2} é o vencedor com {pontjogador2} -> {parjogador2}\n'
            elif pontjogador3 == lista[0]:
                mensagemfinal = f'{jogador3} é o vencedor com {pontjogador3} -> {parjogador3}\n'
        else:
            if pontjogador1 == pontjogador2:
                mensagemfinal = f'O jogo terminou empatado entre {jogador1} e {jogador2} com {pontjogador1} pontos'
            elif pontjogador2 == pontjogador3:
                mensagemfinal = f'O jogo terminou empatado entre {jogador2} e {jogador3} com {pontjogador2} pontos'
            elif pontjogador1 == pontjogador3:
                mensagemfinal = f'O jogo terminou empatado entre {jogador1} e {jogador3} com {pontjogador1} pontos'
    else:
        if lista[0] != lista[1]:
            if pontjogador1 == lista[0]:
                mensagemfinal = f'{jogador1} é o vencedor com {pontjogador1} pontos -> {parjogador1}'
            elif pontjogador2 == lista[0]:
                mensagemfinal = f'{jogador2} é o vencedor com {pontjogador2} pontos-> {parjogador2}'
            elif pontjogador3 == lista[0]:
                mensagemfinal = f'{jogador3} é o vencedor com {pontjogador3} pontos-> {parjogador3}'
    print(f'{jogador1} fez {pontjogador1} pontos e obteves os seguintes pares: {parjogador1}\n')
    print(f'{jogador2} fez {pontjogador2} pontos e obteves os seguintes pares: {parjogador2}\n')
    if quantidade_jogadores == 3:
        print(f'{jogador3} fez {pontjogador3} pontos e obteves os seguintes pares: {parjogador3}\n')
    return mensagemfinal

quantidade_jogadores = njogadores()
jogador1, pontjogador1, parjogador1 = jogador() 
jogador2, pontjogador2, parjogador2 = jogador()
if quantidade_jogadores == 2:
    caracteres = ' ☺ ☻ ♥ ♦ ♣ ♠ • ○ ◙ ▬ ↨ ♪ '.split()
    pilha_de_caracteres = criar_pilha()
    pontjogador3 = 0
    jogador3 = ''
    dois_jogadores()
elif quantidade_jogadores == 3:
    jogador3, pontjogador3, parjogador3 = jogador()
    caracteres = ' ☺ ☻ ♥ ♦ ♣ ♠ • ○ ◙ ▬ ↨ ♪ ♫ ☼ ► ◄ ↕ ‼ ¶ § ⌂ ø ↑ ↓ '.split()
    pilha_de_caracteres = criar_pilha()
    tres_jogadores()