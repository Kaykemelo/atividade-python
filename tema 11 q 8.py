# Recebimento de valores 
numero = int(input("Digite um valor inteiro:"))

# Convertendo de valor inteiro para string
numeroInvertido = str(numero)[::-1]


# Verificando o Palindromo 

print("")

if numeroInvertido == str(numero):
    print(str(numero)+ "O numero é um palindromo" + str (numeroInvertido) +".")
    
else:
    print(str(numero) + "O numero não é palindromo")    