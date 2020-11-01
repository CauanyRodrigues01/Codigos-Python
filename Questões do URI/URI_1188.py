operacao = input()

soma = 0
min = 5
max = 7
cont = 0

m = []

for a in range(12):
    linha = []
    for b in range(12):
        numero = float(input())
        linha.append(numero)
    m.append(linha)
    
for c in range(7, 12):
    for d in range(min, max):
        soma = soma + m[c][d]
        cont += 1
    min -= 1
    max += 1

if operacao == "S":
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/cont))
