# название = значение

import time
import random

hp = 100
mana = 100
strength = 5
agility = 5
intellect = 5
lvl = 1
damage = 5
defence = 5

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
    damage = 5
    defence = 5
    _class = "язь"
elif _class == "адвокат" or _class== "2":
    intellect *= 2
    agility *= 1.3
    damage = 5
    defence = 5
    _class == "адвокат"
elif _class == "паукан" or _class== "3":
    agility *= 2
    strength *= 1.5
    intellect *= 1.3
    damage = 5
    defence = 5
    _class == "паукан"
else: 
    print("ФАТАЛЬНАЯ ОШИБКА, ты Говнcnfcо!.\nВсе характеристики понижены на 3")
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

    rand = random.randint(1,6)

    enemy =[]
    "Name":"Адвокат"
    "damage":15,
    "hp":40
    "armor":4

    
    print("Выпало" , rand)

    enemyName ="Жив Цел Орёл"
    enemyName1 ="Ниппон Газаува"
    enemyName2 ="Я Пушистый я Смелей"
    enemyName3 ="Копротошка"
    enemyName4 ="Члензилло"

    massEnemies = ["Жив Цел Орёл", "Ниппон Газаува", "Я Пушистый я Смелей", "Копротошка", "Члензилло"]
    print(massEnemies[0])
    print(len(massEnemies))
    print(massEnemies[len(massEnemies)-1])

    massEnemies.append(123)
    print(massEnemies)
    massEnemies.remove
    print(massEnemies)
    massEnemies.copy
    print(massEnemies)
    massEnemies.pop(0)
    print(massEnemies)

if rand == 2:
        hpEnemy = 100
        damageEnemy = 75
        while True:
            print("Перед Вами Вылез Адвокат Что Будем Делать?")
            Choice = input("1. аттоковать 2. Защититься 3. увернутся")
            if Choice == "1":
                hpEnemy -= damage
                print(f"АДВОКАТ ПОЛУЧИЛ ОПЛЕУХУ!! У НЕГО ОСТАЛОСЬ {hpEnemy}")
            elif Choice =="2":
                if damageEnemy > defence:
                    hp = hp - (damageEnemy-defence) 
                    print(f"Адвокат наносит {damageEnemy-defence} Урона")
                else:
                    print("Невироятная Защита! Урон Полностью Блокирован!")
            
            elif Choice == "3":
                print("Уворот")
            if (hpEnemy<=0):
                print("ПОБЕДА!!")
                break
                
if hp <= 0:
        print("Остаток Здоровья:" , hp)
        print("WASTED!")
        isGame = Falsebreak       
time.sleep(0.5)


print("Конец Игры!")