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

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depositar...")
    elif opcao == "s":
        print("Sacar...")
    elif opcao == "e":
        print("Visualizar Extrato...")
    elif opcao == "q":
        break
    else:
        print("Digite uma opção válida!")
