from _collections import deque

n = int(input())
fila = deque(input().split())

m = int(input())

saidas = input().split()

for i in saidas:
    fila.remove(i)

print(" ".join(fila))
