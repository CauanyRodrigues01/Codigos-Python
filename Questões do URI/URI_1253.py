casosTeste = int(input())

for  i in range(casosTeste):
    mensagem = input()
    quant = int(input())
    novaMensagem = ""
    for j in mensagem:
        posicao = ord(j) - quant

        if posicao < 65:
            novaMensagem += chr(91 - (65 - posicao))
        else:
            novaMensagem += chr(posicao)     
    print(novaMensagem)
