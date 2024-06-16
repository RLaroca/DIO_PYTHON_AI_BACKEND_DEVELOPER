
nome = "Rafael"
idade = 35
lingua = "Python"

pessoa = {"nome":"rafael", "idade":35, "lingua":"Python"}

# Old Style com %  (não é mais utilizado em Python 3, lembra um pouco como é em C)
print("Meu nome é %s, tenho %d anos e estudo %s"%(nome, idade, lingua))

#format - evolução do old style
print("Meu nome é {}, tenho {} anos e estudo {}.".format(nome, idade, lingua)) #preenche as variáveis na sequência da indexação passada no parâmetro, fica como no print abaixo:
print("Meu nome é {0}, tenho {1} anos e estudo {2}.".format(nome, idade, lingua)) 
#para ordenor a posição das variáveis:
print("Tenho {1} anos, meu nome é {0} e estudo {2}.".format(nome, idade, lingua)) #nessa formatação é possível reutilizar as variáveis em posições diferentes
print("Meu nome é {nome}, tenho {idade} anos e estudo {lingua}.".format(nome=nome, idade=idade, lingua=lingua)) #aqui é possível trabalhar melhor de forma visual com as variáveis, mas nota-se que ao código fica mais extenso
print("Meu nome é {nome}, tenho {idade} anos e estudo {lingua}.".format(**pessoa)) #Usando um dicionário

# F STRING
print(f"Meu nome é {nome}, tenho {idade} anos e estudo {lingua}.") #melhor forma visual e flexibildiade
## Uma desvantagem (não tão problemática) é ter que passar a variável novamente durante o texto quando se quer exibir o conteúdo mais de uma vez, o que na verdade melhora a visibilidade
## Formatação de casas decimais:
pi = 3.14159
print(f"pi é {pi:.2f}")
###Formatação de casas de unidade
print(f"pi é: {pi:10.2f}") # poe 11 unidades a frente da variável