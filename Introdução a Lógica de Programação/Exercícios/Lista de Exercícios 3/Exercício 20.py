
n1 = int(input())
n2 = int(input())
n3 = int(input())
media = (n1 + n2 + n3) // 3
print('Média:', media)
if media < 30:
  print('Resultado: Reprovado')
elif media >= 30 and media <= 69:
  print('Resultado: Em recuperação')
else:
  print('Resultado: Aprovado')

# tem um erro nesse elif aí, erap ra ser media >= 30 e media < 70, pq se o cara tirar 69.999999 ele tá de rec, mas se tirar 70 passa.