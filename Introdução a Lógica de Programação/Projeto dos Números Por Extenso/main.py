print('Olá, seja bem-vindo! Esta ferramenta serve para "descomprimir" o número, como se fosse fatorá-lo.')
a = int(input('Por favor, digite um número: '))

if isinstance(a, int):
    # Convert the number to a string to work with each digit
    a = str(a)
    
    # Initialize an empty string to store the result
    resultado = ''
    
    # Loop through the digits and add each place value (e.g., 10000 + 2000 + 400 + 10 + 5)
    for indice, digito in enumerate(a):
        # Create the place value (e.g., 10000, 2000, etc.)
        lugar = int(digito) * (10 ** (len(a) - indice - 1))
        if lugar != 0:
            resultado += f'{lugar} + '  # Append the place value to the result
    
    # Remove the last ' + ' for cleaner output
    resultado = resultado.rstrip(' + ')
    
    print(f'O número descomprimido é: {resultado}')
else:
    print("O valor inserido não é um número inteiro!")
