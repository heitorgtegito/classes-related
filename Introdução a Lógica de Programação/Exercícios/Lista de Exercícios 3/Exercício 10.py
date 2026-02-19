def f1(x):
  return x ** 2 - 1

def f2(x):
  return  x // 2 + 1

print(f1(5))
print(f2(7))
print(f1(f2(15)))
# 24, 4, 63