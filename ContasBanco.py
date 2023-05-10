class ContaCorrente(): #Padrão + usado --> começa com letra maiuscula e separa com letra maiscula

    def __init__(self, nome, cpf, numero,saldo, limite): #init é uma função contrutora, esse método é quem define o que acopntece quando você cria uma instancia da classe
        self.__nome = nome # atributo com 2 underscore é privado
        self.__cpf = cpf
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite

    def estrato(self):
        print("Saldo {0} do titular {1}".format(self.saldo, self.nome))

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__nome
    
    def set_limite(self, limite):
        self.__limite = limite
    
    def get_limite(self):
        return self.__limite
    
conta_cris = ContaCorrente("Cris", "145.254.569-46", 12456, 15.00, 1000)
print(conta_cris.get_titular())

conta_cris.set_limite(10000)
print(conta_cris.get_limite())

class Cliente():
    def __init__(self, nome):
        self.__nome = nome

    '''def get_nome(self):
        return self.nome.title() # retornando o nome com a primiera letra maiuscula'''
    
    @property #posso chamar cliente.nome sem os paranteses
    def nome(self):
        return self.__nome.title()
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

        
       
cliente = Cliente("cris")
cliente.nome = "marco"
print(cliente.nome)