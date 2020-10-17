entrada1 = input()
entrada2 = input()


desc1 = ""
desc2 = ""
for i in entrada1:
    if i in "0123456789":
        desc1 += i
for i in entrada2:
    if i in "0123456789":
        desc2 += i
    
print("cpf "+desc1[:11])
print(f"{int(desc2):.2f}")
