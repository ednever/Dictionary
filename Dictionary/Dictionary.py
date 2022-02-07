from Module import *
from random import *
sonastik = failist_sõnastikusse()
linnad = [i for i in sonastik.keys()]
pealinnad = [i for i in sonastik.values()]
vastus = True
while vastus:
    print("""
    1. Все страны и столицы
    2. Поиск стран и столиц
    3. Новая страна и столица
    4. Исправление ошибок
    5. Тест
    6. Озвучивание
    7. Выйти""")
    vastus = input(" >>> ")
    if vastus == "1":
        for key, value in sonastik.items():
            print(key + " - " + value)
    elif vastus == "2":
        slovo = input("Введите страну или столицу для получения большей информации о ней >>> ")
        if slovo in linnad:
            print(slovo + " - " + sonastik[slovo])
        elif slovo in pealinnad:
            print(slovo + " - " + linnad[pealinnad.index(slovo)])
        else:
            print(f'Страны или столицы "{slovo}" нет в словаре')
    elif vastus == "3":
        new_word(sonastik)
    elif vastus == "4": #Не удаляет старую запись с файла
        slovo = input("Введите страну, в которой допущена ошибка >>> ")
        if slovo in sonastik:
            print(f'Страна "{slovo}" со своей столицей была удалена')
            del sonastik[slovo]
            new_word(sonastik)
        else:
            print("Такой страны в списке нет, попрубуйте ещё раз")
    elif vastus == "5":
        print("""
        Вводите правильные ответы""")
        result = 0
        for i in range(5):
            number = randint(1,2)
            if number == 1:
                result = test(result,linnad,pealinnad)                
            else:
                result = test(result,pealinnad,linnad)
        hind = result * 100 / 5
        print(f"У тебя {result}/5 баллов")
        if hind >= 90:
            print("Отлично, вы получили 5!")
        elif hind >= 75 and hind <= 90:
            print("Молодец, вы получили 4!")
        elif hind >= 50 and hind <= 75:
            print("Неплохо, вы получили 3!")
        else:
            print("Ничего страшного, вы получили 2!")
    elif vastus == "6": #Не работает
        print()
        #text=input("->")
        #keel=input("->")
        #heli(text,keel)
    elif vastus == "7":
        vastus = False
    else:
        print("Неправильный тип данных!")