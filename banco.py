menu = """
    ------------- MENU -------------
    [d] Depositar
    [s] Sacar
    [e] Visualizar extrato
    [q] Sair 
    --------------------------------
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
                print("Valor adicionado ao saldo!")

    elif opcao == "s":
        print("Sacar...")
    elif opcao == "e":
        print("Visualizar Extrato...")
    elif opcao == "q":
        break
    else:
        print("Digite uma opção válida!")
