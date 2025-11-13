class Car:
    def __init__(self, brand, model, year):
        # Initialize car attributes
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  # Starting mileage
        self.fuel_level = 100.0  # Starting fuel level in percentage

    def drive(self, kilometers):
        # Prevent driving negative distances
        if kilometers < 0:
            print("Cannot drive a negative distance.")
            return

        required_fuel = kilometers * 0.1  # 0.1% fuel per km
        if required_fuel <= self.fuel_level:
            self.mileage += kilometers
            self.fuel_level -= required_fuel
            print(f"{self.brand} {self.model} drove {kilometers} km.")
        else:
            max_km = self.fuel_level / 0.1
            self.mileage += max_km
            self.fuel_level = 0
            print(f"{self.brand} {self.model} could only drive {max_km:.1f} km due to low fuel.")

    def refuel(self, amount):
        # Prevent refueling with negative amounts
        if amount < 0:
            print("Cannot refuel a negative amount.")
            return

        self.fuel_level = min(100.0, self.fuel_level + amount)
        print(f"{self.brand} {self.model} refueled to {self.fuel_level:.1f}%.")

    def __str__(self):
        # String representation of the car's current state
        return f"{self.brand} {self.model} ({self.year}) - {self.mileage} km, {self.fuel_level:.1f}% fuel"


class Fleet:
    def __init__(self):
        # Initialize an empty list of cars
        self.cars = []

    def add_car(self, car):
        # Add a car to the fleet
        self.cars.append(car)
        print(f"Added {car.brand} {car.model} to fleet.")

    def remove_car(self, car):
        # Remove a car from the fleet
        if car in self.cars:
            self.cars.remove(car)
            print(f"Removed {car.brand} {car.model} from fleet.")
        else:
            print("Car not found in fleet.")

    def total_mileage(self):
        # Calculate total mileage of all cars in the fleet
        return sum(car.mileage for car in self.cars)

    def show_fleet(self):
        # Display all cars in the fleet
        for car in self.cars:
            print(car)


# example usage
car1 = Car("Toyota", "Corolla", 2018)
car2 = Car("Ford", "Focus", 2020)
car3 = Car("VW", "Passat", 2022)

fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

car1.drive(150)
car2.drive(800)
car3.drive(-50)  # Invalid drive
car2.refuel(30)
car3.refuel(10)

print("\nFleet status:")
fleet.show_fleet()

print(f"\nTotal fleet mileage: {fleet.total_mileage()} km")