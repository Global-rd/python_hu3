class Car:
    def __init__(self, brand: str, model: str, year: int):
        """
        Initialize a Car object.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100.0  # percentage

    def drive(self, km_traveled: float):
        """
        Increases the car's mileage by the given kilometers
        and decreases the fuel level (0.1% per kilometer).
        The car can only drive as far as its fuel allows.
        """
        if km_traveled <= 0:
            print(f"{self.brand} {self.model}: Distance must be positive.")
            return

        max_distance = self.fuel_level / 0.1  # 0.1% fuel consumption per km

        if km_traveled > max_distance:
            print(f"{self.brand} {self.model}: Could only drive {max_distance:.1f} km — ran out of fuel.")
            km_traveled = max_distance

        self.mileage += km_traveled
        self.fuel_level -= km_traveled * 0.1

        if self.fuel_level < 0:
            self.fuel_level = 0

        print(f"{self.brand} {self.model}: Drove {km_traveled:.1f} km. "
              f"Odometer: {self.mileage:.1f} km, Fuel: {self.fuel_level:.1f}%")

    def refuel(self, amount: float):
        """
        Refuels the car by the given percentage amount.
        Cannot exceed 100%.
        """
        if amount <= 0:
            print(f"{self.brand} {self.model}: Refuel amount must be positive.")
            return

        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100
            print(f"{self.brand} {self.model}: Tank is now full (100%).")
        else:
            print(f"{self.brand} {self.model}: Added +{amount:.1f}%. Current fuel: {self.fuel_level:.1f}%")

    def __str__(self):
        """
        Returns a readable string representation of the car's status.
        """
        return (f"{self.brand} {self.model} ({self.year}) - "
                f"Odometer: {self.mileage:.1f} km, Fuel: {self.fuel_level:.1f}%")


class Fleet:
    def __init__(self):
        """
        Manages a collection of cars.
        """
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)
        print(f"Car added to fleet: {car.brand} {car.model}")

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Car removed from fleet: {car.brand} {car.model}")
        else:
            print("This car is not in the fleet.")

    def total_mileage(self):
        """
        Returns the total mileage of all cars in the fleet.
        """
        return sum(car.mileage for car in self.cars)

    def show_fleet(self):
        """
        Displays the status of all cars in the fleet.
        """
        print("\n--- Fleet Status ---")
        for car in self.cars:
            print(car)
        print(f"Total mileage: {self.total_mileage():.1f} km")
        print("--------------------\n")