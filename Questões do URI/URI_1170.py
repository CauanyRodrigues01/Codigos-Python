n = int(input())

for i in range(n):
    cont = 0
    ent = float(input())
    while (ent > 1):
        ent = ent/2
        cont += 1

    print(cont, "dias")
