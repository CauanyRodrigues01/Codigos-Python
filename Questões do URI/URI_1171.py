teste = int(input())
numeros = []
for a in range(teste):
    num = int(input())
    cont = 0
    if num not in numeros:
        numeros.append(num)
    elif num in numeros:
        for i in numeros:
            if num == i:
                cont+=1

    print(f"{num} aparece {cont} vez(es)")
