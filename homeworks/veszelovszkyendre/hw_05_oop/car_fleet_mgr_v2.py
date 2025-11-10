class Car:
    def __init__(self, brand, model, year, mileage, tank_capacity, fuel_consumption):
        """
        tank_kapacitás: liter
        üzemanyag_fogyasztás: liter / 100 km
        megtett_út: km
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.tank_capacity = tank_capacity
        self.fuel_level = tank_capacity
        self.fuel_consumption = fuel_consumption

    def drive(self, km):
        if km < 0:
            raise ValueError("A megtett távolság (km) nem lehet negatív.")

        max_possible_km = (self.fuel_level / self.fuel_consumption) * 100
        actual_km = min(km, max_possible_km)

        self.mileage += actual_km
        self.fuel_level -= actual_km * self.fuel_consumption / 100
        self.fuel_level = max(self.fuel_level, 0)

        print(
            f"{self.brand} {self.model} megtett {actual_km:.1f} km, üzemanyag szint: {self.fuel_level:.1f} L")

    def refuel(self, liters):
        if liters < 0:
            raise ValueError(
                "A tankolt üzemanyag mennyisége nem lehet negatív.")

        max_fillable = self.tank_capacity - self.fuel_level
        if liters > max_fillable:
            print(
                f"Nem lehet {liters:.1f} L-t tankolni. Maximálisan tankolható mennyiség: {max_fillable:.1f} L")
            self.fuel_level = self.tank_capacity
        else:
            self.fuel_level += liters
            print(
                f"{self.brand} {self.model} megtankolva, üzemanyag szint: {self.fuel_level:.1f} L")

    def __str__(self):
        return (f"{self.brand} {self.model} ({self.year}) - Megtett út: {self.mileage:.1f} km, "
                f"Üzemanyag: {self.fuel_level:.1f}/{self.tank_capacity:.1f} L, Fogyasztás: {self.fuel_consumption} L/100km")


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} hozzáadva a flottához.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} eltávolítva a flottából.")
        else:
            print(f"{car.brand} {car.model} nem található a flottában.")

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def show_fleet(self):
        for car in self.cars:
            print(car)


fleet = Fleet()

num_cars = int(input("Hány autót szeretnél hozzáadni a flottához? "))

for i in range(num_cars):
    print(f"\nAdatok az {i+1}. autóhoz:")
    brand = input("Márka: ")
    model = input("Modell: ")
    year = int(input("Évjárat: "))
    mileage = float(input("Megtett kilométer: "))
    tank_capacity = float(input("Tank kapacitás (L): "))
    fuel_consumption = float(input("Fogyasztás (L/100km): "))

    car = Car(brand, model, year, mileage, tank_capacity, fuel_consumption)
    fleet.add_car(car)

print("\n--- Flotta állapota ---")
fleet.show_fleet()

for car in fleet.cars:
    while True:
        try:
            km_to_drive = float(
                input(f"\nHány km-t szeretnél vezetni a {car.brand} {car.model}-rel? "))
            car.drive(km_to_drive)
            break
        except ValueError as e:
            print(f"Hiba: {e}. Próbáld újra!")

    while True:
        try:
            refuel_amount = float(
                input(f"Hány litert tankolnál a {car.brand} {car.model}-be? "))
            car.refuel(refuel_amount)
            break
        except ValueError as e:
            print(f"Hiba: {e}. Próbáld újra!")

print("\n--- Flotta frissített állapota ---")
fleet.show_fleet()
print(f"\nFlotta összesített kilométer: {fleet.total_mileage():.1f} km")
