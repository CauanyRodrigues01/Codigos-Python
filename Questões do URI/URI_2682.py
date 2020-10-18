anterior = int(input())
verifica = True
while True:
    try:
        #anterior = entrada1
        prox = int(input())
        if prox < anterior:
            print(anterior + 1)
            verifica = False
            break
        else:
            anterior = prox
    except EOFError:
        break
if verifica:
    print(anterior + 1)
