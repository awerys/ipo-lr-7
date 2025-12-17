#Вариант 1
import json
import os
DATA_FILE = "fishes.json"
operations_count = 0
if not os.path.exists(DATA_FILE):
    initial_data = [
        {"id": 1, "name": "Карп", "latin_name": "Cyprinus carpio", "is_salt_water_fish": False, "sub_type_count": 3},
        {"id": 2, "name": "Лосось", "latin_name": "Salmo salar", "is_salt_water_fish": True, "sub_type_count": 5},
        {"id": 3, "name": "Щука", "latin_name": "Esox lucius", "is_salt_water_fish": False, "sub_type_count": 2},
        {"id": 4, "name": "Тунец", "latin_name": "Thunnus", "is_salt_water_fish": True, "sub_type_count": 8},
        {"id": 5, "name": "Окунь", "latin_name": "Perca fluviatilis", "is_salt_water_fish": False, "sub_type_count": 4}
    ]
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(initial_data, f, ensure_ascii=False, indent=2)
while True:
    print("\n" + "="*50)
    print("Меню данной базы рыб:")
    print(" "*50)
    print("1. Вывести все записи")
    print("2. Вывести запись по полю (id)")
    print("3. Добавить запись")
    print("4. Удалить запись по полю (id)")
    print("5. Выйти из программы")
    print(" "*50)
    choice = input("Выберите пункт меню (1-5): ").strip()
    if choice == "1":
        operations_count += 1
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                fishes = json.load(f)
            else:
                print(f"\nВсего записей: {len(fishes)}")
                print("-" * 70)
                for i, fish in enumerate(fishes, 1):
                    water_type = "морская" if fish["is_salt_water_fish"] else "пресноводная"
                    print(f"{i}. ID: {fish['id']}")
                    print(f"   Название: {fish['name']}")
                    print(f"   Латинское название: {fish['latin_name']}")
                    print(f"   Тип: {water_type}")
                    print(f"   Количество подвидов: {fish['sub_type_count']}")
                    print(" " * 70)
    elif choice == "2":
        operations_count += 1
            fish_id = input("Введите ID рыбы для поиска: ").strip()
            fish_id = int(fish_id)
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                fishes = json.load(f)
            found = False
            for position, fish in enumerate(fishes, 1):
                if fish["id"] == fish_id:
                    print(f"\nНайдена запись (позиция {position}):")
                    print("-" * 50)
                    water_type = "морская" if fish["is_salt_water_fish"] else "пресноводная"
                    print(f"ID: {fish['id']}")
                    print(f"Название: {fish['name']}")
                    print(f"Латинское название: {fish['latin_name']}")
                    print(f"Тип: {water_type}")
                    print(f"Количество подвидов: {fish['sub_type_count']}")
                    print(" " * 50)
                    found = True
                    break
    elif choice == "3":
        operations_count += 1
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                fishes = json.load(f)
            print("\nДобавление новой записи о рыбе:")
            print("-" * 30)
            max_id = max(fish["id"] for fish in fishes) if fishes else 0
            new_id = max_id + 1
            name = input("Введите общее название рыбы: ").strip()
            latin_name = input("Введите латинское название рыбы: ").strip()
            water_input = input("Морская рыба? (да/нет): ").strip().lower()
            is_salt_water_fish = water_input in ['да', 'yes', 'y', 'д']
            sub_type_count_input = input("Введите количество подвидов: ").strip()
            sub_type_count = int(sub_type_count_input)
            new_fish = {
                "id": new_id,
                "name": name,
                "latin_name": latin_name,
                "is_salt_water_fish": is_salt_water_fish,
                "sub_type_count": sub_type_count
            }
            fishes.append(new_fish)
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(fishes, f, ensure_ascii=False, indent=2)
            print(f"\nЗапись успешно добавлена с ID: {new_id}")
    elif choice == "4":
        operations_count += 1
            fish_id = input("Введите ID рыбы для удаления: ").strip()
            fish_id = int(fish_id)
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                fishes = json.load(f)
            found = False
            for i, fish in enumerate(fishes):
                if fish["id"] == fish_id:
                    deleted_fish = fishes.pop(i)
                    water_type = "морская" if deleted_fish["is_salt_water_fish"] else "пресноводная"
                    with open(DATA_FILE, 'w', encoding='utf-8') as f:
                        json.dump(fishes, f, ensure_ascii=False, indent=2)
                    print(f"\nЗапись успешно удалена:")
                    print(f"ID: {deleted_fish['id']}")
                    print(f"Название: {deleted_fish['name']}")
                    print(f"Латинское название: {deleted_fish['latin_name']}")
                    print(f"Тип: {water_type}")
                    print(f"Количество подвидов: {deleted_fish['sub_type_count']}")
                    found = True
                    break
            if not found:
                print(f"\nРыба с ID {fish_id} не найдена")
        except ValueError:
            print("\nОшибка: Неверный формат ID")
        except Exception as e:
            print(f"\nОшибка при удалении записи: {e}")
    elif choice == "5":
        print(f"\nВсего выполнено операций: {operations_count}")
        print("Программа завершена. До свидания")
        break
