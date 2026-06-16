# Boleto
from enum import Enum
from datetime import datetime
class Boleto: # Aqui algumas coisas não vão ter dados iniciais, até pq ngm recebe um boleto já pago.
    def __init__(self, codBarras, dataEmissao, dataVencimento, valorBoleto):
        self.set_codBarras(codBarras)
        self.set_dataEmissao(dataEmissao)
        self.set_dataVencimento(dataVencimento)
        self.__dataPagto = None
        self.set_valorBoleto(valorBoleto)
        self.__valorPago = 0
        self.__situacaoPagamento = Pagamento.EM_ABERTO

    def set_codBarras(self, codBarras): # Supondo q o código de barra tem 10 dígitos
        if len(codBarras) != 10: raise ValueError()
        else: self.__codBarras = codBarras
    def get_codBarras(self): return self.__codBarras
    
    def set_dataEmissao(self, dataEmissao):
        if dataEmissao > datetime.now(): raise ValueError()
        else: self.__dataEmissao = dataEmissao
    def get_dataEmissao(self): return self.__dataEmissao

    def set_dataVencimento(self, dataVencimento):
        if dataVencimento < datetime.now(): raise ValueError()
        else: self.__dataVencimento = dataVencimento
    def get_dataVencimento(self): return self.__dataVencimento

    def set_valorBoleto(self, valorBoleto):
        if valorBoleto <= 0: raise ValueError()
        else: self.__valorBoleto = valorBoleto
    def get_valorBoleto(self): return self.__valorBoleto
    def get_valorPago(self): return self.__valorPago
    def get_dataPagto(self): return self.__dataPagto

    def pagar(self, valor_pago):
        if valor_pago < 0 or valor_pago > self.__valorBoleto: raise ValueError()
        if self.__situacaoPagamento != Pagamento.EM_ABERTO: raise ValueError()
        self.__valorPago = valor_pago
        self.__dataPagto = datetime.now()
        if self.__valorBoleto == self.__valorPago: self.__situacaoPagamento = Pagamento.PAGO
        else: self.__situacaoPagamento = Pagamento.PAGO_PARCIAL
    def situacao(self): return self.__situacaoPagamento

    def __str__(self):
        return f"Boleto: {self.__codBarras} - Emissão: {self.__dataEmissao} - Data de Vencimento {self.__dataVencimento} - Valor: R${self.__valorBoleto:.2f} - Data de Pagamento: {self.__dataPagto} - Valor Pago: R${self.__valorPago:.2f} - Situação: {self.__situacaoPagamento}"


class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class BoletoUI:
    __boletos = []
    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = BoletoUI.menu()
            if op == 1: BoletoUI.inserir()
            if op == 2: BoletoUI.listar()
            if op == 3: BoletoUI.atualizar()
            if op == 4: BoletoUI.excluir()
            if op == 5: BoletoUI.boletos_em_aberto()
            if op == 6: BoletoUI.boletos_pagos()
            if op == 7: BoletoUI.boletos_a_vencer()
            if op == 8: BoletoUI.boletos_vencidos()
            if op == 9: BoletoUI.pagar_boleto()

    @staticmethod
    def menu():
        print("1-Inserir \n2-Listar \n3-Atualizar \n4-Excluir \n5-Boletos Em Aberto \n6-Boletos Pagos \n7-Boletos A Vencer \n8-Boletos Vencidos \n9-Pagar Boleto \n10-Sair")
        return int(input("Escolha uma opção: "))
    
    @classmethod
    def inserir(cls):
        codBarras = input("Digite o código de barras: ")
        dataEmissao = datetime.strptime(input("Informe a data de emissão: "), "%d/%m/%Y")
        dataVencimento = datetime.strptime(input("Informe a data de vencimento: "), "%d/%m/%Y")
        valorBoleto = float(input("Digite o valor do boleto: "))
        cls.__boletos.append(Boleto(codBarras, dataEmissao, dataVencimento, valorBoleto))

    @classmethod
    def listar(cls):
        if len(cls.__boletos) == 0: print("Não há boletos")
        for i in cls.__boletos: print(i)

    @classmethod
    def atualizar(cls):
        cls.listar()
        codBarras = input("Informe o código de barras: ")
        for i in cls.__boletos:
            if i.get_codBarras() == codBarras:
                cls.__boletos.remove(i)
                dataEmissao = datetime.strptime(input("Informe a data de emissão: "), "%d/%m/%Y")
                dataVencimento = datetime.strptime(input("Informe a data de vencimento: "), "%d/%m/%Y")
                valorBoleto = float(input("Digite o valor do boleto: "))
                novo = Boleto(codBarras, dataEmissao, dataVencimento, valorBoleto)
                cls.__boletos.append(novo)
            else: raise NameError()

    @classmethod
    def excluir(cls):
        cls.listar()
        codBarras = input("Informe o código de barras: ")
        for i in cls.__boletos:
            if i.get_codBarras() == codBarras: cls.__boletos.remove(i)

    @classmethod
    def boletos_em_aberto(cls):
        for i in cls.__boletos:
            if i.situacao() == Pagamento.EM_ABERTO: print(i)

    @classmethod
    def boletos_pagos(cls):
        for i in cls.__boletos:
            if i.situacao() == Pagamento.PAGO or i.situacao() == Pagamento.PAGO_PARCIAL: print(i)

    @classmethod
    def boletos_a_vencer(cls):
        for i in cls.__boletos:
            if i.situacao() == Pagamento.EM_ABERTO and i.dataVencimento > datetime.now(): print(i)

    @classmethod
    def boletos_vencidos(cls):
        for i in cls.__boletos:
            if i.situacao() == Pagamento.EM_ABERTO and i.dataVencimento <= datetime.now(): print(i)

    @classmethod
    def pagar_boleto(cls):
        codBarras = input("Digite o código de barras: ")
        for i in cls.__boletos:
            if i.get_codBarras() == codBarras:
                valor = float(input("Digite o valor que será pago do boleto: "))
                i.pagar(valor)

BoletoUI.main()
