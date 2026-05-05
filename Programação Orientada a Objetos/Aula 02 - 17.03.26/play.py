entrada = input("Digite uma frase\n")
palavras = entrada.split()
for i in range(len(palavras)):
    palavra = palavras[i]
    letras = palavra.split()
    for j in range(len(letras)):
        primeiraletra = letras[j-1]
        letras.append(primeiraletra)
        letras.remove(primeiraletra)
    print(*letras)