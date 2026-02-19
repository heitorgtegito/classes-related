a = int(input())
b = int(input())
x = min(a, b)
while x >= 1:
  if a % x == 0 and b % x == 0:
    print(x)
    break # interrompe o while
  x = x - 1
