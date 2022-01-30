from Module import*
from random import*
sonastik = {}
file = open("C_C.txt","r")
for line in file:
    k,v = line.strip().split("-")
    sonastik[k.strip()] = v.strip()

vastus = True
while vastus:
    print("""
    1. Kõik riigid ja pealinnad
    2. Polnoreff
    3. Uus riik või pealinn
    4. Viga parandamine
    5. Test
    6. Rääkimine
    7. Välja minna""")
    vastus = input(" >>> ")
    if vastus == "1":
        print(sonastik)
    elif vastus == "2":
        print()
    elif vastus == "3":
        print()
    elif vastus == "4":
        print()
    elif vastus == "5":
        print()
    elif vastus == "6":
        print()
        #text=input("->")
        #keel=input("->")
        #heli(text,keel)
    elif vastus == "7":
        vastus = False
    else:
        print("Vale andmetüüp!")
