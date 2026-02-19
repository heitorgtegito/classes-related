n = 5
ls = [None] * n
for i in range(n):
  ls.append(1)
ls[0] = 5
ls[3] = -3
print(ls)
# 5 None None -3 None 1 1 1 1 1