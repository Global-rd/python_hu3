# Car Fleet Manager
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100  # százalék

    def drive(self, km):
        # Negatív távolság ellenőrzése
        if km < 0:
            print("Hiba: a megtett kilométer nem lehet negatív!")
            return

        # 0.1% üzemanyag fogy kilométerenként → km * 0.1
        fuel_needed = km * 0.1

        if fuel_needed > self.fuel_level:
            # Ha nincs elég üzemanyag, annyit megyünk, amennyire elég
            max_km = int(self.fuel_level / 0.1)
            print(f"Nincs elég üzemanyag! Csak {max_km} km-t tudtál menni.")
            self.mileage += max_km
            self.fuel_level = 0
        else:
            self.mileage += km
            self.fuel_level -= fuel_needed

    def refuel(self, amount):
        # amount (százalékban)
        if amount < 0:
            print("Nem lehet negatívat tankolni!")
            return
        
        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100  # Max 100%

    def __str__(self):
        # Kiírás
        return f"{self.brand} {self.model} ({self.year}) - Km: {self.mileage}, Üzemanyag: {self.fuel_level:.1f}%"
    
class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def total_mileage(self):
        # Összes autó km-je
        return sum(car.mileage for car in self.cars)
    
    def show_fleet(self):
        print("\n--- Flotta állapota ---")
        for car in self.cars:
            print(car)
        print(f"Összesített futásteljesítmény: {self.total_mileage()} km")
        print("------------------------\n")
# ------------------------------
# Példa használat
# ------------------------------
if __name__ == "__main__":
    # Autók létrehozása
    car1 = Car("Toyota", "Corolla", 2015)
    car2 = Car("BMW", "X5", 2020)
    car3 = Car("Tesla", "Model 3", 2022)

    # Flotta létrehozása
    fleet = Fleet()

    # Autók hozzáadása
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    # Néhány művelet
    car1.drive(150)
    car1.refuel(20)
    car2.drive(300)
    car3.drive(900)
    car3.refuel(50)
    
    # Flotta állapotának megjelenítése
    fleet.show_fleet()