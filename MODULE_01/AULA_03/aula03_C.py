#Operadores lógicos em Python
## Utilizados em conjunto com operadores de comparação para montar uma operação lógica
## O operador lógico vai operar em cima do retorno do operador de comparação, ou seja, vai utilizar o valor booleano para operar e vai retornar outro booleano
## Exmplos de retorno das operações booleanas
comp_a = "a"=="a"
comp_b = "b"=="b"
comp_c = "c"=="d"
comp_d = type("c")==type("d")
print(comp_a, comp_b, comp_c, comp_d) # aqui é possível ver o retorno booleano como verdadeiro ou falso
print(comp_a+comp_b) # aqui é possível visualizar o tratamento do valor retornado sendo TRUE = 1
print(comp_a+comp_b+comp_c+comp_d)

# Operador AND
saldo = 500
saque = 600
limite = 100
print(saque <= saldo and saque <= limite)
## true and true = true
## false and false = false
## true and false = false
## false  and true = false

#Operador OR
print(saque <= saldo or saque<= limite+saldo)
## true and true = true
## false and false = false
## true and false = true
## false  and true = true

#Operador NOT
##Nega, ou inverte, o resultado
print(not 1000 > 100)
#true = false
#false = true
lista = []
lista_cheia = [1,2,3]
print(not lista, ", lista vazia") #lista vazia é considerado FALSE
print(not lista_cheia, ", lista cheia") #lista cheia é considerado TRUE
palavra = "string"
palavra_vazia = ""
print(not palavra) # uma string é considerada TRUE
print(not palavra_vazia) # uma string vazia é considerada FALSE
## Sequencias de caracteres ou objetos, quando vazias, são consideradas FALSE e, quando cheias, são consideradas TRUE

#Parênteses
## Define a precedência da operação lógica a ser realizada
## A precdência seque a ordem da esquerda pra direita
print((1>1)or(1>=1))
print((1>1 and 1!=2)and(1>=1))
print((1>1 and 1!=2)or(1>=1))



