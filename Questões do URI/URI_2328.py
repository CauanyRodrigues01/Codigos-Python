n = int(input())
entrada = input().split()
estoque = 0
for i in entrada:
    estoque = estoque + int(i)-1

print(estoque)
