class InvalidFuelError(Exception):
    pass

class InvalidReFuelError(Exception):
    pass

class Car:
    def __init__(self, make, model, manufacture_year, odometer, fuel_level):
        self.make = make
        self.model = model
        self.manufacture_year = manufacture_year
        self.odometer = odometer
        self.fuel_level = fuel_level
    
    def drive(self, drive_distance):
        max_distance = self.fuel_level / 0.1 
        if drive_distance > max_distance:
            print(f"Not enough fuel for {drive_distance} km.")
        else:
            print(f"You drove {drive_distance} km with {self.make} {self.model}. You used {drive_distance / 10}% of the fuel.")
            self.fuel_level -= drive_distance / 10
            self.odometer += drive_distance
        
    def refuel(self, amount):
        if amount <= 0:
            raise InvalidFuelError("Fuel amount must be positive.")
        elif self.fuel_level + amount > 100:
            raise InvalidReFuelError("You cant refuel this amount. To much!")

        else:
            self.fuel_level += amount
            print(f"Added {amount}% to the tank of {self.make} {self.model}. Fuel leve is now {self.fuel_level}%")
        
    def __str__(self):
        return f"{self.make} {self.model} {self.manufacture_year} {self.odometer}km {float(self.fuel_level)}%"

class Fleet:
    def __init__(self, fleet_name):
        self.fleet_name = fleet_name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        for x in self.cars:
            if x == car:
                self.cars.remove(car)
    
    def total_km(self):
        total = 0
        for car in self.cars:
            total += car.odometer
        return total
    
    def list_cars(self):
        
        for car in self.cars:
            print(car)