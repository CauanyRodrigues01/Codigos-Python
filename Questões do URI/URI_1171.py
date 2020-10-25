loops = int(input())
entradas = dict()

for a in range(loops):
    chave = int(input())
    if (chave in entradas):
        entradas[chave] += 1
    else:
        entradas[chave] = 1

chaves = entradas.keys()
chaves = sorted(chaves)
for b in chaves:
    print(b,"aparece", entradas[b], "vez(es)")
