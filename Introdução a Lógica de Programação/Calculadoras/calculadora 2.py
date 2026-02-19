print("Bom dia/tarde/noite, aqui é a calculadora nerdolinha tá ligado? \nDigite seu primeiro número.")
a = int(input()) # Padrão né, um input básico, ele vai ser o nosso STARTER então por isso que fica fora do loop.


while True: # Loopzinho básico, basicamente ele faz com que se repita até que se torne fake

    print("Digite agora a operação, digite + para somar, - para subtrair, * para multiplicar, / para dividir, // para dividir no número inteiro mais próximo, % para pegar o resto da divisão, ** para potenciação e ^ para radiciação")
    o = input() # Input de Operação

    print("Perfeito dog, digite o próximo número")
    b = int(input()) # Segundo número pra fazer a operação

    if o == '+':
        c = a + b
        print(c)

    elif o == '-':
        c = a - b
        print(c)

    elif o == '*':
        c = a * b
        print(c)

    elif o == '/':
        c = a / b
        print(c)

    elif o == '//':
        c = a // b
        print(c)

    elif o == '%':
        c = a % b
        print(c)

    elif o == '**':
        c = a ** b
        print(c)

    elif o == '^':
        b = 1 / b
        c = a ** b
        print(c)

    else:
        print("Por favor, digite certo na próxima vez.") # Até aqui tudo são operações apenas, eu só tipo, caracterizei cada

    print("Você deseja continuar com esse cálculo? Digite 'sim' para continuar com o resultado anterior, 'nao' para encerrar ou qualquer outra coisa para reiniciar.")
    x = input() # Isso daqui serve pra tipo, se ele quer continuar com o resultado, digite sim, se quiser só usar denovo digite qualquer coisa, caso queira encerrar, digite não

    if x == 'sim': # Se x = sim, então a = c, como o input a está fora do loop, isso faz com q ele seja substituido, no caso C, que é o resultado, se torna A, o primeiro número.
        a = c 
        
    elif x == 'nao': 
        print("Tchau Newba")
        break # Faz o While se tornar false, no caso, quebra o loop, fazendo o programa parar de rodar

    else:
        print("PARE") # Renicia o código, sem salvar histórico
        print("Pufavozinho digite seu primeiro número.")
        a = int(input())

# Dog, vou explicar todo o código aqui só pra garantir tlgd
    # Ele é basicamente uma calculador que utiliza input como base, e usa um sistema de Loop com While & Break pra formar esse loop.