import textwrap

saldo = 0
limite = 500
LIMITE_SAQUE = 3
extrato = ""
numero_saques = 0

def menu():
    menu = """
    ------------- MENU -------------
    [d]\t\tDepositar
    [s]\t\tSacar
    [e]\t\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\t\tSair 
    --------------------------------
    Digite a opção:
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Valor adicionado ao saldo!")
    return saldo, extrato

def sacar(saque, saldo, limite, numero_saques, limite_saques, extrato):
    if saque > saldo:
        print("Operação inválida! Saldo insuficiente!")
    elif saque > limite:
        print("Operação inválida! Valor ultrapassou o limite!")
    elif numero_saques >= limite_saques:
        print("Operação inválida! Números de saques excedido!")
    elif saque > 0:
        saldo -= saque
        extrato += f"Saque: R$ {saque:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido")

def exibir_extrato(extrato, saldo):
    print("------------- EXTRATO -------------")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"Saldo atual: {saldo:.2f}")

while True:
    opcao = menu()

    if opcao == "d":
        print("Depositar...")

        deposito = float(input("Digite o valor que deseja depositar: "))
        while deposito < 0:
            deposito = float(input("Digite o valor que deseja depositar: "))

        saldo, extrato = depositar(saldo, deposito, extrato)

    elif opcao == "s":
        print("Sacar...")
        saque = float(input("Digite o valor que deseja sacar: "))

        saldo, extrato = sacar(
            saque=saque,
            saldo=saldo,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUE,
            extrato=extrato)

    elif opcao == "e":
        exibir_extrato(extrato, saldo)

    elif opcao == "q":
        break
    else:
        print("Digite uma opção válida!")
