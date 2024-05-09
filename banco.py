menu = """
------------- MENU -------------
[d] Depositar
[s] Sacar
[e] Visualizar extrato
[q] Sair 
--------------------------------
Digite a opção:
"""

saldo = 0
limite = 500
LIMITE_SAQUE = 3
extrato = ""
numero_saques = 0


while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depositar...")

        deposito = float(input("Digite o valor que deseja depositar: "))
        while deposito < 0:
            deposito = float(input("Digite o valor que deseja depositar: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("Valor adicionado ao saldo!")

    elif opcao == "s":
        print("Sacar...")
        saque = float(input("Digite o valor que deseja sacar: "))

        if saque > saldo:
            print("Operação inválida! Saldo insuficiente!")
        elif saque > limite:
            print("Operação inválida! Valor ultrapassou o limite!")
        elif numero_saques >= LIMITE_SAQUE:
            print("Operação inválida! Números de saques excedido!")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "e":
        print("------------- EXTRATO -------------")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo atual: {saldo:.2f}")

    elif opcao == "q":
        break
    else:
        print("Digite uma opção válida!")
