
class Car:
    def __init__(self, brand, model, year, mileage=0, fuel_level=100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def drive(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        elif distance * 0.1 > self.fuel_level:            
            self.mileage += self.fuel_level * 10
            self.fuel_level = 0         
            #raise ValueError("Not enough fuel to drive the requested distance.")
        else:
            self.mileage += distance
            self.fuel_level -= distance * 0.1  # Assume fuel consumption rate

    def refuel(self, amount):
        if amount < 0:
            raise ValueError("Refuel amount cannot be negative.")
        elif self.fuel_level + amount > 100:
            self.fuel_level = 100
            #raise ValueError("Fuel level cannot exceed 100%.")  
        else:
            self.fuel_level = min(100, self.fuel_level + amount)

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}, Mileage: {self.mileage} km , Fuel Level: {self.fuel_level}%"    
    
class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError("Only Car instances can be added to the fleet.")
        self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
        else:
            raise ValueError("Car not found in the fleet.")

    def get_total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def __str__(self):
        return "\n".join(str(car) for car in self.cars)
    
if __name__ == "__main__":
    car1 = Car("Opel", "Zafira", 2018, mileage=190000, fuel_level=20)
    car2 = Car("Skoda", "Octavia", 2014, mileage=240000, fuel_level=50)

    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)

    print("Fleet before driving:")
    print(fleet)

    try:
        car1.drive(300)
    except ValueError as e:
        print(e)

    car2.refuel(30)

    print("\nFleet after driving and refueling:")
    print(fleet)

    print(f"\nTotal mileage of the fleet: {fleet.get_total_mileage()} km")