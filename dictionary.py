print("hello world!")
user = {
    "username": "Процессор",
    "password": 12345,
    "robux": 3000,
    "age": 34,
    "genger": "Мужской"
}

print("Имя Пользователя", user["username"])
print("У Вас", user["robux"], "Робусов")

print("До Манипуляций", user)
user.clear()
print("Поле Clear",user)

print(user.get("gender")) #тоже самое что и User["gender"]
print(user.items())
print(user.keys)
print (user.pop("robux"))
print (user)
print (user.values())
# добавляем в словарь новое свойство 
user["robux"] = 1234567


user.setdefault("new key", "Моё Новое Значение")

print(user)

enemy = {
    "hp": 100,
    "damage": 10

}
def fight(player=player, enemy=enemy):
    pass
    print(f"Игрок {player["name"]} атакует {enemy["name"]} и Наносит {player["damage"]}")
    enemy["hp"] -= player ["damage"]
    print(f"У {enemy["name"]} Осталось {enemy["hp"]}, Здоровья")

    fight(player, enemy)
    fight(player, enemy)