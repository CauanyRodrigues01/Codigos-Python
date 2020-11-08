while True:
    try:
        dic = {}
        saida = []
        n = int(input())

        for a in range(n):
            carne, validade = [b for b in input().split(" ")]
            validade = int(validade)
            dic[carne] = validade

        for c in sorted(dic, key=dic.get):
            saida.append(c)

        print(*saida)
        
    except EOFError:
        break
