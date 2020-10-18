cont = 0
while True:
    n = int(input())
    if(n == 0):
        break
    entrada = input().split()
    cont += 1
    print("Teste", cont)
    for i in range(n):
        aux = entrada[i]
        if (int(aux) == i+1):
            print(entrada[i])
    print()
