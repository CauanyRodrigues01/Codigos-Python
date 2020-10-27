loops = int(input())

for a in range(loops):
    mensagem = input()

    criptografia = ''

    for b in mensagem:
        if b in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            criptografia += chr(ord(b)+3)
        else:
            criptografia += b

    criptografia = criptografia[::-1]

    meio = int((len(criptografia)/2))
    metade2Novo = ''
    for c in criptografia[meio:]:
        metade2Novo += chr(ord(c)-1)

    criptografia_final = criptografia[0:meio] + metade2Novo

    print(criptografia_final)

'''import re

loops = int(input())

for a in range(loops):
    mensagem = input()

    criptografia = ''

    for b in mensagem:
        if re.match("[a-zA-Z]", b):
            criptografia += chr(ord(b)+3)
        else:
            criptografia += b

    criptografia = criptografia[::-1]

    meio = int((len(criptografia)/2))
    metade1 = criptografia[0:meio]
    metade2 = criptografia[meio:]

    metade2Novo = ''

    for c in metade2:
        metade2Novo += chr(ord(c)-1)

    criptografia_final = metade1 + metade2Novo

    print(criptografia_final)'''


'''loops = int(input())

for a in range(loops):
    mensagem = input()

    criptografia_1 = []
    criptografia_2 = []
    criptografia_final = []

    for b in mensagem:
        if b in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTUVWXYZ":
            criptografia_1.append(chr(ord(b)+3))
        else:
            criptografia_1.append(b)

    for c in range(len(criptografia_1)-1, -1, -1):
        criptografia_2.append(criptografia_1[c])

    inverte = False
    while True:
        if inverte:
            for d in range((int(len(criptografia_2)/2)), len(criptografia_2)):
                criptografia_final.append(chr(ord(criptografia_2[d])-1))
            break
        else:
            for e in range(int(len(criptografia_2)/2)):
                criptografia_final.append(criptografia_2[e])
            inverte = True

    print("".join(criptografia_final))'''


