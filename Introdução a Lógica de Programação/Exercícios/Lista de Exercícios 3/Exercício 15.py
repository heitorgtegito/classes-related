
def f1(m):
  x = 0
  for i in range(len(m)):
    for j in range(0, len(m[0]), 2):
      x = x + m[i][j]
  return x

a = [
  [1, 2, 3, 4], 
  [10, 20, 30, 40]
]
print(f1(a))
a = [
  [1, 2], 
  [10, 20]
]
print(f1(a))
# 44, 11