import json
class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"
    def to_json(self): # Transforma em dict games
        return {"id": self.id, "nome": self.nome}
    @staticmethod
    def from_json(dict):
        return Cliente(dict["id"], dict["nome"])

def salvar():
    a = Cliente(1, "Douglas")
    b = Cliente(2, "Jon")
    c = Cliente.from_json({ "id" : 3, "nome" : "Alan Turing" })

    lista = [a,b,c]
    arquivo = open("clientes.json", mode="w")
    json.dump(lista, arquivo, default = Cliente.to_json, indent= 2)
    arquivo.close()

# print(a)
# print(b)
# print(c)
# # Tanto o .__dict__ quanto o vars() transformam o bagulho em dict mas normalmente dão b.o em alguma parada
# print(a.__dict__)
# print(b.__dict__)
# print(vars(a))
# print(vars(b))
# print(a.to_json())
# print(b.to_json())
# print(c.to_json())

def abrir():
    arquivo = open("clientes.json", mode="r")
    list_dict = json.load(arquivo)
    arquivo.close()
    for i in list_dict: 
        x = Cliente.from_json(i)
        print(x)
salvar()
abrir()