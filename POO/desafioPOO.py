menuUsuario = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


menuInicial = """

[1] Cadastrar usuário
[2] Cadastrar conta corrente
[3] Monstrar usuários cadastradas
[4] Mostrar contas cadastradas
[5] Acessar conta
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []


#Primeira parte do problema: Criar as funções para as operações existentes:Sacar, Depositar e Visualizar extrato
def sacar(valor):
    global saldo
    global extrato
    global numero_saques 


    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")



def depositar(valor):
    global saldo
    global extrato 
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return


def visualizar_historico_extrato():
    global saldo
    global extrato 
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")     



#Segnda parte do problema: Criar as funções para criar usuário e criar conta bancária corrente
class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
class ContaCorrente:
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario



def cadatrar_usuario():
    nome = (input("Informe o nome do usuário: "))
    data_nascimento = (input("Informe a data de nascimento do usuário (dd-mm-aaaa): "))
    cpf = (input("Informe o CPF do usuário (somente números): "))
    endereco = (input("Informe o endereço do usuário (logradouro, número - bairro - cidade/sigla estado): "))
    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def cadastrar_conta():
    cpf_do_usuario = input("Informe o cpf do usuário para associar a conta: ")
    for usuario in usuarios:
        if usuario.cpf == cpf_do_usuario:
            numero_conta = len(contas) + 1
            conta = ContaCorrente("0001", numero_conta, usuario)
            contas.append(conta)
            print("Conta criada com sucesso!")
            return
    print("Usuário não encontrado. Cadastre um usuario primeiro. Conta não criada.")









while True:
    opcao = input(menuInicial)
    if opcao == "1":
        cadatrar_usuario()
    elif opcao == "2":
        cadastrar_conta()
    elif opcao == "3": #mostrar usuários cadastrados
        for usuario in usuarios:
            print(f"Nome: {usuario.nome}, Data de Nascimento: {usuario.data_nascimento}, CPF: {usuario.cpf}, Endereço: {usuario.endereco}")
    elif opcao == "4": #mostrar contas cadastradas
        for conta in contas:
            print(f"Agência: {conta.agencia}, Número da Conta: {conta.numero_conta}, Titular: {conta.usuario.nome}")
    elif opcao == "5":
        print("Acessando conta...")
        while True:

            opcao = input(menuUsuario)
            if opcao == "d":
                valor = float(input("Informe o valor do depósito: "))
                depositar(valor)
                
            elif opcao == "s":
                valor = float(input("Informe o valor do saque: "))
                sacar(valor)

            elif opcao == "e":
                visualizar_historico_extrato()

            elif opcao == "q":
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
                break


    elif opcao == "0":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

