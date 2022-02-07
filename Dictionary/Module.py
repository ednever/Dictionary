from random import *
#import os
#from gtts import gTTS
def failist_sõnastikusse():
    sonastik = {}
    file = open("CC.txt","r",encoding = "utf-8-sig")
    for line in file:
        linn,pealinn = line.strip().split(":")
        sonastik[linn.strip()] = pealinn.strip()
    file.close()
    return sonastik

def new_word(sonastik:dict):
    slovo = input("Введите страну, которую хотите добавить >>> ")
    slovo2 = input("Введите столицу, которую хотите добавить >>> ")
    with open("CC.txt","a",encoding = "utf-8-sig") as fail:
        fail.write(slovo + ":" + slovo2 + "\n")
    sonastik[slovo] = slovo2
    print(f'Страна "{slovo}" и её столица "{slovo2}" добавлены')

def test(result:int,l:list,l2:list)->int:
    """Juhuslikult valitakse sõna loendist, ning pärast kontrollitakse
    :param int result: Punktide arv
    :param list l: Vene keele sõnastik
    :param list l2: Inglise keele sõnastik
    :rtype: int
    """
    slovo = choice(l)
    otvet = input(f"{slovo} >>> ")
    if otvet in l2: 
        if l2.index(otvet) == l.index(slovo):
            result += 1
            print("Правильно")
    else:
        print("Неправильно")
    return result

#def heli(text:str,keel:str):
#    """
#    :param str text: sõna mis tahad rääkida
#    :param str keel: millises keeles tahad rääkida"""
#    obj = gTTS(text = text,lang = keel, slow = False).save("heli.mp3")
#    os.system("heli.mp3")