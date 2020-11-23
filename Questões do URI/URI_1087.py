while True:
    entrada = input().split()
    x1 = int(entrada[0])
    y1 = int(entrada[1])
    x2 = int(entrada[2])
    y2 = int(entrada[3])

    if (x1 + y1 + x2 + y2 == 0):
        break

    linha = x2 - x1
    coluna = y2 - y1

    if(x1 == x2 and y1 == y2):
        print(0)
    elif (x1 == x2 and y1 != y2):
        print(1)
    elif (x1 != x2 and y1 == y2):
        print(1)
    elif (linha == coluna):
        print(1)
    elif(linha == -coluna or -linha == coluna):
        print(1)
    else:
        print(2)
