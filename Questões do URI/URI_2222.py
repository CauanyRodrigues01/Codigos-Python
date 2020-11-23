loops = int(input())
for i in range(loops):
    conjuntos = []

    for j in range(int(input())):
        conjuntos.append(set(input().split()[1:]))

    for j in range(int(input())):
        q = input().split()
        c1 = conjuntos[int(q[1]) - 1]
        c2 = conjuntos[int(q[2]) - 1]

        if q[0] == '1':
            print(len(c1.intersection(c2)))
        else:
            print(len(c1.union(c2)))
