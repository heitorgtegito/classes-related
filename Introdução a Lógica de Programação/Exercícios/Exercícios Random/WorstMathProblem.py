from random import choice
resultado = ''
problema = 0
# seguindo o PEMDAS -> 9 + 13 * 4/1 + 5 + 12 * 2 - 7 - 11 + 8 * 3/6 -10
# sem PEMDAS -> 5 + 13 * 4/9 + 7 + 12 * 1 - 3 - 11 + 6 * 8/2 -10 = 66
while problema != 66:
    lista = [1,2,3,4,5,6,7,8,9]
    a = choice(lista)
    lista.remove(a)
    b = choice(lista)
    lista.remove(b)
    c = choice(lista)
    lista.remove(c)
    d = choice(lista)
    lista.remove(d)
    e = choice(lista)
    lista.remove(e)
    f = choice(lista)
    lista.remove(f)
    g = choice(lista)
    lista.remove(g)
    h = choice(lista)
    lista.remove(h)
    i = choice(lista)
    lista.remove(i)
    # problema = a + 13 * b/c + d + 12*e - f - 11 + g * h/i - 10
    problema = (((((((((((a + 13) * b)/c) + d) + 12) *e) - f) - 11) + g) * h) /i) - 10
    resultado = f'{a} + 13 * {b}/{c} + {d} + 12 * {e} - {f} - 11 + {g} * {h}/{i} -10 = 66'
print(resultado)