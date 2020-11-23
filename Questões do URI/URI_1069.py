loops = int(input())
entrada = []
stack = []
contAbre = 0
cont = 0
listaCont = []

for i in range(loops):
    lista = [i for i in input().split()]
    entrada.append(lista)

for i in entrada:
    for j in i:
        for w in j:
            if w == '<':
                stack.append(w)
                contAbre += 1
            elif w == '>' and contAbre > 0:
                stack.pop()
                contAbre -= 1
                cont += 1
    listaCont.append(cont)
    cont = 0
    contAbre = 0

for i in listaCont:
    print(i)
