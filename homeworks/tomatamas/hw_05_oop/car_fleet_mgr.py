class Car:
    """
    Egyszerű autó-osztály.
    A fuel_level százalékban megadott érték
    A fogyasztás 0.1% üzemanyag / km
    """

    consumption_percent_per_km = 0.1

    def __init__(self, brand:str, model:str, year:int, mileage:float = 0, fuel_level:int = 100.0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = float(mileage)
        # 0–100 közé korlátozzuk a fuel_levelt
        if fuel_level < 0:
            fuel_level = 0
        elif fuel_level > 100:
            fuel_level = 100
        self.fuel_level = fuel_level

    def __repr__(self):
        return f"{self.year} {self.brand} {self.model} – {self.mileage:.1f} km, üzemanyag: {self.fuel_level:.1f}%"

    def drive(self, kms):
        # Megpróbál kms kilométert menni. Ha nincs elég üzemanyag, csak amennyire elég
        if kms <= 0:
            return 0.0
        
        # kiszámoljuk, mennyit tudna megtenni
        max_km = self.fuel_level / self.consumption_percent_per_km
        driven = min(kms, max_km)

        # frissítjük az adatokat
        self.mileage += driven
        self.fuel_level -= driven * self.consumption_percent_per_km

        # biztonsági korlát
        if self.fuel_level < 0:
            self.fuel_level = 0
        if self.fuel_level > 100:
            self.fuel_level = 100

        return driven
    
    def refuel(self, amount):
        # Tankolás adott mennyiséggel, de max 100%-ig
        if amount <= 0:
            return 0.0

        space_left = 100 - self.fuel_level
        added = min(amount, space_left)
        self.fuel_level += added

        if self.fuel_level > 100:
            self.fuel_level = 100

        return added

class Fleet:
    """Flotta kezelő osztály"""

    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, model):
        # Eltávolít egy autót a modell neve alapján
        for car in self.cars:
            if car.model == model:
                self.cars.remove(car)
                return True
        print(f"Nincs ilyen autó a flottában: {model}")
        return False

    def list_cars(self):
        print(f"A {self.name} flotta autóinak listája:")

        if len(self.cars) == 0:
            print("Nincs autó a flottában!")
        else:
            for car in self.cars:
                print("-----")
                print(f"Márka: {car.brand}")
                print(f"Modell: {car.model}")
                print(f"Gyártási év: {car.year}")
                print(f"Kilométeróra állás: {car.mileage:.1f} km")
                print(f"Üzemanyagszint: {car.fuel_level:.1f}%")

    def total_mileage(self):
        # Összes kilométer a flottában
        total = 0
        for car in self.cars:
            total += car.mileage
        return total
    
car_1 = Car(brand="Mazda", model="CX30", year=2015, mileage=98767, fuel_level=50)
car_2 = Car(brand="Toyota", model= "Yaris", year=2013, mileage=118755)

fleet_1 = Fleet(name="Flotta 1")

fleet_1.add_car(car_1)
fleet_1.add_car(car_2)

fleet_1.list_cars()

fleet_1.remove_car("Yaris")

fleet_1.list_cars()