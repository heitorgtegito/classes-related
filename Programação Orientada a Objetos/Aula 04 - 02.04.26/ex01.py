class Retangulo:
    def __init__(self):
        self.__base = 0
        self.__altura = 0
    def set_base(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__base = valor
    def get_base(self):
        return self.__base
    def set_altura(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__altura = valor
    def get_altura(self):
        return self.__altura
    def diagonal(self):
        return (self.__base **2 + self.__altura **2) ** 0.5

class UI:
    def main():
        x = Retangulo()
        x.set_base(float(input("Digite o valor da base: ")))
        x.set_altura(float(input("Digite o valor da altura: ")))
        print(f'O retângulo de base {x.get_base()} e altura {x.get_altura()}')
        print(f'tem a diagonal: {x.diagonal()}')

UI.main()

"""
Essa ideia de atributos enclausurados é para a proteção dos dados, 
já que se torna impossível de acessa-lós diretamente pelo código principal
"""