def f1(m):
  x = 0
  for l in m:
    for e in l:
      if e > 5:
        x += 1
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
a = [
  [3, -10, 1], 
  [0, 5, -9]
]
print(f1(a))
# 4, 2, 0