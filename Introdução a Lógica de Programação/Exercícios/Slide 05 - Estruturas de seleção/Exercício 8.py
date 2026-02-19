a = int(input('Digite sua idade\n'))
if a < 5:
    print('Muito novo ainda, aguarde até os 5 anos no mínimo.')
elif 5 <= a <= 7:
    print('Peixinho')
elif 8 <= a <= 10:
    print('Infantil A')
elif 11 <= a <= 13:
    print('Infantil B')
elif 14 <= a <= 17:
    print('Juvenil')
elif a >= 18:
    print('Adulto')
else:
    print('Digite um número válido.')