#CONVERSÃO DE TIPOS DE VARIÁVEIS

#String para inteiro
preco = "22"
preco = int(preco)
print(preco)

#Float para inteiro
valor = 10.9
valor = int(valor) #corta os decimais
print(valor)

#Inteiro para float
numero = 11
numero = float(numero)
print(numero)

# O resultado de uma divisão retorna um float
divisao = 10/2
print(divisao)
## Para retornar u inteiro se utilza barra dupla //
divisao_inteira = preco//3
print(divisao_inteira)

#Existem casos em que uma conversão não é possívele o Python ira lançar um erro:
##Converter uma cadeia de caracteres (string) em float:
#name = "rafael"
#name = float(name)
#print(name)

#Para verificar o typo da variável se utiliza type()
print(type(100.0))

# Utilizando a conversão antes da operação ja retorna o tipo esperado.
print((int(10/3)))