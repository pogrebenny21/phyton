# название = значение

import time
import random

hp = 100
mana = 100
strength = 5
agility = 5
intellect = 5
lvl = 1

print("Здоровье:", hp, "Стас Давыдов:", mana)
print(f"Сила: {strength}\nЛовкость: {agility}\nИнтеллект: {intellect}")
name = input("Введите имя персонажа: ")
print(f"Приветствуем вас, {name}!")

_class = input("Выберите класс: 1. язь, 2. адвокат, 3. паукан\n")
# Если класс ЯЗЬ - умножаем силу на 2, а ловкость на 1.6
# Если класс Адвокат - умножаем интеллект на 2, а ловкость на 1.3
# Если класс Паукан - умножаем ловкость на 2, а силу на 1.5, а интеллект на 1.3
# > < == >= <= !=
if _class == "язь" or _class== "1":
    strength = strength * 2
    agility *= 1.6 
    _class = "язь"
elif _class == "адвокат" or _class== "2":
    intellect *= 2
    agility *= 1.3
    _class == "адвокат"
elif _class == "паукан" or _class== "3":
    agility *= 2
    strength *= 1.5
    intellect *= 1.3
    _class == "паукан"
else: 
    print("ФАТАЛЬНАЯ ОШИБКА, ты Говно!.\nВсе характеристики понижены на 3")
    strength -= 3
    agility -= 3
    intellect -= 3
    _class = "Вирусные Видео"

print(f"Ваш новый класс: {_class}, новые характеристики:\nСила: {strength}\nЛовкость: {agility}\nИнтеллект: {intellect}")


for i in range(5,100,2):
     print("Проход По Циклу (Вирусные Видео) №" , i)

n = 0



isGame = True
while isGame:
    print("Игра Началась")
    hp -= 1
    rand = random.randint(1,6)
    print("выпало", rand)
    print("Здоровье на исходе:" , hp)
    if hp <= 0:
        print("Остаток Здоровья:" , hp)
        print("WASTED!")
        isGame = False
        break
    time.sleep(0.5)


print("Конец Игры!")