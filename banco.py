import textwrap

saldo = 0
limite = 500
LIMITE_SAQUE = 3
extrato = ""
numero_saques = 0
AGENCIA = "0001"
usuarios = []
contas = []

def menu():
    menu = """
    ------------- MENU -------------
    [d]\t\tDepositar
    [s]\t\tSacar
    [e]\t\tExtrato
    [nu]\tNovo usuário
    [nc]\tNova conta
    [lc]\tListar contas
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

def sacar(*, saque, saldo, limite, numero_saques, limite_saques, extrato):
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

def exibir_extrato(saldo, /, *, extrato):
    print("------------- EXTRATO -------------")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"Saldo atual: {saldo:.2f}")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente os números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")


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
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        print("Criando novo usuário...")
        criar_usuario(usuarios)

    elif opcao == "nc":
        print("Criando nova conta...")
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "lc":
        print("Listar contas...\n")
        listar_contas(contas)

    elif opcao == "q":
        break
    else:
        print("Digite uma opção válida!")
