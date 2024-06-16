#Identação e blocos
## A identação serve para melhorar  a legibilidade e a manutenbilidade do código
## Em Python, a identação serve para definir os limites dos blocos de código

## A convenção sobre a identação é de deixar quatro espaços em branco (1 tab) da margem a mais pra cada linha daquele código. Exemplo:

def sacar(self, valor:float) -> None: # início do método
    if self.saldo >= valor: # início do bloco if
        self.saldo -= valor # operação
    # fim do if
#fim do método

##Outro exemplo

def sacar(valor):
    valor = int(valor) #necessário fazer a conversão do input para inteiro, pois o tipo de dado recebido pelo programa é string
    saldo = 500
    if saldo >=valor:
        print(f"Saque autotizado de R${valor}")
        
sacar(input("Digite o valor: "))