class Pessoa:
    def _init_(self,nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        if isinstance (nome,str) and len(nome) > 0:
            self.__nome = nome
        else:
            print('Nome Invalido')

# Testar a função
abc = Pessoa('Joaqui 5555666n')
print(abc.get_nome())

abc.set_nome('Maria Joaquina')
print(abc.get_nome())

class ContaBancaria:
    def _init_(self, saldo):
        self.__saldo = saldo if saldo >= 0 else 0  # Inicializa o saldo, garantindo que não seja negativo

    # Método para depositar valor na conta
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor depositado inválido")

    # Método para sacar valor da conta
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Valor de saque inválido!")
    
    # Método para obter o saldo atual
    def get_saldo(self):
        return self.__saldo

# Testar código pela entrada de dados
conta = ContaBancaria(1000)  # Inicializa a conta com saldo de 1000
conta.depositar(500)  # Deposita 500 na conta
print(conta.get_saldo())  # Exibe o saldo atual: 1500

conta.sacar(2000)  # Tenta sacar 2000, mas o saldo é insuficiente

print(conta.get_saldo())  # Exibe o saldo atual: 1500