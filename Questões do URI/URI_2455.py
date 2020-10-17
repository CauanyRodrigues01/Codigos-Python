p1, c1, p2, c2 = map(int, input().split())

ladoEsquerdo = p1 * c1
ladoDireito = p2 * c2

if ladoEsquerdo == ladoDireito:
    print("0")
if ladoEsquerdo < ladoDireito:
    print("1")
if ladoEsquerdo > ladoDireito:
    print("-1")
