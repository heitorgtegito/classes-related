#1
print('Olá! Digite um número para eu duplicar')
a = int(input())
print(f'{a*2} é o dobro do seu número')

#2
print('Olá! Digite um número para eu triplicar')
b = int(input())
print(f'{b*3} é o triplo do seu número')

#3
print('Olá! Digite mais um número e então eu somarei todos!')
c = int(input())
d = a+b+c
print(f'{d} é a soma dos seus últimos 3 números!')

#4
print(f'{d*2} é o dobro da soma!')

#5
print('Digite 3 números REAIS e eu farei a média deles')
a = float(input())
b = float(input())
c = float(input())
d = a+b+c
print(f'{round(d/3,1)} é a média aritmética dos seus números')
#6
d = a*1 + b*1.5 + c*2
print(f'{round(d/4.5,1)} é a média ponderada')

#7
print('Agora farei a área de um triângulo qualquer, digite primeiro a altura dele!')
a = float(input())
print('Agora a largura dele!')
b = float(input())
print(f'Então a área do triângulo é {round(a*b/2,1)}')

#8
print('Escolha um número e farei a tabuada dele')
a = int(input())
print(f'Aqui está! \n {a*0} \n {a*1} \n {a*2} \n {a*3} \n {a*4} \n {a*5} \n {a*6} \n {a*7} \n {a*8} \n {a*9} \n {a*10}')

#9
print('Escolha dois números')
a = int(input('Digite o primeiro (base)'))
b = int(input('Digite o segundo (expoente)'))
print(f'{a**b} é o resultado')

#10
print('Escolha o X e o Y da expressão -- 20x^3+2x^2y^5')
a = float(input('Escolha o X \n '))
b = float(input('Agora escolha Y \n '))
c = a**3 * 20
d = a**2 * 2
e = b**5
print(f'{c + d * e } é o resultado')

#11
a = input('Escolha um caractere \n ')
b = ' '
print(f' \n {a*1} \n {a*2} \n {a*3} \n {a*4}')

#12
print(f' \n {b*4} {a} \n {b*3} {a} {a} \n {b*2} {a} {b} {a} \n {b} {a}-----{a}')

#13
a = int(input('Digite o primeiro número \n '))
b = int(input('Digite o segundo número \n'))
print(f' \n Quociente = {a//b} \n Resto = {a%b}')

#14
print('Um bolo custa R$8,50, quantos reais você quer comprar em bolo?')
a = float(input())
print(f'\nVocê consegue comprar {a//8.50} bolos e o troco é de {a%8.50}R$')

#15
print('calculadora de bhaskara dog, vai lá')
a = int(input('Me diga qual o multiplicador de x² \n '))
b = int(input('Agora me diga o multiplicador de x \n '))
c = int(input('Agora me diz qual o número solto \n '))
d = b**2 - 4*a*c
e = d**(1/b)
print(f'Primeira raiz é {(-b + e)/2*a}')
print(f'Já a segunda raiz é {(-b - e)/2*a}')

#16
print('calculadora de hipotenusa')
a = float(input('digite a medida do primeiro cateto \n'))
b = float(input('digite a medida do segundo cateto \n'))
c = b**2 + a**2
print(f'a hipotenusa é {round(c**(1/2),2)}')

#17
a = int(input('Quantos comprimidos você precisa tomar? \n '))
print(f' \n Você precisa comprar {a//6} caixa(as)')

#18
a = int(input('Quantos metros ele correu? \n '))
print(f' \n Ele deu {a//400} volta(as) já!')

#19
print('Um bolo custa R$8,50, quantos reais você quer comprar em bolo?')
a = float(input())
print(f'\nVocê consegue comprar {int(a//8.50)} bolos')
if a%8.50 == 0:
    print('Sem troco')
else:
    print(f'{a%8.50} é o seu troco')

#20
a = int(input('Digite um número e eu verificarei se ele é múltiplo de 5 \n'))
b = a%5
if b == 0:
    print(f'{a} é múltiplo de 5')
else:
    print(f'{a} não é múltiplo de 5')

#21
a = int(input('Digite um número e eu verificarei se ele é múltiplo de 5 e 3 \n'))
b = a%5
c = a%3
if b == 0 and c == 0:
    print(f'{a} é múltiplo de 5 e 3')
else:
    print(f'{a} não é múltiplo de 5 e 3')

#22
a = float(input('Quanto que o vendedor conseguiu vender? \n'))
b = 5/100 * a
if a >= 5000:
    print(f'Ele recebeu R${b + 300} de comissão')
else:
    print(f'Ele recebeu R${b} de comissão')

#23
a = int(input('Quantas caixas de frutas você quer comprar? Cada caixa custa 30R$, e, na compra de mais de 5, recebe um desconto de 2R$ por caixa!'))
if a >= 5:
    b = a * 30
    print(f'{b - 2*a} é o valor total da compra')
else:
    b = a * 30
    print(f'{b} é o valor total da compra')

#24
a = int(input('Escreva o número e eu te darei a raiz quadrada dele, com até 4 casas decimais. \n'))
if a < 0:
    print('Erro, digite um número não negativo da próxima vez.')
else:
    print(f'{round(a**(1/2),4)} é a raiz quadrada do seu número')

#25
a = int(input('Me diga um valor em minutos e te darei o valor em horas e minutos \n'))
if a >= 60:
    b = a//60
    c = a%60
    print(f'São {b} horas e {c} minutos')
else:
    print(f'São {a} minutos')

#26
a = int(input('Qual a bandeira que você quer? Digite 1 para a bandeira 1 (R$3,00 por KM) e digite 2 para a bandeira 2 (R$4,18 por KM) \n'))
b = float(input('Digite agora qual a distância (Em KMs) da viagem \n'))
if a == 1:
    c = 3
    print(f'{c * b + 4.85}R$ é o custo da viagem')
elif a == 2:
    c = 4.18
    print(f'{c * b + 4.85}R$ é o custo da viagem')
else:
    print('Digite uma bandeira válida.')

#27
a = int(input('Digite um número inteiro e eu responderei se ele está fora ou não do intervalo ]0,10[ \n'))
if a > 0 and a < 10:
    print(f'{a} está no intervalo! Então é Falso')
else:
    print(f'{a} está fora do intervalo! Então é Verdadeiro')

#28
a = int(input('Digite um número inteiro e eu responderei se ele está fora ou não do intervalo [0,5] ou no intervalo [10,15] \n'))
if a >= 0 and a <= 5 or a >= 10 and a <= 15:
    print(f'{a} está no intervalo, então é Falso!')
else:
    print(f'{a} não está no intervalo, então é Verdadeiro!')

#29
print('Bem vindo, escolha seus incrementos.')
a = input('Deseja cobertura? Digite s para sim e n para não \n')
b = input('Deseja Granulado? Digite s para sim e n para não \n')
c = int(input('Quantos canudos? Digite um número. \n'))
if a == 's':
    a = 1.50
elif a == 'n':
    a = 0
else:
    print('Digite apenas s ou n.')
if b == 's':
    b = 1.0
elif b == 'n':
    b = 0
else:
    print('Digite apenas s ou n.')
if c >= 0:
    c = c*0.5
    print(f'{round(4.00 + a + b + c,2)}R$ é o preço do sorvete')
else:
    print('Digite um valor válido para os canudos.')

#30
a = int(input('Digite a primeira nota \n'))
b = int(input('Digite a segunda nota \n'))
c = int(input('Digite a terceira nota \n'))
d = round((a + b + c)/3,0)
if d < 30:
    print(f'Média: {d} \nSituação: Reprovado')
elif 30 <= d and d <= 69:
    print(f'Média: {d} \nSituação: Em recuperação')
elif 70 <= d and d <= 100:
    print(f'Média: {d} \nSituação: Aprovado')
else:
    print('Digite números válidos')

#31
a = int(input('Digite um número e direi se ele é multiplo de 5 e/ou múltiplo de 3 \n'))
b = a%5
c = a%3
if b == 0 and c == 0:
    print(f'{a} é múltiplo de 5 e de 3')
elif b == 0 and c != 0:
    print(f'{a} é apenas múltiplo de 5')
elif b != 0 and c == 0:
    print(f'{a} é apenas múltiplo de 3')
else:
    print(f'{a} não é nem múltiplo de 5 nem de 3')

#32
a = input('Em qual turno você estuda? Digite M para matutino, V para vespertino ou N para noturno.')
if a == 'M':
    print(f'O aluno estuda no turno Matutino')
elif a == 'V':
    print(f'O aluno estuda no turno Vespertino')
elif a == 'N':
    print(f'O aluno estuda no turno Noturno')
else:
    print(f'Valor inválido, tente novamente.')

#33
a = float(input('Coloque sua altura para calcularmos seu IMC (em metros) \n'))
b = float(input('Coloque seu peso agora \n'))
c = b/(a**2)
if c < 18.5:
    print('Baixo Peso')
elif 18.5 <= c <= 24.9:
    print('Peso normal')
elif 25 <= c <= 29.9:
    print('Sobrepeso')
elif 30 <= c <= 39.9:
    print('Obesidade')
elif 40 <= c:
    print('Obesidade grave')
else:
    print('Erro!')

#34
a = int(input('Por favor digite as horas que a corrida começou \n'))
b = int(input('Por favor digite os minutos que a corrida começou \n'))
c = int(input('Por favor digite as horas que a corrida terminou \n'))
d = int(input('Por favor digite os minutos que a corrida terminou \n'))
a_minutos = a*60
h_comecou = a_minutos + b
c_minutos = c*60
h_terminou = c_minutos + d
if h_terminou < h_comecou: 
    h_total = h_comecou - h_terminou
    t_horas = (h_total//60) +24
    t_minutos = h_total%60
    print(f'Durou {t_horas}horas e {t_minutos}minutos')
elif h_terminou == h_comecou:
    t_horas = 24
    t_minutos = 0
    print(f'Durou {t_horas}horas e {t_minutos}minutos')
elif h_terminou > h_comecou:
    h_total = h_terminou - h_comecou
    t_horas = h_total//60
    t_minutos = h_total%60
    print(f'Durou {t_horas}horas e {t_minutos}minutos')

#35
'''
Considerando os operadores da linguagem Python, determine o resultado de cada uma das expressões a seguir. 
Considere que as variáveis A, B e C armazenam respectivamente os valores 0, 3 e True.
6 - 2 * 5 + 1 = -3
16 % 4 ** 2 = 0
14 / 7 * 3 = 6
(26 + B) // 7 % B = 1
-1 + -5 * 4 = -21
((2 + 8) * B) ** 2 * B = 2700
(C or True or False) and A > 0 = false
10 // B == 3.3 = false
not C != True = True
A < 0 and B < 0 or C = true
B ** A >= A and C = true
(A < 2 and B == 3) and A * 100 >= 10 or (-A < 0 and C) = false
'''

#36
''' A saída da impressão é -1'''

#37
''' A saída da impressão é 2'''

#38
''' A saída da impressão é 4 ; 8 ; ---- ; 8 ; 4'''

#39
''' A saída da impressão é 3 ; 1 ; 13 ; 4; '''

#40
''' Se for 2 forma: 9 ; Se for -3 forma: -6'''

#41
''' Forma: A B B'''

#42
''' Forma: ABD ABD ABD ACD'''

#43
''' Forma: 5 9 0 3'''

print('ACABOU!')