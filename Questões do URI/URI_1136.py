while True:
    ent = input().split()
    loops = int(ent[0])
    numBolas = int(ent[1])
    
    if (loops == 0 and numBolas == 0):
        break

    bolas = list(map(int, input().split()))

    difBolas = [0]*(loops+1)

    for a in bolas:
        for b in bolas:
            if (a >= b):
                dif = a - b
                difBolas[dif] = 1
            else:
                dif = b - a
                difBolas[dif] = 1
                
    if (difBolas.count(1) < loops+1):
        print("N")
    else:
        print("Y")
