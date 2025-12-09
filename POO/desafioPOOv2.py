from abc import ABC, abstractmethod, abstractproperty
import textwrap
from datetime import datetime


class Conta:
    def __init__(self,numero,Cliente ):
        _saldo = 0
        _numero = numero
        _agencia = "0001"
        _cliente = Cliente
        _historico = Histórico()
    @property    
    def saldo():
        return _saldo
    @property
    def numero():
        return _numero
    @property
    def agencia():
        return _agencia
    @property
    def cliente():
        return _cliente
    @property
    def historico():
        return _historico   
    
    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(numero,cliente)

    def sacar(self,valor):
        excedeu_saldo = valor > self._saldo
        #excedeu_limite = valor > self._limite
        #excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        #elif excedeu_limite:
        #    print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        #elif excedeu_saques:
        #    print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False
        
    def depositar(self,valor):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

class ContaCorrente(Conta):
    def __init__(self,numero,cliente, limite=500, limite_saques=3):
        super().__init__(numero,cliente )
        _limite = limite
        _limite_saques = limite_saques
        
    def sacar(self, valor):
        #verificar se o saque é possível dentro do limite
        number_saques = 0
        for i in range(self.historico.transacoes.length(),0,-1):
            if self.historico.transacao.tipo == 'Saque':
                number_saques +=1
        
        excedeu_limite = valor > self._limite
        execedeu_saques = number_saques >= self._limite_saques
        
        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False
        
        elif number_saques >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False
        #registrar o saque no histórico de transações
        else:
            return super().sacar(valor)
        return False        

    def __str__(self):
        return super().__str__() + f"\nLimite: {self._limite}\nLimite Saques: {self._limite_saques}"

class Cliente():
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
    def realizar_transacao(conta ,transacao):
        transacao.registrar(conta)
    def adicionar_conta(self,Conta):
        self._contas.append(Conta)
    def __str__(self):
        return f" \nEndereço: {self._endereco}"


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento,endereco):
        super().__init__(endereco)
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._nome = nome
    @property
    def cpf(self):
        return self._cpf
    
    def __str__(self):
        return  f"\nNome: {self._nome}\nCPF: {self._cpf}\nData de Nascimento: {self._data_nascimento}" + super().__str__()



class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractmethod
    def registrar(Conta):
        pass



class Deposito(Transacao):
    def __init__(self,valor):
        _valor = valor
    @property
    def valor(self):
        return _valor
    
    def registrar(self,conta):
        sucesso_transacao = conta.depositar(self._valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self,valor):
        _valor = valor
    @property
    def valor(self):
        return _valor
    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self._valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Histórico:
    def __init__(self):
        self._transacoes = []
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )













































def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [lcc]\tListar clientes cadastrados
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_clientes(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append(PessoaFisica(cpf, nome, data_nascimento, endereco))

    #cliente.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def listar_clientes_cadastrados(clientes: list[Cliente]):
    print("\n=== Lista de Clientes Cadastrados ===")
    for cliente in clientes :
        print(cliente)



def main():

    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_clientes(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "lcc":
            listar_clientes_cadastrados(clientes)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
