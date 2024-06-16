#String
## Rica em métodos e é fácil de trabalhar

texto = "   lingua De PROGRAMAÇÃO PyThOn    "
##Maiúscula:
print(texto.upper())

##Minúscula:
print(texto.lower())

##Título
print(texto.title())

##STRIP

print(texto.lstrip())
print(texto.rstrip())
print(texto.strip())

##CENTER e JOIN
print(texto.center(50,"#"))
print(".".join(texto))