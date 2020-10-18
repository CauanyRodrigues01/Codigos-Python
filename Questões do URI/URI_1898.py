entrada1 = input()
entrada2 = input()


desc1 = ""
desc2 = ""
'''for i in entrada1:
    if ponto:
        if i in "0123456789.":
            desc1 += i
            ponto = False
    else:
        if i in "0123456789":
            desc1 += i
ponto = True
for i in entrada2:
    if ponto:
        if i in "0123456789.":
            desc2 += i
    else:
        if i in "0123456789":
            desc2 += i'''
ponto1 = 0
for i in entrada1:
    if ponto == 1:
        if i in "0123456789":
            desc1 += i
    if ponto == 0:
        if i in "0123456789.":
            desc1 += i
            ponto = 1

ponto = 0
for j in entrada2:
    if ponto == 1:
        if j in "0123456789":
            desc2 += j
    if ponto == 0:
        if j in "0123456789.":
            desc2 += j
            ponto = 1
    

novo1 = desc1[11:]
saida2 = float(novo1) + float(desc2)

#testes
print("desc1",desc1)
print("desc2",desc2)
print("novo1",novo1)
print("saida2",saida2)
print("cpf "+desc1[:11])
print(f"{saida2:.2f}")
