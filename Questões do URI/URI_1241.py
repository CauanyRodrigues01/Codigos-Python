testes = int(input())
for i in range(testes):
    num1, num2 = [str(i) for i in input().split()]
    parte_comparar = num2[-len(num2):]
    print(parte_comparar)
    if num2 in parte_comparar:
        print("encaixa")
    else:
        print("nao encaixa")
