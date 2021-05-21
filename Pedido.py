from abc import ABC, abstractmethod
from datetime import date


class Pedido(object):
    """ Classe responsável pelos pedidos. """

    def __init__(self, cliente, valor):
        """ Cria um pedido. """
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data = None

    def pagamento(self):
        """ Paga o pedido. """
        self.__status = 'PAGO'
        print("O pedido do cliente", self.cliente, "foi pago.")

    def finaliza(self):
        """ Finaliza o pedido. """
        self.__data = date.today()
        self.__status = 'ENTREGUE'
        print("O pedido do cliente", self.cliente, "foi entregue na data", self.data_finalizacao)

    @property
    def cliente(self):
        """ Pega o cliente do pedido. """
        return self.__cliente

    @property
    def valor(self):
        """ Pega o valor do pedido. """
        return self.__valor

    @property
    def status(self):
        """ Pega o status do pedido. """
        return self.__status

    @property
    def data_finalizacao(self):
        """ Pega a data de finalização do pedido. """
        return self.__data


class CriarPedido(ABC):
    """ Classe abstrata para criar um pedido. """

    @abstractmethod
    def executa(self):
        """ Executa o pedido. """
        pass


class FinalizarPedido(CriarPedido):
    """ Conclui o pedido. """

    def __init__(self, pedido):
        """ Cria o comando concluir e insere o pedido na qual o comando irá agir. """
        self.__pedido = pedido

    def executa(self):
        """ Executa o comando para concluir o pedido.  """
        self.__pedido.finaliza()


class PagarPedido(CriarPedido):
    """ Paga o pedido. """

    def __init__(self, pedido):
        """ Paga e insere o pedido na qual irá agir. """
        self.__pedido = pedido

    def executa(self):
        """ Executa o pagamento do pedido. """
        self.__pedido.pagamento()


class Comandos(object):
    """ Fila de comandos. """

    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()


pedido1 = Pedido('Marcos', 200)
pedido2 = Pedido('Beatriz', 400)

teste = Comandos()

comando1 = FinalizarPedido(pedido1)
comando2 = PagarPedido(pedido1)
comando3 = FinalizarPedido(pedido2)

teste.adiciona(comando1)
teste.adiciona(comando2)
teste.adiciona(comando3)

teste.processa()
