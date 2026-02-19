def marcar_posicao(x, y, jogador, grade):
  if not(x >=0 and x < 3 and y >=0 and y < 3 and grade[x][y] == 0):
    return False
  grade[x][y] = jogador
  return True

def checar_vencedor(grade):
  for i in range(0, 3):
    # verifica linha
    if grade[i][0] != 0 and grade[i][0] == grade[i][1] and grade[i][1] == grade[i][2]:
      return grade[i][0]
    # verifica coluna
    if grade[0][i] != 0 and grade[0][i] == grade[1][i] and grade[1][i] == grade[2][i]:
      return grade[0][i]
    # verifica diagonal
    if grade[0][0] != 0 and grade[0][0] == grade[1][1] and grade[1][1] == grade[2][2]:
      return grade[0][0]
    # verifica a outra diagonal
    if grade[0][2] != 0 and grade[0][2] == grade[1][1] and grade[1][1] == grade[2][0]:
      return grade[0][2]
    # verifica empate
    contador = 0
    for i in range(0, 3):
      for j in range(0, 3):
        if grade[i][j] != 0:
          contador += 1
    if contador == 9:
      return -1 # empate
    return 0 # partida não acabou

def print_grade(grade):
  for l in range(0, 3):
    print(f'{grade[l][0]}|{grade[l][1]}|{grade[l][2]}')
    if l < 2:
      print('-----')

# programa principal
grade = [
  [0, 0, 0], 
  [0, 0, 0], 
  [0, 0, 0]
]
jogador = 1

print_grade(grade)
while checar_vencedor(grade) == 0:
  print(f'Jogador {jogador}')
  x = int(input(' Informe a linha: '))
  y = int(input(' Informe a coluna: '))
  jogada_ok = marcar_posicao(x, y, jogador, grade)
  if jogada_ok:
    jogador = 2 if jogador == 1 else 1
  else:
    print('Jogada inválida!')
  print_grade(grade)
vencedor = checar_vencedor(grade)
if vencedor == -1:
  print('Empate!')
else:
  print(f'Jogador {vencedor} ganhou!')