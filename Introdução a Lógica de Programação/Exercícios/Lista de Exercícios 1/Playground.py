
def njogadores():
    quantidade_jogadores = int(input('Digite a quantidade de jogadores: '))
    return quantidade_jogadores

def jogador():
    nome = input('Digite o nome por qual você deseja ser chamado: ')
    pontuacao = 0
    pares_obtidos = ''
    return nome, pontuacao, pares_obtidos

def calcular_vencedor(x,y,z):
    lista = [x,y,z]
    lista.sort(reverse=True)
    return lista

def fim_de_jogo():
    lista = calcular_vencedor(pontjogador1, pontjogador2, pontjogador3)
    p1 = lista.index(pontjogador1)
    p2 = lista.index(pontjogador2)
    p3 = lista.index(pontjogador3)
    mensagemfinal = f''
    if pontjogador1 != pontjogador2 and pontjogador1 != pontjogador3 and pontjogador2 != pontjogador3: 
        if p1 == 0:
            mensagemfinal = f'{jogador1} é o vencedor com {pontjogador1} -> {parjogador1}\n'
        elif p2 == 0:
            mensagemfinal = f'{jogador2} é o vencedor com {pontjogador2} -> {parjogador2}\n'
        elif p3 == 0:
            mensagemfinal = f'{jogador3} é o vencedor com {pontjogador2} -> {parjogador3}\n'
    elif pontjogador1 == pontjogador2 == pontjogador3:
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
                mensagemfinal = f'O jogo terminou empatado entre {jogador1} e {jogador2} com {p1} pontos'
            elif pontjogador2 == pontjogador3:
                mensagemfinal = f'O jogo terminou empatado entre {jogador2} e {jogador3} com {p1} pontos'
            elif pontjogador1 == pontjogador3:
                mensagemfinal = f'O jogo terminou empatado entre {jogador1} e {jogador2} com {p1} pontos'
    return mensagemfinal

quantidade_jogadores = njogadores()
jogador1, pontjogador1, parjogador1 = jogador() 
jogador2, pontjogador2, parjogador2 = jogador()
if quantidade_jogadores == 2:
    caracteres = ' ☺ ☻ ♥ ♦ ♣ ♠ • ○ ◙ ▬ ↨ ♪ '.split()
    pontjogador3 = 0
elif quantidade_jogadores == 3:
    jogador3, pontjogador3, parjogador3 = jogador()
    caracteres = ' ☺ ☻ ♥ ♦ ♣ ♠ • ○ ◙ ▬ ↨ ♪ ♫ ☼ ► ◄ ↕ ‼ ¶ § ⌂ ↨ ↑ ↓ '.split()
print(fim_de_jogo())