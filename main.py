import random
import time

player_health = 100
player_max_health = 100
player_attack = 10
player_weapon = "Меч"  
player_money = 0


enemies = [
    {"name": "Гоблин", "health": 50, "health_max": 50, "attack": 5, "loot": ["Кинжал", "Яблоко"]},
    {"name": "Орк", "health": 80, "health_max": 80, "attack": 8, "loot": ["Топор", "Зелье исцеления"]},
    {"name": "Тролль", "health": 120, "health_max": 120, "attack": 12, "loot": ["Булава", "Золотая монета"]}
]

invalid_weapons = ["Яблоко", "Зелье исцеления", "Золотая монета"]

current_enemy_index = random.randint(0, len(enemies) - 1)
current_enemy = enemies[current_enemy_index]

inventory = []

def show_enemy_info():
    print(f"Имя противника: {current_enemy['name']}")
    print(f"Здоровье противника: {current_enemy['health']}")

def attack():
    global player_health, current_enemy, current_enemy_index, enemies, inventory
    while player_health > 0:
        if not current_enemy or current_enemy["health"] <= 0:
            current_enemy_index = random.randint(0, len(enemies) - 1)
            current_enemy = enemies[current_enemy_index]
            current_enemy["health"] = current_enemy["health_max"]  
            show_enemy_info()

        if player_weapon == "Меч":
            damage = 10
        elif player_weapon == "Кинжал":
            damage = 15
        elif player_weapon == "Булава":
            damage = 20
        elif player_weapon == "Топор":
            damage = 12.5  
        else:
            damage = player_attack

        current_enemy["health"] -= damage
        print(f"Вы атаковали {current_enemy['name']} своим {player_weapon} и нанесли {damage} урона.")
        time.sleep(0.5)  

        if current_enemy["health"] <= 0:
            loot = random.choice(current_enemy["loot"])
            inventory.append(loot)
            print(f"Вы получили: {loot}")
            print(f"{current_enemy['name']} повержен!")
            enemies.pop(current_enemy_index)
            if not enemies:
                enemies = [
                    {"name": "Гоблин", "health": 50, "health_max": 50, "attack": 5, "loot": ["Кинжал", "Яблоко"]},
                    {"name": "Орк", "health": 80, "health_max": 80, "attack": 8, "loot": ["Топор", "Зелье исцеления"]},
                    {"name": "Тролль", "health": 120, "health_max": 120, "attack": 12, "loot": ["Булава", "Золотая монета"]}
                ]
            current_enemy_index = random.randint(0, len(enemies) - 1)
            current_enemy = enemies[current_enemy_index]
            current_enemy["health"] = current_enemy["health_max"]  
            show_enemy_info()
            break

        player_health -= current_enemy["attack"]
        print(f"{current_enemy['name']} атаковал вас и нанес {current_enemy['attack']} урона.")
        time.sleep(0.5) 
        print(f"Ваше здоровье: {player_health}")

    if player_health <= 0:
        print("Вы проиграли!")
        return

def heal():
    global player_health
    player_health = player_max_health
    print(f"Ваше здоровье восстановлено до {player_max_health}.")

def show_inventory():
    global player_weapon, inventory, player_money
    print(f"Текущее оружие: {player_weapon}")
    print(f"Ваши монеты: {player_money}")
    print("Ваш инвентарь:")
    if not inventory:
        print("Инвентарь пуст.")
    else:
        for item in inventory:
            print("- " + item)
        weapon_choice = input("Введите название оружия, которое хотите взять, или нажмите Enter для выхода: ").strip()
        if weapon_choice in inventory and weapon_choice not in invalid_weapons:
            if player_weapon != weapon_choice:
                inventory.append(player_weapon)
                inventory.remove(weapon_choice)
                player_weapon = weapon_choice
                print(f"Вы взяли {player_weapon}.")
            else:
                print(f"У вас уже есть {player_weapon}.")
        elif weapon_choice in invalid_weapons:
            print(f"{weapon_choice} не является оружием.")
        elif weapon_choice:
            print("Такого оружия нет в инвентаре.")

def skip_enemy():
    global current_enemy_index, current_enemy, enemies
    print(f"Вы пропустили {current_enemy['name']}.")
    if len(enemies) > 1:
        enemies.pop(current_enemy_index)
        current_enemy_index = random.randint(0, len(enemies) - 1)
        current_enemy = enemies[current_enemy_index]
        show_enemy_info()
    elif current_enemy["health"] <= 0:
        enemies.pop(current_enemy_index)
        if not enemies:
            enemies = [
                {"name": "Гоблин", "health": 50, "health_max": 50, "attack": 5, "loot": ["Кинжал", "Яблоко"]},
                {"name": "Орк", "health": 80, "health_max": 80, "attack": 8, "loot": ["Топор", "Зелье исцеления"]},
                {"name": "Тролль", "health": 120, "health_max": 120, "attack": 12, "loot": ["Булава", "Золотая монета"]}
            ]
        current_enemy_index = random.randint(0, len(enemies) - 1)
        current_enemy = enemies[current_enemy_index]
        show_enemy_info()
    else:
        current_enemy_index = random.randint(0, len(enemies) - 1)
        current_enemy = enemies[current_enemy_index]
        show_enemy_info()

def upgrade_character():
    global player_attack, player_money
    print("Добро пожаловать в мастерскую!")
    print("Здесь вы можете улучшить свою силу атаки.")
    print(f"Текущий урон: {player_attack}")
    
    if player_money >= 10:
        upgrade_cost = 10
        new_attack = player_attack * 1.2
        print(f"Цена улучшения: {upgrade_cost} монет")
        confirm = input(f"Вы хотите улучшить свою атаку до {new_attack:.2f}? (y/n) ").lower()
        if confirm == "y":
            player_money -= upgrade_cost
            player_attack = new_attack
            print(f"Ваша атака была улучшена до {player_attack:.2f}.")
        else:
            print("Вы отменили улучшение.")
    else:
        print(f"У вас недостаточно монет. Требуется {10 - player_money} монет для улучшения.")

def trade():
    global player_money, inventory
    print("Вы зашли на рынок.")
    
    if not inventory:
        print("У вас нет ничего, что можно продать.")
        return
    
    print("Вот что вы можете продать:")
    for item in inventory:
        if item == "Яблоко":
            price = 5
        elif item == "Зелье исцеления":
            price = 10
        elif item == "Золотая монета":
            price = random.randint(20, 25)
        else:
            price = 0
        if price > 0:
            print(f"- {item} за {price} монет")
    item_to_sell = input("Введите название предмета, который хотите продать, или нажмите Enter для выхода: ").strip()
    if item_to_sell in inventory:
        if item_to_sell == "Яблоко":
            price = 5
        elif item_to_sell == "Зелье исцеления":
            price = 10
        elif item_to_sell == "Золотая монета":
            price = random.randint(20, 25)
        else:
            price = 0
        if price > 0:
            inventory.remove(item_to_sell)
            player_money += price
            print(f"Вы продали {item_to_sell} за {price} монет. Теперь у вас {player_money} монет.")
        else:
            print(f"Вы не можете продать {item_to_sell}.")
    elif item_to_sell:
        print("Такого предмета нет в вашем инвентаре.")
    else:
        print("Вы вышли с рынка.")

print(f"Вы начинаете игру с оружием: {player_weapon} и {player_money} монетами.")

while player_health > 0:
    action = input("Выберите действие (1 - Атака, 2 - Информация о противнике, 3 - Инвентарь, 4 - Восстановить здоровье, 5 - Пропустить противника, 6 - Торговля, 7 - Прокачать персонажа): ")
    if action == "1":
        attack()
    elif action == "2":
        show_enemy_info()
    elif action == "3":
        show_inventory()
    elif action == "4":
        heal()
    elif action == "5":
        skip_enemy()
    elif action == "6":
        trade()
    elif action == "7":
        upgrade_character()
    else:
        print("Неверный выбор действия. Попробуйте снова.")