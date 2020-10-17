num = 0
verifica = True
while True:
    try:
        aux = num
        num = int(input())
        if verifica:
            if num <= aux:
                print(aux+1)
                verifica = False
    except EOFError:
        break
