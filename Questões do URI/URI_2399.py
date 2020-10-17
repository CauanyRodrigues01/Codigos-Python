n = int(input())

tabuleiro = []

for i in range(n):
    celula = int(input())
    tabuleiro.append(celula)
minas = []
for i in range(n):
    if (i == 0 and n > 1):
        minas.append(rabuleiro[i]+rabuleiro[i+1])
    elif (i > 0 and i < n-1):
        minas.append(tabuleiro[i-1] + tabuleiro[i] + tabuleiro[i+1])
    elif (n == 1):
        minas.append(tabuleiro[i])
    else:
        minas.append(tabuleiro[i] + tabuleiro[i-1])
for j in minas:
    print(j)
