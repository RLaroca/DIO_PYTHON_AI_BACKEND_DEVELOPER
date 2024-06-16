#Condicionais aninhadas
## Pode-se testar condições dentro de outros blocos que testam condições:

opcao = input("Conta Normal [1] \nConta Universitário [2] \n")
if opcao =="1":
    opcao = int(opcao)
elif opcao =="2":
    opcao = int(opcao)
else:
    opcao = 0
    print("Não foi possível realizar a operação")


if opcao ==1:
    saque = int(input("Digite o valor desejado: "))
    saldo =500
    especial =100
    if saldo >= saque:
        print("ok")
    elif saque <= (saldo+especial):
        print("ok, com cheque especial")
    else:
        print("Não foi possível completar a operação")
elif opcao==2:
    saque = int(input("Digite o valor desejado: "))
    saldo =500
    especial =0
    if saldo >= saque:
        print("ok")
    elif saldo < saque:
        print("nao ok")
    else:
        print("Não foi possível completar a operação")