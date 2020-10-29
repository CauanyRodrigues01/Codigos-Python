loops = int(input())

for a in range(loops):
    frase1, frase2 = input().split()

    maior = 0
    menor = 0
    tam_frase1 = len(frase1)
    tam_frase2 = len(frase2)
    if tam_frase1 > tam_frase2:
        maior = frase1
        menor = frase2
    elif tam_frase1 < tam_frase2:
        maior = frase2
        menor = frase1
    elif tam_frase1 == tam_frase2:
        maior = frase2
        menor = frase1
    
    verifica = True
    tam_menor = 0
    palavra = ''
    for b in range(len(maior)):
        if verifica:
            palavra += frase1[b]
            palavra += frase2[b]
            cont = 1
            tam_menor += 1
            if tam_menor == (len(menor)):
                verifica = False
        else:
            palavra += maior[b]
    print(palavra)
