la = [0, 5, 3, -1, 2]
sp = 0
si = 0
i = 0
while i < len(la):
  if i % 2 == 0:
    sp += la[i] # 0 + 3 + 2
  else:
    si += la[i] # 5 + -1
  i += 1
print(sp)
print(si)
# 5 4 