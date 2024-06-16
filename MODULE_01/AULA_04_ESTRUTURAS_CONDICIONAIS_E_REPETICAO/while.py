# Comando WHILE
##Repete um bloco de códigos diversas vezes
## Utilizado quando não sabemos o numero de vezes, sendo que esse numero depende de algum evento
## Testa a condição e caso true, executa o bloco e testa novamente a condição
## Quando o teste reorna FALSE, pode ser usado um ELSE para finalizar o bloco e a repetição.

opcao = -1

while opcao != 0:
    opcao = int(input("Digite 1 ou 2 par operações \n Digite 0 para sair: "))
    if opcao == 1:
        print("saque")
    elif opcao ==2:
        print("saldo")
else: 
    print("Obrigado por usar nosso sistema")


#BREAK E CONTINUE
## O comando break para a execução do bloco de código quando a condição é satisfeita
## O comando continue pula a execução quando a condição é satisfeita

while True:
    numero = int(input("Digite um número:   "))
    if numero == 10:
        print("Saindo do sistema")
    
        break

for num in range(100):
    if num%2==0:
        continue

    print(num)