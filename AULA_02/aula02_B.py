# VARIÁVEIS
#Variáveis em python podem ser declaradas da seguinte maneira:
name="rafael"
age=35

#forma agrupada:
name1, age1 = ("rafael_2", "35_2")

print(age, name, name1, age1)

#Para usar a impressão foramtada com as variáveis:

print(f'Meu nome é {name}, tenho {age} anos')

#para mudar o valor da variável, basta atribuir o novo valor:

name = "Roberto"

print(f'Meu nome agora é {name}')

#CONSTANTES
## O valor da constante permanece o mesmo até o fim da execução do código, o valor é imutável
##Python não tem constantes é necessário utilizar algum mecanismo para tornar um valor imutável
## Por convenção, a fim de comunicar que uma variável é imutável se declara ela com letras maiúsculas

#BOAS PRÁTICAS
## Utiizar snake case: snake_Case
## EScolher nomes sugestivos
## Nome de constantes todo em maiúsculo
