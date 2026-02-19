def f1(x):
  return x % 2 == 0

def f2(x):
  y = x
  while y % 2 != 0:
    y = y + 1
  return y

def f3(x):
  if f1(x):
    return x
  return f2(x)

print(f1(5))
print(f1(6))
print(f2(8))
print(f2(11))
print(f3(1))
print(f3(4))

# False, True, 8, 12, 2, 4