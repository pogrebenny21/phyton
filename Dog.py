# TODO Создать класс СОБАКА, добавить ей Характеристики: Кличка, Порода, Вес, Злоба, Доброта, Дрожь
# TODO Добавить Методы (Функции) Бега (должно Выводится "Собака Кличка Бежит") и Вывода Информации о собаке
# Кличка: Шарик, Порода: Простокашенская, вес: 88 кг, Злоба: 70%, Дрожь: 0%


class Dog:
    def __init__(self, NewName, newBreed, newWeight, newEvil, newGood, newShake):
       self.name = NewName
       self.breed = newBreed
       self.weight = newWeight
       self.evil = newEvil
       self.good = newGood
       self.shake = newShake

    def Run(self):
        print("Имя:", self.name)
        print("Порода:", self.breed)
        print("Вес:", self.weight)
        print("Процент Злобы:", self.evil)
        print("Процент Доброты:", self.good)
        print("Процент Дрожи:", self.shake)
    def Run(self):
        print(self.name,"Бежит")

dog1 = Dog("Шарик", "Простокашенская", "88", 70, 100, 0)
dog1.Run()