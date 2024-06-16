saldo = 0
limite_diario = 3
limite_saque = 500
extrato = ""

menu = f"""
############ MENU ############
Digite uma opcão:
[1] - SAIR
[2] - DEPOSITAR
[3] - SACAR
[4] - EXTRATO

##############################
"""

while True:
    opcao = int(input(menu))
    if opcao < 0 or opcao >4:
        print("Escolha uma opção válida.")
    elif opcao ==1:
        print("Obrigado por utilizar nosso sistema!")
        break
    elif opcao == 2:
        valor = int(input("Digite o valor para depositar: R$"))
        if valor>0:
            saldo += valor
            extrato += f"Deposito realizado: +R${valor:.2f}\n"
            print(f"Saldo atualizado: R${saldo:.2f}")
        else:
            print("Operação cancelada: Entre com um valor válido.")
    elif opcao == 3:
        valor = int(input("Digite o valor para sacar: "))
        if valor<0 or valor>saldo or valor>limite_saque or limite_diario==0:
            print("Saque não permitido, tente outro valor")
        else:
            saldo -= valor
            limite_diario -=1
            extrato += f"Saque realizado: -R${valor:.2f}\n"
            print(f"Saldo atualizado R${saldo:.2f}")
    elif opcao ==4:
        show_extrato = f"""
            ######### EXTRATO ########
            {extrato}
            --------------------------
            Saldo: R${saldo:.2f}
            Limite de saque: R${limite_saque:.2f}
            Saques disponíveis: {limite_diario}
            ##########################
            """
        print(show_extrato)
