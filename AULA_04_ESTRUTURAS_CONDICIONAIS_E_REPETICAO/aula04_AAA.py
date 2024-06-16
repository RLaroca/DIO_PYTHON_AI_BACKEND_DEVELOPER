# IF ternário
## Permite testar uma condição em uma única linha
## É composto por trÊs partes
### 1 - Retorno, caso a expressão seja veradeira
### 2 - expressão lógica
### 3 - retorno caso a expressão seja falsa

saldo = 500
saque = int(input("Digite o valor: "))

status = "Sucesso" if saque<=saldo else "Falha"

print(f"{status} ao realizar o saque")