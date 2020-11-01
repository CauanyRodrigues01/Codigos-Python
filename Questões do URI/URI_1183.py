operacao = input()

soma = 0
max = 1
cont = 0

m = []

for a in range(12):
    linha = []
    for b in range(12):
        numero = float(input())
        linha.append(numero)
    m.append(linha)
    
for c in range(12):
    for d in range(max, 12):
        soma = soma + m[c][d]
        cont += 1

    max += 1

if operacao == "S":
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/cont))
