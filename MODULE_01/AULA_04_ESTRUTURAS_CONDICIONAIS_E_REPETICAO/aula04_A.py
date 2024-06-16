#Estruturas condicionais e repetição em Python

##Estruturas condicionais permitem o desvio do fluxo de controle do código quando determinadas expressões lógicas são atendidas

# IF - estrutura condicional simples
## Executa o bloco de código caso a expressão lógica retorne verdadeira (TRUE).Exemplo
saldo = 2000 
saque = float(input("Digite o valor desejado: "))

if saque<=saldo:
    print(f"Saque autorizado de R${saque}")

if saque>saldo:
    print(f"Saque de R${saque} não autorizado")


# IF/ELSE
## Cria uma estrutura condicional com dois desvios
## Se a condição testada retornar TRUE o bloco IF é executado
## Caso a condição testada retorne FALSE, o bloco ELSE é executado
if saque<=saldo:
    print(f"Saque autorizado de R${saque}")
else:
    print(f"Valor de R${saque} não autorizado")


#ELIF
## Usado quando se quer mais de dois desvios de fluxo no código
## Testa a condição novamente e caso retorne TRUE, executa o seu bloco de código
opcao = input("Digite uma opção \n [1] para sacar \n [2] para ver o saldo \n")

if opcao != 1 or opcao!=2:
    opcao =0
else:
    opcao=int(opcao)

if opcao==1:
    print(f"Painel de saque")
elif opcao==2:
    print(f"painel de saldo")
else:
    print(f"Exit")