listaCodigos = []
codigo = []

while True:
    try:
        quantLivros = int(input())
        for a in range(quantLivros):
            codigo.append(input())

        codigo.sort()
        for b in codigo:
            listaCodigos.append(b)
        codigo.clear()
        
    except EOFError:
        for c in listaCodigos:
            print(c)
        break
