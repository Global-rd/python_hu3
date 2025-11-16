# car_fleet_mgr.py

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100  # in percentage

    def drive(self, kilometers):
        fuel_needed = kilometers * 0.1  # 0.1% fuel per km
        max_possible_km = self.fuel_level / 0.1

        if kilometers <= max_possible_km:
            self.mileage += kilometers
            self.fuel_level -= fuel_needed
            print(f"{self.brand} {self.model} drove {kilometers} km.")
        else:
            self.mileage += max_possible_km
            self.fuel_level = 0
            print(f"{self.brand} {self.model} only had enough fuel to drive {max_possible_km:.1f} km.")

    def refuel(self, amount):
        if amount <= 0:
            print("Refuel amount must be positive.")
            return

        new_level = self.fuel_level + amount
        if new_level > 100:
            self.fuel_level = 100
            print(f"{self.brand} {self.model} is now fully refueled (100%).")
        else:
            self.fuel_level = new_level
            print(f"{self.brand} {self.model} refueled to {self.fuel_level:.1f}%.")

    def __str__(self):
        return (f"{self.brand} {self.model} ({self.year}) - Mileage: {self.mileage} km, "
                f"Fuel level: {self.fuel_level:.1f}%")


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Added car: {car.brand} {car.model}")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Removed car: {car.brand} {car.model}")
        else:
            print("Car not found in fleet.")

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def show_fleet_status(self):
        print("\nFleet Status:")
        for car in self.cars:
            print(f"  - {car}")
        print(f"Total mileage of fleet: {self.total_mileage()} km")



