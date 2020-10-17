while True:
    m, n = input().split(" ")
    if m == '0' and n == '0':
        break
    soma = int(m) + int(n)
    resultado = int(str(soma).replace("0", ""))
    print(resultado)
