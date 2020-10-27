loops = int(input())
for i in range(loops):
    num1, num2 = [str(i) for i in input().split()]
    parte_comparar = num1[-len(num2):]
    if num2 in parte_comparar:
        print("encaixa")
    else:
        print("nao encaixa")
