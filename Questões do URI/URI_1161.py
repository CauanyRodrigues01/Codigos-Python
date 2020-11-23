# 0! = 1
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24

'''while True:
    try:
        a, b = [int(i) for i in input().split()]

        contA = a - 1
        contB = b - 1

        if a == 0:
            a = 1
        if b == 0:
            b = 1

        while contA > 0:
            a = a * contA
            contA -= 1

        while contB > 0:
            b = b * contB
            contB -= 1

        print(a + b)
        
    except EOFError:
        break'''

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

while True:
    try:
        a, b = [int(i) for i in input().split()]

        soma = fatorial(a) + fatorial(b)

        print(soma)
        
    except EOFError:
        break
