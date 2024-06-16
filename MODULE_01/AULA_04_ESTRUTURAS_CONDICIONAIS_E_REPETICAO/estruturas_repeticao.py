#Estruturas de Repetição
## São utilizadas para repetir um deerminado bloco de código um número conhecido de vezes ou determinado em tempo de execução ou através de uma expressão lógica

#Comando FOR
## Percorre um objeto iterável
## Usado quando se conhece o numero de vezes de repetição

texto = input("Digite um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
print()

# FOR/ELSE
texto_vazio = ""

for letra in texto_vazio:
    print(letra, end="")

else:  
    print("executa no final do laço")
