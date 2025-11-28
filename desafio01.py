

def show_menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    return input(menu)



# A função saque deve receber os argmentos apenas por nome(keyword only arguments). 
# Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques,limete_saques
# Sugestão de retorno: saldo e extrato
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

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
    return saldo, extrato



# A função depositar deve receber os argmentos apenas por (positional only arguments).
# Sugestão de argumentos: saldo, valor, extrato
# Sugestão de retorno: saldo e extrato
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


# A função extrato deve receber os argumentos apenas por posição e nome (Positional only e keyword only).
# Argumentos posicionais: saldo
# Argumentos por nome: extrato
def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")



# Novas Funções
# Precisamos criar das novas fnções: Criar usário e criar conta corrente.
# Fique a vontade para adicionar novas funções, exmplos: listar usuários, listar contas, etc.



#O programa deve armazenar os suários em uma lista, um usário é composto por :nome, data de nascimento, cpf e endereço. 
# O endereço é ma string com o formato: logradouro, número - bairro - cidade/sigla estado
# Deve ser armazenado somente os nḿeros do CPF.
#Não podemos cadastrar 2 usuários com o mesmo CPF.
def criar_usuario():
    pass

# O programa deve armazenar contas em uma lista, uma conta é composta por :agência, número da conta e o usário.
#O Nmero da conta é sequencial, iniciado em 1.
# O número da agência é fixo: 0001
# O Usuário pode ter mais de uma conta, mas uma conta pertence a apenas um usário.
def criar_conta_corrente():
    pass
  


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3



    while True:
        opcao = show_menu()

        if opcao == "d":
            valor=float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)  
            

        elif opcao == "e":
          extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")





main()