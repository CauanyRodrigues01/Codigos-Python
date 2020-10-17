a, g, ra, rg = map(float, input().split())

def calculoRazao(precoA, precoG, rendA, rendG):
    razaoA = rendA/precoA
    razaoG = rendG/precoG

    if (razaoA <= razaoG) or (precoA == precoG and rendA == rendG):
        print("G")
    else:
        print("A")
        
calculoRazao(a, g, ra, rg)
