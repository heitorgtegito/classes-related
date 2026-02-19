v = float(input())
bolos = v // 8.5
troco = v % 8.5
print(bolos, 'bolos')
if troco == 0:
  print('Sem troco')
else:
  print(f'R${troco:.2f} de troco')
