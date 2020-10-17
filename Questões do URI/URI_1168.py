teste = int(input())
for i in range(teste):
    num = input()
    leds = 0
    for c in num:
        if c == "1":
            leds += 2
        elif c == "2":
            leds += 5
        elif c == "3":
            leds += 5
        elif c == "4":
            leds += 4
        elif c == "5":
            leds += 5
        elif c == "6":
            leds += 6
        elif c == "7":
            leds += 3
        elif c == "8":
            leds += 7
        elif c == "9":
            leds += 6
        elif c == "0":
            leds += 6
    print(leds, "leds")
