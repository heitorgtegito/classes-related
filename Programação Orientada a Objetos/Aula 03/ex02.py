class Triangulo:
    def __init__(self):
        self.b = 0 # Atributo
        self.h = 0 # Atributo
        pass
    def calc_area(self): # Método
        return self.b * self.h /2

x = Triangulo()
x.b = float(input("Informe a base do triângulo\n"))
x.h = float(input("Informe a altura do triângulo\n"))
print(x.b, x.h)

a = x.calc_area()
print(f"A área do triângulo é {a:.2f}")


y = Triangulo()
y.b = float(input("Informe a base do segundo triângulo\n"))
y.h = float(input("Informe a altura do segundo triângulo\n"))
print(y.b, y.h)

a = y.calc_area()
print(f"A área do segundo triângulo é {a:.2f}")
