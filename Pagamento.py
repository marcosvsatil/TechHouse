from abc import ABC, abstractmethod


class Compra(object):
    """ Compra do cliente. """
    ID = 0

    def __init__(self, loja):
        """ Cria a compra do cliente. """
        self.nome_da_loja = loja
        Compra.ID += 1
        self.id_nota_fiscal = Compra.ID

    def modifica_valor(self, valor):
        """ Modifica o valor da compra. """
        self.valor_total = valor

    @property
    def nota_fiscal(self):
        """ Pega informações da nota fiscal. """
        informacao = "Nota fiscal n° {0}\nLoja: {1}\nValor: {2}\n".format(
            str(self.id_nota_fiscal),
            self.nome_da_loja,
            str(self.valor_total))
        return informacao


class Pagamento(ABC):
    """ Classe abstrata que cria as formas de pagamento. """

    @abstractmethod
    def processa_compra(self, compra):
        """ Processa a compra """
        pass


class Boleto(Pagamento):
    """ Pagamento com boleto bancario. """

    def processa_compra(self, compra):
        """ Processa a compra com boleto bancario como forma de pagamento """
        print("Boleto criado!\n" + compra.nota_fiscal)


class CartaoDeCredito(Pagamento):
    """ Pagamento com cartão de crédito. """

    def processa_compra(self, compra):
        """ Processa a compra utilizando cartão de crédito como forma de pagemento. """
        print("Cartão de credito aceito!\n" + compra.nota_fiscal)


class CartaoDeDebito(Pagamento):
    """ Pagamento utilizando cartão de debito. """

    def processa_compra(self, compra):
        """ Processa a compra utilizando cartão de debito como forma de pagamento. """
        print("Cartão de debito aceito!\n" + compra.nota_fiscal)


class Loja(object):
    """ Loja onde foi realizada a compra. """

    def __init__(self, nome):
        """ Cria a loja. """
        self.nome_da_loja = nome

    def executa_compra(self, valor, forma_de_pagamento):
        """ Executa a compra. """
        compra = Compra(self.nome_da_loja)
        compra.modifica_valor(valor)
        forma_de_pagamento.processa_compra(compra)


tech_house = Loja("Tech House")
tech_house.executa_compra(999.00, CartaoDeCredito())
tech_house.executa_compra(49.90, Boleto())
tech_house.executa_compra(99.00, CartaoDeDebito())