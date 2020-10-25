loops = int(input())

for a in range(loops):
    troco = 0
    maxProdutos = 0

    money, quantProdutos = [int(i) for i in input().split(" ")]
    valoresProdutos = [float(i) for i in input().split(" ")]

    for b in valoresProdutos:
        soma = b
        totalProdutos = 1

        while soma + b <= money:
            soma += b
            totalProdutos += 1

        if (money - soma) > troco:
            maxProdutos = totalProdutos
            troco = money - soma
    print("{:.2f}".format(troco))
