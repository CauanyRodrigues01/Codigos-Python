numEntrada = int(input())
for e in range(numEntrada):
    entrada = input().split()
    pa = int(entrada[0])
    pb = int(entrada[1])
    g1 = float(entrada[2])
    g2 = float(entrada[3])
    anos = 0
    while True:
        pa += int((g1/100) * pa)
        pb += int((g2/100) * pb)
        anos += 1
        
        if pa > pb or anos > 100:
            break
    if anos <= 100:
            print(anos,"anos.")
    else:
        print("Mais de 1 seculo.")
