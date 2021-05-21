class Pessoa:
    def __init__(self):
        self.__Nome = None
        self.__Email = None
        self.__Telefone = None
        self.__Endereco = None

    @property
    def Nome(self):
        return self.__Nome

    @Nome.setter
    def Nome(self, nome):
        self.__Nome = nome

    @property
    def Email(self):
        return self.Email

    @Email.setter
    def Email(self, email):
        self.__Email = email

    @property
    def Telefone(self):
        return self.Telefone

    @Telefone.setter
    def Telefone(self, telefone):
        self.__Telefone = telefone

    @property
    def Endereco(self):
        return self.Endereco

    @Endereco.setter
    def Endereco(self, endereco):
        self.__Endereco = endereco

    def mostrar_dados(self):
        return f'Nome: {self.__Nome} \nEmail: {self.__Email} ' \
               f'\nTelefone: {self.__Telefone} \nEndereço: {self.__Endereco}\n'


class Cliente(Pessoa):
    """ Cliente herda de Pessoa """

    def __init__(self):
        Pessoa.__init__(self)
        self.__Id_cliente = None
        self.__Cpf_cnpj = None
        self.__Limite_Credito = None
        self.__Cartao_Credito = None
        self.__Status = None

    @property
    def Id_cliente(self):
        return self.__Id_cliente

    @Id_cliente.setter
    def Id_cliente(self, id_cliente):
        self.__Id_cliente = id_cliente

    @property
    def Cpf_cnpj(self):
        return self.__Cpf_cnpj

    @Cpf_cnpj.setter
    def Cpf_cnpj(self, cpf_cnpj):
        self.__Cpf_cnpj = cpf_cnpj

    @property
    def Limite_Credito(self):
        return self.__Limite_Credito

    @Limite_Credito.setter
    def Limite_Credito(self, limite):
        self.__Limite_Credito = limite

    @property
    def Cartao_Credito(self):
        return self.__Cartao_Credito

    @Cartao_Credito.setter
    def Cartao_Credito(self, cartao_credito):
        self.__Cartao_Credito = cartao_credito

    @property
    def Status(self):
        return self.__Status

    @Status.setter
    def Status(self, status):
        self.__Status = status

    def Verificar_Credito(self):
        if self.__Limite_Credito > 0:
            print('Saldo Positivo')
        else:
            print('Saldo Negativo')

    def Validar_Cartao(self):
        if self.__Status == 'Ok':
            print('Cartão Valido')
        else:
            print('Cartão Invalido')


class Funcionario(Pessoa):
    """ Funcionario herda de Pessoa """

    def __init__(self):
        Pessoa.__init__(self)
        self.__Id_funcionario = None
        self.__Cargo = None
        self.__Salario = None

    @property
    def Id_funcionario(self):
        return self.__Id_funcionario

    @Id_funcionario.setter
    def Id_funcionario(self, id_funcionario):
        self.__Id_funcionario = id_funcionario

    @property
    def Cargo(self):
        return self.__Cargo

    @Cargo.setter
    def Cargo(self, cargo):
        self.__Cargo = cargo

    @property
    def Salario(self):
        return self.__Salario

    @Salario.setter
    def Salario(self, salario):
        self.__Salario = salario


cliente = Cliente()
cliente.Nome = "Marcos Vinicius"
cliente.Email = 'marcosvsatil@gmail.com'
cliente.Telefone = 62996324157
cliente.Endereco = 'Rua 2 - Goiás'
cliente.Status = 'Ok'
cliente.Limite_Credito = 1000

print(cliente.mostrar_dados())
cliente.Verificar_Credito()
cliente.Validar_Cartao()