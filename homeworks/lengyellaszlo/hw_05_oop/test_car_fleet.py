# test_car_fleet.py

import random
from car_fleet_mgr import (
    Fleet,
    read_fleet_from_txt,
    save_fleet_to_txt,
    CAR_DATABASE,
    FLEET_FILE,
    logger
)


def ask_repeat_count():
    """Bekéri, hányszor fusson le egy teszt (max. 5)."""
    while True:
        try:
            count = int(input("Hányszor fusson le? (1-5): ").strip())
            if 1 <= count <= 5:
                return count
            else:
                print("Csak 1 és 5 közötti számot adhatsz meg.")
        except ValueError:
            print("Érvénytelen érték, egész számot adj meg.")


def rand_add(fleet):
    """Véletlen autók hozzáadása."""
    repeat = ask_repeat_count()
    for _ in range(repeat):
        brand = random.choice(list(CAR_DATABASE.keys()))
        model_info = random.choice(CAR_DATABASE[brand])
        model = model_info["model"]
        from_year = model_info["from"]
        to_year = model_info["to"] or 2025
        year = random.randint(from_year, to_year)
        fleet.add_car(brand, model, year)
    logger.info(f"{repeat} véletlen autó hozzáadva.")
    print(f"{repeat} véletlen autó hozzáadva.")


def rand_remove(fleet):
    """Véletlen autók törlése."""
    if not fleet.cars:
        print("A flotta üres, nincs mit törölni.")
        return
    repeat = ask_repeat_count()
    for _ in range(repeat):
        if not fleet.cars:
            print("A flotta kiürült, nincs több törölhető autó.")
            break
        car_name = random.choice(list(fleet.cars.keys()))
        fleet.remove_car(car_name)
    logger.info(f"{repeat} véletlen törlés lefutott.")
    print(f"{repeat} véletlen törlés lefutott.")


def rand_drive(fleet):
    """Véletlen vezetés (-100 és 1200 km között)."""
    if not fleet.cars:
        print("A flotta üres, nincs mit vezetni.")
        return
    repeat = ask_repeat_count()
    for _ in range(repeat):
        car_name = random.choice(list(fleet.cars.keys()))
        car = fleet.cars[car_name]
        distance = random.randint(-100, 1200)
        print(f"{car_name}: {car.brand} {car.model} - {distance} km próbálkozás")
        car.drive(distance)
    logger.info(f"{repeat} véletlen vezetési művelet lefutott.")
    print(f"{repeat} véletlen vezetési művelet lefutott.")


def rand_refuel(fleet):
    """Véletlen tankolás (-10 és 100% között)."""
    if not fleet.cars:
        print("A flotta üres, nincs mit tankolni.")
        return
    repeat = ask_repeat_count()
    for _ in range(repeat):
        car_name = random.choice(list(fleet.cars.keys()))
        car = fleet.cars[car_name]
        amount = random.randint(-10, 100)
        print(f"{car_name}: {car.brand} {car.model} - tankolás {amount}% próbálkozás")
        car.refuel(amount)
    logger.info(f"{repeat} véletlen tankolási művelet lefutott.")
    print(f"{repeat} véletlen tankolási művelet lefutott.")


def test_menu():
    """Tesztmenü a flotta automatikus próbáihoz."""
    fleet = read_fleet_from_txt(FLEET_FILE)

    while True:
        print("\n--- FLOTTA TESZT MENÜ ---")
        print("1. Flotta megtekintése")
        print("2. Véletlen autók hozzáadása")
        print("3. Véletlen autók törlése")
        print("4. Véletlen vezetés")
        print("5. Véletlen tankolás")
        print("6. Kilépés (mentéssel)")
        print("7. Kilépés (mentés nélkül)")

        choice = input("Válassz egy opciót (1–7): ").strip()

        if choice == "1":
            if not fleet.cars:
                print("A flotta üres.")
                continue
            print("\n--- FLOTTA TARTALMA ---")
            for name, car in fleet.cars.items():
                print(f"{name}: {car}")

        elif choice == "2":
            rand_add(fleet)

        elif choice == "3":
            rand_remove(fleet)

        elif choice == "4":
            rand_drive(fleet)

        elif choice == "5":
            rand_refuel(fleet)

        elif choice == "6":
            save_fleet_to_txt(FLEET_FILE, fleet)
            logger.info("Tesztprogram kilépett, flotta elmentve.")
            print("Kilépés... Flotta mentve.")
            break

        elif choice == "7":
            logger.info("Tesztprogram kilépett mentés nélkül.")
            print("Kilépés mentés nélkül.")
            break

        else:
            print("Érvénytelen opció, próbáld újra.")


if __name__ == "__main__":
    test_menu()
