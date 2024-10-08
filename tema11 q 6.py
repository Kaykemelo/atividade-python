def eh_primo(numero):
    if numero <= 1:
        return False
    
    if numero == 2:
        return True 
    
    if numero % 2 == 0:
        return False
    
    # Percorre apenas os numeros impares
    for i in range(3,numero // 2 + 1, 2):
        if numero % i == 0:
            return False 
        
        return True
    
    Try:
        numero = int(input("Digite um numero inteiro:"))
        if eh_primo(numero):
            print(str(numero) + "é um numero primo!")
        else:
            print(str(numero) + "nao é um numero primo.")
            
        Except valueError:
            print("por favor, digite um numero inteiro válido.")
               
            