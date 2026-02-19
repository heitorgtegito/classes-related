from random import shuffle
from random import choice

disponiveis = ' ☺ ☻ ♥ ♦ ♣ ♠ • ○ ◙ ▬ ↨ ♪ ♫ ☼ ► ◄ ↕ ‼ ¶ § ⌂ ↨ ↑ ↓ '.split() # Vai pegar e vai transformar essa string numa lista
shuffle(disponiveis) # Embaralha a string
print(disponiveis) # Só pra eu ver como tá 
pilha = disponiveis[0:24] # Pilha de caracteres é uma lista copiada de todas as peças (por algum motivo se não especificar o 0:24 ele bota só 50% da lista)
linha1_simbolos = disponiveis[0:6] # 1º linha
linha2_simbolos = disponiveis[6:12] # 2º Linha 
linha3_simbolos = disponiveis[12:18] # 3º linha
linha4_simbolos = disponiveis[18:24] # 4º linha

grade_simbolos = [
    (linha1_simbolos),
    (linha2_simbolos),
    (linha3_simbolos),
    (linha4_simbolos)
]

# grade = '''
# -------------------------
# | ? | ? | ? | ? | ? | ? |
# -------------------------
# | ? | ? | ? | ? | ? | ? |
# -------------------------
# | ? | ? | ? | ? | ? | ? |
# -------------------------
# | ? | ? | ? | ? | ? | ? |
# -------------------------
# '''
# Essa mega string aí é a grade visivel pro jogador
peça = choice(pilha) # Escolhe uma peça aleatória
pilha.remove(peça) # Remove ela da pilha
print(grade_simbolos)
print(f'Busque o par de: {peça}') # Mostra pro jogador qual a peça q ele tem q buscar
#acho q o meta é usar o grade_simbolos pra mexer na grade em si tlgd