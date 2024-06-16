#Técnica pra retornar substrings informando: início, fim e passo
## [start: stop[,step]]

nome = "Rafael Laroca de Freitas"

print(nome[0]) #retorna a primeira letra da string
print(nome[:6]) # retorna uma substring que começa no índice 0 e vai até o 6
print(nome[7:]) # retorna uma substring que começa no indice 7 e vai ate o final, não é necessário conhecer o tamnho da string
print(nome[7:13]) #retorna uma substring delimitada pelos indices 7  13
print(nome[7:12:2]) # retorna uma substring delimitada trazendo os itens com intervalos de 2 unidades
print(nome[:]) # retorna toda a string
print(nome[::-1]) #retorna toda a substring completamente invertida (espelhada)
print(nome[-1]) #retorna o último item da string, conforme se itera o valor para menos, vai retornando os itens de forma decrescente no indice