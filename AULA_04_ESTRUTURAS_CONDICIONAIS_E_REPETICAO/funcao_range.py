#Função range
## Usada para produzir uma sequência de números inteiros a partir de um inicio inclusivo e para um fim exclusivo
## range(i, j) produz [i+1, i+2, i+4,..., j-1]
## Recebe três argumentos:
### 1 - stop (obrigatório)
### 2 - start (opcional)
### 3 - step (opcional)
## Retorna um objeto "range"

## range(4) retorna um range object com 4 itens sequenciais de 0 a 3. Mas não retorna a lista com os itens, sendo necessário converter o objeto para list:
print("\n")

teste = range(4)
print(teste)

print("\n")

teste_lista = list(teste)
print(teste_lista)

print("\n")

## FOR e RANGE
for n in range(4,11):
    print(n, end=" ")

print("\n")
## STEP
for n in range(0, 51, 5): #o terceiro argumento é o step, define o intervalo entre os numeros da sequência
    print(n, end=" ")

print("\n")