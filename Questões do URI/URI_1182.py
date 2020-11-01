coluna = int(input())
operacao = input()

soma = 0
cont = 0

m = []

for a in range(12):
    linha = []
    for b in range(12):
        numero = float(input())
        linha.append(numero)
    m.append(linha)
    
for c in range(12):
    soma += m[c][coluna]
    cont += 1


if operacao == "S":
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/cont))
