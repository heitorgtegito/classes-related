def f1(m):
  r = []
  for i, l in enumerate(m):
    for j, e in enumerate(l):
      if e < 0:
        r.append([i, j])
  return r

a = [
  [1, 2, 3, 4], 
  [10, 20, 30, 40]
]
print(f1(a))
a = [
  [1, -2], 
  [10, 20]
]
print(f1(a))
a = [
  [3, -10, 1], 
  [0, 5, -9]
]
print(f1(a))
# [], [[0,1]], [[0,1],[1,2]]