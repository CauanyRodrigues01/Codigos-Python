loops = int(input())
c = 0
e = 0
cont = 0
for a in range(loops):
    tempo = input().split()
    if (tempo[0] == "chuva"):
        cont  -= 1
        if (c < -cont):
            c = -cont
    if (tempo[1] == "chuva"):
        cont += 1
        if (e < cont):
            e = cont

print(c, e)
