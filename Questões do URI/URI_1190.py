operacao = input()

soma = 0
min = 11
cont = 0

m = []

for a in range(12):
    linha = []
    for b in range(12):
        numero = float(input())
        linha.append(numero)
    m.append(linha)
    
for c in range(1, 11):
    for d in range(min, 12):
        soma = soma + m[c][d]
        cont += 1
    if c < 5: 
        min -= 1
    if c > 5:
        min += 1

if operacao == "S":
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/cont))
