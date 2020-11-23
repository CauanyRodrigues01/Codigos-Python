diferenca = 0
listaDiferenca = []
while True:
    try:
        entrada = [int(i) for i in input().split()]

        if entrada[0] > entrada[1]:
            diferenca = entrada[0] - entrada[1]
        else:
            diferenca = entrada[1] - entrada[0]

        listaDiferenca.append(diferenca)
        
    except EOFError:
        for i in listaDiferenca:
            print(i)
        break
