# ТЕМА: Робота зі словником
# Варіант 8
# Задано дані про потужність двигуна і вартість n=10 легкових автомобілів.
# Визначити загальну вартість автомобілів, у яких потужність двигуна перевищує 100 к.с.

cars = {
    "Toyota_Corolla": {"power": 132, "price": 18500},
    "Volkswagen_Golf": {"power": 110, "price": 21000},
    "Skoda_Fabia": {"power": 95, "price": 14500},
    "BMW_320i": {"power": 184, "price": 32000},
    "Audi_A4": {"power": 150, "price": 30000},
    "Renault_Logan": {"power": 90, "price": 12000},
    "Ford_Focus": {"power": 125, "price": 17000},
    "Hyundai_i30": {"power": 100, "price": 16500},
    "Kia_Ceed": {"power": 120, "price": 19000},
    "Mercedes_C200": {"power": 204, "price": 42000}
}


def print_cars():
    print("\nВсі автомобілі:")
    for name, data in cars.items():
        print(f"{name}: потужність = {data['power']} к.с., вартість = {data['price']} євро")


def add_car():
    try:
        name = input("Введіть назву автомобіля: ")

        if name in cars:
            print("Такий автомобіль вже є у словнику.")
            return

        power = int(input("Введіть потужність двигуна, к.с.: "))
        price = int(input("Введіть вартість автомобіля: "))

        cars[name] = {"power": power, "price": price}
        print("Автомобіль додано до словника.")

    except ValueError:
        print("Помилка введення. Потужність і вартість мають бути числами.")


def delete_car():
    name = input("Введіть назву автомобіля для видалення: ")

    try:
        del cars[name]
        print("Автомобіль видалено зі словника.")
    except KeyError:
        print("Помилка. Автомобіля з такою назвою немає у словнику.")


def print_sorted_cars():
    print("\nСловник, відсортований за ключами:")

    for name in sorted(cars.keys()):
        data = cars[name]
        print(f"{name}: потужність = {data['power']} к.с., вартість = {data['price']} євро")


def total_price_power_more_100():
    total = 0

    print("\nАвтомобілі з потужністю більше 100 к.с.:")

    for name, data in cars.items():
        if data["power"] > 100:
            print(f"{name}: {data['power']} к.с., {data['price']} євро")
            total += data["price"]

    print("Загальна вартість автомобілів з потужністю більше 100 к.с. =", total, "євро")


def menu():
    while True:
        print("\nМеню")
        print("1 - Вивести всі автомобілі")
        print("2 - Додати автомобіль")
        print("3 - Видалити автомобіль")
        print("4 - Вивести словник за відсортованими ключами")
        print("5 - Обчислити загальну вартість автомобілів з потужністю більше 100 к.с.")
        print("0 - Вихід")

        choice = input("Виберіть пункт меню: ")

        if choice == "1":
            print_cars()
        elif choice == "2":
            add_car()
        elif choice == "3":
            delete_car()
        elif choice == "4":
            print_sorted_cars()
        elif choice == "5":
            total_price_power_more_100()
        elif choice == "0":
            print("Роботу програми завершено.")
            break
        else:
            print("Помилка. Такого пункту меню немає.")


menu()
