#Вариант 1
import json
import os
DATA_FILE = "fishes.json"
operations_count = 0
def load_fishes():
    if not os.path.exists(DATA_FILE):
        fishes = [
            {"id": 1, "name": "Карп", "latin_name": "Cyprinus carpio", "is_salt_water_fish": False, "sub_type_count": 3},
            {"id": 2, "name": "Лосось", "latin_name": "Salmo salar", "is_salt_water_fish": True, "sub_type_count": 5},
            {"id": 3, "name": "Щука", "latin_name": "Esox lucius", "is_salt_water_fish": False, "sub_type_count": 2},
            {"id": 4, "name": "Тунец", "latin_name": "Thunnus", "is_salt_water_fish": True, "sub_type_count": 8},
            {"id": 5, "name": "Окунь", "latin_name": "Perca fluviatilis", "is_salt_water_fish": False, "sub_type_count": 4}
        ]
        save_fishes(fishes)
        return fishes
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)
def save_fishes(fishes):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(fishes, f, ensure_ascii=False, indent=2)
def check_id(fish_id):
    return fish_id.strip().isdigit()
def check_name(name):
    return len(name.strip()) > 0
def check_number(num):
    return num.strip().isdigit() and int(num) >= 0
def show_all():
    global operations_count
    operations_count += 1
    fishes = load_fishes()
    if not fishes:
        print("\nБаза данных пуста!")
        return
    print(f"\nВсего записей: {len(fishes)}")
    print("-" * 70)
    for i, fish in enumerate(fishes, 1):
        water = "морская" if fish["is_salt_water_fish"] else "пресноводная"
        print(f"{i}. ID: {fish['id']}")
        print(f"   Название: {fish['name']}")
        print(f"   Латинское название: {fish['latin_name']}")
        print(f"   Тип: {water}")
        print(f"   Количество подвидов: {fish['sub_type_count']}")
        print("-" * 70)
def find_by_id():
    global operations_count
    operations_count += 1
    fish_id = input("Введите ID рыбы для поиска: ").strip()
    if not check_id(fish_id):
        print("\nОшибка: ID должен быть числом!")
        return
    fishes = load_fishes()
    fish_id = int(fish_id)
    for fish in fishes:
        if fish["id"] == fish_id:
            water = "морская" if fish["is_salt_water_fish"] else "пресноводная"
            print(f"\nНайдена запись:")
            print("-" * 50)
            print(f"ID: {fish['id']}")
            print(f"Название: {fish['name']}")
            print(f"Латинское название: {fish['latin_name']}")
            print(f"Тип: {water}")
            print(f"Количество подвидов: {fish['sub_type_count']}")
            return
    print(f"\nРыба с ID {fish_id} не найдена!")
def add_fish():
    global operations_count
    operations_count += 1
    fishes = load_fishes()
    print("\nДобавление новой рыбы:")
    max_id = max(fish["id"] for fish in fishes) if fishes else 0
    new_id = max_id + 1
    name = input("Введите название рыбы: ").strip()
    if not check_name(name):
        print("Ошибка: Название не может быть пустым!")
        return
    latin = input("Введите латинское название: ").strip()
    if not check_name(latin):
        print("Ошибка: Латинское название не может быть пустым!")
        return
    water = input("Морская рыба? (да/нет): ").strip().lower()
    if water not in ['да', 'yes', 'y', 'д', 'нет', 'no', 'n', 'н']:
        print("Ошибка: Введите 'да' или 'нет'!")
        return
    subtypes = input("Введите количество подвидов: ").strip()
    if not check_number(subtypes):
        print("Ошибка: Введите неотрицательное число!")
        return
    new_fish = {
        "id": new_id,
        "name": name,
        "latin_name": latin,
        "is_salt_water_fish": water in ['да', 'yes', 'y', 'д'],
        "sub_type_count": int(subtypes)
    }
    fishes.append(new_fish)
    save_fishes(fishes)
    print(f"\nРыба '{name}' добавлена с ID: {new_id}")
def delete_fish():
    global operations_count
    operations_count += 1
    fish_id = input("Введите ID рыбы для удаления: ").strip()
    if not check_id(fish_id):
        print("\nОшибка: ID должен быть числом!")
        return
    fishes = load_fishes()
    fish_id = int(fish_id)
    for i, fish in enumerate(fishes):
        if fish["id"] == fish_id:
            deleted = fishes.pop(i)
            save_fishes(fishes)
            water = "морская" if deleted["is_salt_water_fish"] else "пресноводная"
            print(f"\nРыба удалена:")
            print(f"ID: {deleted['id']}")
            print(f"Название: {deleted['name']}")
            return
    print(f"\nРыба с ID {fish_id} не найдена!")
def show_menu():
    print("\n" + "="*50)
    print("БАЗА ДАННЫХ РЫБ")
    print("="*50)
    print("1. Показать всех рыб")
    print("2. Найти рыбу по ID")
    print("3. Добавить рыбу")
    print("4. Удалить рыбу")
    print("5. Выйти")
    print("-"*50)
def main():
    print("Добро пожаловать в базу данных рыб!")
    while True:
        show_menu()
        choice = input("Выберите действие (1-5): ").strip()
        if choice == "1":
            show_all()
        elif choice == "2":
            find_by_id()
        elif choice == "3":
            add_fish()
        elif choice == "4":
            delete_fish()
        elif choice == "5":
            print(f"\nВсего операций: {operations_count}")
            print("До свидания!")
            break
        else:
            print("\nОшибка! Выберите от 1 до 5")
        if choice != "5":
            input("\nНажмите Enter чтобы продолжить...")
if __name__ == "__main__":
    main()
