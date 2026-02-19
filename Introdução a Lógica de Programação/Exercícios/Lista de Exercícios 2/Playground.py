from random import choice
n = 0
while n < 10:
    linha1 = [1, 2, 3, 4, 5]
    linha2 = [6, 7, 8, 9, 10]

    matriz = [
        (linha1),
        (linha2)
    ]
    n = n + 1
    escolha = input('Digite qual casa você escolhe: ')
    escolha.split()
    colunas = ' A B C D E '.split()
    linhas = ' 1 2 '.split()
    print(escolha)
    print(colunas)
    print(linhas)
    coluna_escolhida = colunas.index(escolha[0])
    linha_escolhida = linhas.index(escolha[1])
    print(coluna_escolhida)
    print(linha_escolhida)
    matriz[linha_escolhida][coluna_escolhida] = '?'
    print(matriz)

