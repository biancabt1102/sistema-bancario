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

def valor_invalido(valor):
    if valor < 0:
        print("Digite um valor válido!")
        return True


while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depositar...")

        valor = float(input("Digite o valor que deseja depositar: "))
        while valor_invalido(valor):
            valor = float(input("Digite o valor que deseja depositar: "))
            if valor > 0:
                saldo += valor
                extrato = f"Depósito: R$ {valor:.2f}\n"
                print("Valor adicionado ao saldo!")

    elif opcao == "s":
        print("Sacar...")
        saque = float(input("Digite o valor que deseja sacar: "))
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if saque > saldo:
            print("Operação inválida! Saldo insuficiente!")
        elif saque > limite:
            print("Operação inválida! Valor ultrapassou o limite!")
        elif numero_saques >= LIMITE_SAQUE:
            print("Operação inválida! Números de saques excedido!")
        elif saque > 0:
            saldo -= saque
            extrato = f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "e":
        print("Visualizar Extrato...")
    elif opcao == "q":
        break
    else:
        print("Digite uma opção válida!")
