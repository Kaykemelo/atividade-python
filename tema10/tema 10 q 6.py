def cifra_de_cesar(mensagem, chave):
    mensagem_criptografada = ""
    for caractere in mensagem:
        deslocamento = 65
    if caractere.isupper()

    else 97 mensagem_criptografada += chr((ord(caractere) - deslocamento + chave) % 26 + deslocamento)

    else:
        mensagem_criptografada += caractere
        return mensagem_criptografada

    #Solicitar a mensagem e a chave do usuario
    mensagem = input("Digite a mensagem a ser criptografada: ")
    chave = int(input("Digite o valor da chave (deslocamento): "))

    #criptografar a mensagem
    mensagem_criptografada = cifra_de_cesar(mensagem , chave)

    #mostrar a mensagem criptografada
    print("A mensagem criptografada é:", mensagem_criptografada)
