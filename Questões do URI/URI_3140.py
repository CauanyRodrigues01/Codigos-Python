verifica = 0
while True:
    try:
        linha = input()
        if "<body>" in linha:
            verifica = 1
        if "</body>" in linha:
            verifica = 0
        if verifica == 1 and "<body>" not in linha:
            print(linha)
    except EOFError:
        break
