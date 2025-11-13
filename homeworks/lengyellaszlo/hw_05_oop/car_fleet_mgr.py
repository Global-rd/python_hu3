from pathlib import Path
import logging
from logging_config import setup_logging
from datetime import datetime
import random

# --- Logger inicializálása ---
setup_logging()
logger = logging.getLogger(__name__)

# --- Fájl elérési útvonalak ---
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
FLEET_FILE = DATA_DIR / "fleet.txt"

# --- Fix márka–típus adatbázis---
CAR_DATABASE = {
    "AUDI": [
        {"model": "A3", "from": 2010, "to": 2018},
        {"model": "A4", "from": 2015, "to": None},
        {"model": "Q5", "from": 2017, "to": None},
        {"model": "TT", "from": 2008, "to": 2020},
    ],
    "BMW": [
        {"model": "X1", "from": 2012, "to": None},
        {"model": "X3", "from": 2014, "to": None},
        {"model": "3 SERIES", "from": 2015, "to": None},
        {"model": "5 SERIES", "from": 2018, "to": None},
    ],
    "MERCEDES": [
        {"model": "C-CLASS", "from": 2014, "to": None},
        {"model": "E-CLASS", "from": 2016, "to": None},
        {"model": "GLA", "from": 2017, "to": None},
        {"model": "S-CLASS", "from": 2013, "to": None},
    ],
    "LEXUS": [
        {"model": "IS", "from": 2013, "to": None},
        {"model": "RX", "from": 2016, "to": None},
        {"model": "NX", "from": 2018, "to": None},
        {"model": "LS", "from": 2012, "to": None},
    ],
}


# --- Car osztály ---
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100
        logger.debug(f"Új autó létrehozva: {self.brand} {self.model} ({self.year})")

    def drive(self, distance):
        """Növeli a megtett kilométert és csökkenti az üzemanyagot."""
        if not isinstance(distance, int) or distance <= 0:
            logger.warning("A megtett távolság csak pozitív egész szám lehet.")
            print("Hiba: a megtett távolság csak pozitív egész szám lehet.")
            return

        fuel_needed = distance * 0.1
        if fuel_needed > self.fuel_level:
            possible_distance = int(self.fuel_level / 0.1)
            self.mileage += possible_distance
            self.fuel_level = 0
            logger.warning(
                f"Nincs elegendő üzemanyag. Csak {possible_distance} km-t tudott megtenni."
            )
            print(
                f"Nincs elegendő üzemanyag. Csak {possible_distance} km-t tudtál megtenni."
            )
        else:
            self.mileage += distance
            self.fuel_level -= fuel_needed
            logger.info(
                f"{self.brand} {self.model} {distance} km-t ment. "
                f"Új óraállás: {self.mileage} km, üzemanyag: {self.fuel_level:.1f}%"
            )

    def refuel(self, amount):
        """Tankolás - nem enged több üzemanyagot, mint amennyi hely van a tankban."""
        if amount <= 0:
            logger.warning("A tankolás mennyisége nem lehet nulla vagy negatív.")
            print("A tankolás mennyisége nem lehet nulla vagy negatív.")
            return

        available_space = 100 - self.fuel_level
        if amount > available_space:
            logger.error(f"Túl sok üzemanyag. Csak {available_space:.1f}% hely van a tankban.")
            print(f"Hiba: csak {available_space:.1f}% hely van a tankban.")
            return

        self.fuel_level += amount
        logger.info(
            f"{self.brand} {self.model} tankolva: +{amount}%. "
            f"Üzemanyagszint: {self.fuel_level:.1f}%"
        )
        print(f"Tankolás sikeres. Jelenlegi üzemanyagszint: {self.fuel_level:.1f}%")

    def __str__(self):
        # Kiírásnál az első betű nagy, a többi kicsi
        return (
            f"{self.brand.upper()} {self.model.upper()} ({self.year}) | "
            f"{int(self.mileage)} km | {self.fuel_level:.1f}% üzemanyag"
        )


# --- Fleet osztály ---
class Fleet:
    def __init__(self, cars=None, next_id=1):
        self.cars = cars if cars else {}
        self.next_id = next_id

    def add_car(self, brand, model, year):
        name = f"car{self.next_id}"
        self.cars[name] = Car(brand, model, year)
        logger.info(f"Új autó hozzáadva: {name} - {brand} {model} ({year})")
        print(f"Autó hozzáadva: {name} - {brand.upper()} {model.upper()} ({year})")
        self.next_id += 1

    def remove_car(self, car_name):
        if car_name not in self.cars:
            logger.warning(f"Törlés sikertelen, nincs ilyen autó: {car_name}")
            print("Nincs ilyen autó a flottában.")
            return
        removed_car = self.cars.pop(car_name)
        logger.info(f"Autó törölve: {car_name} - {removed_car.brand} {removed_car.model}")
        print(f"Autó törölve: {car_name} - {removed_car.brand.upper()} {removed_car.model.upper()}")

    def fleet_stats(self, brand=None):
        if brand:
            selected = [car for car in self.cars.values() if car.brand == brand.upper()]
            if not selected:
                print(f"Nincs autó a flottában ezzel a márkával: {brand.upper()}")
                return
            print(f"\n{brand.upper()} márka statisztika:")
        else:
            selected = list(self.cars.values())
            if not selected:
                print("A flotta üres.")
                return
            print("\nTeljes flotta statisztika:")

        total_cars = len(selected)
        total_km = sum(int(car.mileage) for car in selected)
        avg_fuel = sum(car.fuel_level for car in selected) / total_cars
        avg_year = sum(car.year for car in selected) / total_cars
        avg_age = datetime.now().year - avg_year

        print(f"Autók száma: {total_cars}")
        print(f"Összes km: {total_km}")
        print(f"Átlagos üzemanyagszint: {avg_fuel:.1f}%")
        print(f"Átlagos életkor: {avg_age:.1f} év")
        logger.info(f"Statisztika lekérve ({'márka: ' + brand if brand else 'teljes flotta'})")


# --- Fájlműveletek ---
def read_fleet_from_txt(filename):
    cars = {}
    max_id = 0
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                if len(parts) < 6:
                    continue
                car_name, brand, model, year, mileage, fuel = parts
                car = Car(brand, model, int(year))
                car.mileage = int(float(mileage))
                car.fuel_level = float(fuel)
                cars[car_name] = car
                try:
                    num = int(car_name.replace("car", ""))
                    if num > max_id:
                        max_id = num
                except ValueError:
                    continue
        logger.info(f"Flotta beolvasva {len(cars)} autóval. Következő ID: car{max_id + 1}")
        print(f"{len(cars)} autó beolvasva a flottába.")
    except FileNotFoundError:
        logger.warning("A flotta fájl nem található. Üres flotta indul.")
        print("Nem található korábbi flotta, új flotta indul.")
    return Fleet(cars=cars, next_id=max_id + 1)


def save_fleet_to_txt(filename, fleet):
    with open(filename, "w", encoding="utf-8") as f:
        for name, car in fleet.cars.items():
            f.write(f"{name};{car.brand};{car.model};{car.year};{int(car.mileage)};{car.fuel_level}\n")
    logger.info(f"Flotta mentve: {len(fleet.cars)} autó -> {filename}")
    print("Flotta sikeresen mentve.")


# --- Felhasználói adatbekérés ---
def get_car_input():
    print("\nElérhető márkák:")
    for brand in CAR_DATABASE.keys():
        print(" -", brand.upper())
    brand = input("Válassz egy márkát: ").strip().upper()
    if brand not in CAR_DATABASE:
        print("Hibás márka. A megadott márka nem található az adatbázisban.")
        logger.warning(f"Ismeretlen márka megadva: {brand}")
        return None

    print(f"\nElérhető típusok a {brand.upper()} márkánál:")
    available_models = [record["model"] for record in CAR_DATABASE[brand]]
    print(" - " + ", ".join([m.upper() for m in available_models]))
    model = input("Válassz egy típust: ").strip().upper()
    if model not in available_models:
        print("Hibás modell. A megadott típus nem található ennél a márkánál.")
        logger.warning(f"Ismeretlen modell: {brand} {model}")
        return None

    record = next(r for r in CAR_DATABASE[brand] if r["model"] == model)
    from_year = record["from"]
    to_year = record["to"]
    current_year = datetime.now().year

    year_input = input("Add meg a gyártási évet: ").strip()
    if not year_input.isdigit():
        print("A gyártási évnek egész számnak kell lennie.")
        logger.warning("Hibás gyártási év (nem szám).")
        return None

    year = int(year_input)
    if year < from_year:
        print(f"Hiba: a {model.upper()} típust csak {from_year}-től gyártják.")
        logger.warning(f"Túl korai gyártási év: {year} ({brand} {model})")
        return None
    if to_year is not None and year > to_year:
        print(f"Hiba: a {model.upper()} típust {to_year}-ig gyártották, nem {year}-ben.")
        logger.warning(f"Túl késői gyártási év: {year} ({brand} {model})")
        return None
    if year > current_year + 1:
        print("Hiba: a gyártási év nem lehet a jövőben.")
        logger.warning(f"Jövőbeli gyártási év megadva: {year}")
        return None

    logger.info(f"Új autó adatainak megadása: {brand} {model} ({year})")
    return brand, model, year


# --- Menü ---
def main_menu():
    fleet = read_fleet_from_txt(FLEET_FILE)

    while True:
        print("\n--- AUTÓFLOTTA KEZELŐ ---")
        print("1. Flotta megtekintése")
        print("2. Új autó hozzáadása")
        print("3. Autó törlése")
        print("4. Autó vezetése")
        print("5. Autó tankolása")
        print("6. Flotta statisztika")
        print("7. Márka statisztika")
        print("8. Kilépés (mentéssel)")

        choice = input("Válassz egy opciót (1-8): ").strip()

        if choice == "1":
            if not fleet.cars:
                print("A flotta üres.")
                continue
            print("\n--- FLOTTA TARTALMA ---")
            for name, car in fleet.cars.items():
                print(f"{name}: {car}")
            logger.info("Flotta megtekintése lefutott.")

        elif choice == "2":
            brand_input = input("Add meg a márkát : ").strip()

            result = get_car_input()
            if result:
                brand, model, year = result
                fleet.add_car(brand, model, year)
            else:
                print("Autó hozzáadása megszakítva hibás adatok miatt.")
                logger.warning("Autó hozzáadása megszakadt hibás input miatt.")

        elif choice == "3":
            if not fleet.cars:
                print("A flotta üres, nincs mit törölni.")
                continue

            print("Jelenlegi autók:")
            for name, car in fleet.cars.items():
                print(f" - {name}: {car.brand.upper()} {car.model.upper()} ({car.year})")

            car_name = input("Add meg a törlendő autó azonosítóját (pl. car1): ").strip()
            fleet.remove_car(car_name)

        elif choice == "4":
            if not fleet.cars:
                print("A flotta üres, nincs mit vezetni.")
                continue

            print("Elérhető autók:")
            for name, car in fleet.cars.items():
                print(f" - {name}: {car}")

            car_name = input("Add meg az autó azonosítóját: ").strip()
            if car_name not in fleet.cars:
                print("Nincs ilyen autó a flottában.")
                continue

            try:
                distance = int(input("Add meg, hány km-t szeretnél menni: ").strip())
                fleet.cars[car_name].drive(distance)
            except ValueError:
                print("Érvénytelen érték, egész számot adj meg.")

        elif choice == "5":
            if not fleet.cars:
                print("A flotta üres, nincs mit tankolni.")
                continue

            print("Elérhető autók:")
            for name, car in fleet.cars.items():
                print(f" - {name}: {car}")

            car_name = input("Add meg az autó azonosítóját: ").strip()
            if car_name not in fleet.cars:
                print("Nincs ilyen autó a flottában.")
                continue

            try:
                amount = float(input("Add meg a tankolás mennyiségét (%): ").strip())
                fleet.cars[car_name].refuel(amount)
            except ValueError:
                print("Érvénytelen érték, számot adj meg.")

        elif choice == "6":
            fleet.fleet_stats()

        elif choice == "7":
            if not fleet.cars:
                print("A flotta üres.")
                continue

            available_brands = sorted({car.brand.upper() for car in fleet.cars.values()})
            print("Elérhető márkák a flottában:", ", ".join(available_brands))
            brand = input("Add meg a márkát: ").strip().upper()
            fleet.fleet_stats(brand)

        elif choice == "8":
            save_fleet_to_txt(FLEET_FILE, fleet)
            logger.info("Program kilépett, flotta elmentve.")
            print("Kilépés... Flotta mentve.")
            break

        else:
            print("Érvénytelen opció, próbáld újra.")
            logger.warning("Ismeretlen menüpont választva.")


if __name__ == "__main__":
    main_menu()
