loops = int(input())

familia = dict()

for a in range(loops):
    entrada = input().split()
    familia[entrada[0]] = [entrada[1], entrada[2], entrada[3]]
while True:
    try:
        teste = input().split()
        pessoa = teste[0]
        presente = teste[1]
        if pessoa in familia:
            if presente in familia[pessoa]:
                print("Uhul! Seu amigo secreto vai adorar o/")
            else:
                print("Tente Novamente!")
        else:
            print("Tente Novamente!")
            
    except EOFError:
        break
