'''palavras = list()
while True:
    try:
        frase = input().lower()
        minus = True
        maius = False
        for i in frase:
            if i == ' ':
                print(i, end="")
            elif (minus == True and maius == False):
                print(i.upper(), end="")
                minus = False
                maius = True
            elif (maius == True and minus == False):
                print(i.lower(), end="")
                maius = False
                minus = True

    except EOFError:
        break'''

'''palavras = list()
while True:
    try:
        frase = input().lower()
        for a in frase:
            palavras.append(a)
        for i in range(0, len(palavras), 2):
            if (palavras[i] != ' '):
                palavras[i] = frase[i].upper()
        for b in palavras:
            print(b, end="")

    except EOFError:
        break'''

while True:
    try:
        frase = input().upper()
        fraseNova = ""
        cont = 1
        for palavra in frase:
            if palavra != ' ':
                if cont == 0:
                    fraseNova += palavra.lower()
                    cont = 1
                elif cont == 1:
                    fraseNova += palavra
                    cont = 0
            else:
                fraseNova += ' '
        print(fraseNova)

    except EOFError:
        break

