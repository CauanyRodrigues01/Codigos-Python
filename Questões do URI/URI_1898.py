'''entrada1 = input()
entrada2 = input()


cpf = ""
linha2 = ""

ponto = 0
for i in entrada1:
    if ponto == 1:
        if i in "0123456789":
            cpf += i
    if ponto == 0:
        if i in "0123456789.":
            cpf += i
            ponto = 1

cpf = cpf[:11]

ponto = 0
for j in entrada2:
    if ponto == 1:
        if j in "0123456789":
            linha2 += j
    if ponto == 0:
        if j in "0123456789.":
            linha2 += j
            ponto = 1
    
propina = float("".join(linha2)) + float("".join(cpf))
#propina = float(cpf[11:]) + float(linha2)
print("cpf", cpf)
print(f"{propina:.2f}")'''

'''entrada1 = input()
entrada2 = input()


cpf = []
linha2 = []

ponto = 0
for i in entrada1:
    if ponto == 1:
        if i in "0123456789":
            cpf.append(i)
    if ponto == 0:
        if i in "0123456789.":
            cpf.append(i)
            ponto = 1

ponto = 0
for j in entrada2:
    if ponto == 1:
        if j in "0123456789":
            linha2.append(j)
    if ponto == 0:
        if j in "0123456789.":
            linha2.append(j)
            ponto = 1
    
propina = float("".join(linha2)) + float("".join(cpf[11:]))

print("cpf", "".join(cpf[:11]))
print(f"{propina:.2f}")'''

'''import re

numeros = re.compile("[\d.]")

ent1 = input()
ent2 = input()

cpf = []
propina = []

for a in ent1:
    if numeros.match(a):
        cpf.append(a)

for b in ent2:
    if numeros.match(b):
        propina.append(b)

print("cpf", "".join(cpf[:11]))
print("{:.2f}".format(float("".join(propina)) + float("".join(cpf[11:]))))'''

import re

numeros = re.compile("[\d.]")

ent1 = input()
ent2 = input()

cpf = ""
propina = ""

for a in ent1:
    if numeros.match(a):
        cpf += a

for b in ent2:
    if numeros.match(b):
        propina += b

print("cpf", cpf[:11])
print(f"{float(propina) + float(cpf[11:]):.2f}")
