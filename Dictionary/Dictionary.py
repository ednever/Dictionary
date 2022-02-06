def failist_sõnastikusse():
    sonastik = {}
    file = open("CaC.txt","r",encoding = "utf-8-sig")
    for line in file:
        linn,pealinn = line.strip().split(":")
        sonastik[linn.strip()] = pealinn.strip()
    file.close()
    return sonastik

sonastik = failist_sõnastikusse()

vastus = True
while vastus:
    print("""
    1. Все страны и столицы
    2. Поиск
    3. Новая страна и столица
    4. Исправление ошибок
    5. Тест
    6. Озвучивание
    7. Выйти""")
    vastus = input(" >>> ")
    if vastus == "1":
        print(sonastik)
    elif vastus == "2":
        slovo = input("Введите страну или столицу для получения большей информации о ней >>> ")
        if slovo in sonastik:
            print(slovo + " - " + sonastik[slovo])
        else:
            print("Такой страны или столицы ещё не существует")
    elif vastus == "3":
        slovo = input("Введите страну, которую хотите добавить >>> ")
        slovo2 = input("Введите страну, которую хотите добавить >>> ")
        with open("CaC.txt","a",encoding = "utf-8-sig") as fail:
            fail.write(slovo + ":" + slovo2 + "\n")
        sonastik[slovo] = slovo2
        print(f'Страна "{slovo}" и её столица "{slovo2}" добавлены')
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
        print("Неправильный тип данных!")