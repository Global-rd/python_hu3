class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, km):
        max_possible_km = self.fuel_level / 0.1
        actual_km = min(km, max_possible_km)

        self.mileage += actual_km
        self.fuel_level -= actual_km * 0.1
        self.fuel_level = max(self.fuel_level, 0)

        print(
            f"{self.brand} {self.model} drove {actual_km:.1f} km, fuel level: {self.fuel_level:.1f}%")

    def refuel(self, amount):
        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100
        print(f"{self.brand} {self.model} refueled, fuel level: {self.fuel_level:.1f}%")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - Mileage: {self.mileage:.1f} km, Fuel: {self.fuel_level:.1f}%"


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Added {car.brand} {car.model} to fleet.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Removed {car.brand} {car.model} from fleet.")
        else:
            print(f"{car.brand} {car.model} not found in fleet.")

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def show_fleet(self):
        for car in self.cars:
            print(car)


car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Focus", 2021)

fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

print("\n--- Initial Fleet ---")
fleet.show_fleet()

car1.drive(150)  # Toyota
car2.drive(300)  # Honda
car3.drive(50)   # Ford

car2.refuel(20)
car3.refuel(10)

print("\n--- Updated Fleet ---")
fleet.show_fleet()

print(f"\nTotal fleet mileage: {fleet.total_mileage():.1f} km")
