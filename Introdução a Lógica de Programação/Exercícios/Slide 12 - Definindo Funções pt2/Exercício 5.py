def funcao(i):
  if -3 < i < -1:
    return 'Z'
  elif i == 0:
    return 'Y'
  x = i % 3
  if x == 0:
    return 'T'
  elif x == 1:
    return 'U'
  return 'W'

print(funcao(3))
print(funcao(5))
print(funcao(0))
print(funcao(4))
print(funcao(-10))
print(funcao(-2))

# T W Y U W Z