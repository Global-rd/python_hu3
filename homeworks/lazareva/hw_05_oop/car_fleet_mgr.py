from datetime import datetime as dt

class NotPositiveAmountError(Exception):
    """
    Custom exception for invalid amount on deposit/withdraw.
    """
    pass

class NotEnoughFuelError(Exception):
    """
    Custom exception for insufficient funds on withdraw.
    """
    pass

class FuelLimitError(Exception):
    """
    Custom exception for insufficient funds on withdraw.
    """
    pass

class Car:
    def __init__(self, brand: str, model: str, year: int, mileage: float=0.0, fuel_level: float=100.0) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def drive(self, distance: float) -> None:
        if distance <= 0:
            raise NotPositiveAmountError("Distance must be positive!")
        fuel_needed = distance * 0.1  # 10 km/liter
        if fuel_needed > self.fuel_level:
            raise NotEnoughFuelError("Not enough fuel to drive the requested distance.")
        self.mileage += distance
        self.fuel_level -= fuel_needed

    def refuel(self, amount: float) -> None:
        if amount <= 0:
            raise NotPositiveAmountError("Refuel amount must be positive!")

        max_amount = 100.0 - self.fuel_level
        if max_amount < amount:
            raise FuelLimitError(f"Only {max_amount} % fuel can be added into the tank.")
        self.fuel_level += amount

# Car instances - test drive and refuel
print("----1. Car instances - without fleet management")
car_1 = Car(brand="Audi", model="e-tron GT", year=2021)
car_2 = Car(brand="BMW", model="i4", year=2022)
car_2.drive(150)

print(f"car_2.mileage: {car_2.mileage}")
print(f"car_2.fuel_level: {car_2.fuel_level}")

class Fleet:

    cars_count = 0

    def __init__(self, name: str, cars: list[Car]) -> None:
        self.name = name #fleet of foot"
        self.cars = cars
        Fleet.cars_count += len(cars)
        self.fleet_history = []

    def add_car(self, car: Car) -> None:
        self.cars.append(car)
        Fleet.cars_count += 1
        self.fleet_history.append({
            "date": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": "ADD_CAR",
            "car": f"{car.brand} {car.model} ({car.year})"
        })
   
    def remove_car(self, car: Car) -> None:
        if car not in self.cars:
            print(f"{car.brand} {car.model} ({car.year}) is not in the fleet.")
            return
        self.cars.remove(car)
        Fleet.cars_count -= 1
        self.fleet_history.append({
            "date": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": "RMV_CAR",
            "car": f"{car.brand} {car.model} ({car.year})"
        })

    def get_mileage_total(self) -> float:
        total_mileage = 0.0
        for car in self.cars:
            total_mileage += car.mileage
        return total_mileage

    def get_fleet_info(self) -> str:
        info = f"Information for '{self.name}' :\n"
        if not self.cars:
            info += "    No cars in the fleet.\n"
        for car in self.cars:
            info += (f"    {car.brand} {car.model} ({car.year}) - "
                     f"Mileage: {car.mileage} km, Fuel Level: {car.fuel_level}%\n")
        return info
    
    def get_fleet_history(self) -> str:
        if not self.fleet_history:
            return "No cars in the fleet.\n"
        history = f"History for '{self.name}' :\n"
        for record in self.fleet_history:
            history += (f"    {record['date']} - {record['type']} - {record['car']})\n")
        return history

"""
Fleet management test drive and refuel
"""

# Fleet management    
fleet = Fleet(name="Fleet of Foot", cars=[])

# üres history
print("\n----2. Empty fleet history")
fleet_history = fleet.get_fleet_history()    
print(fleet_history)

# korábban felvett autók hozzáadása a flottához 
fleet.add_car(car_1)
fleet.add_car(car_2) 

# flotta aktuális állapota
print("----3. Fleet info after adding cars")
print(fleet.get_fleet_info())

# flotta összes autó száma
print(f"Total cars in fleet: {Fleet.cars_count}")

# flotta összesített km
mileage_total = fleet.get_mileage_total()
print(f"Total mileage of fleet: {mileage_total} km\n") 

# új autó felvétele (még nincs a flottában)
print("----4. Fleet info before adding a new car (car_3)" )
car_3 = Car(brand="Toyota", model="Prius", year=2020, fuel_level=50.0)

print(fleet.get_fleet_info())
print(f"Total cars in fleet: {Fleet.cars_count}")

mileage_total = fleet.get_mileage_total()
print(f"Total mileage of fleet: {mileage_total} km\n") 

# új autó hozzáadása, egy autó eltávolítása, vezetés, tankolás
print("----5. Fleet info after adding a new car (car_3) and removing car_2. Plus drive and refuel" )
fleet.remove_car(car_2) 
fleet.add_car(car_3) 
car_3.drive(120)
car_3.refuel(37)

print("--- After updates ---")
print(f"Car_3 mileage: {car_3.mileage}")
print(f"Car_3 fuel level: {car_3.fuel_level}")
car_1.drive(200)

print(fleet.get_fleet_info())
print(f"Total cars in fleet: {Fleet.cars_count}")

mileage_total = fleet.get_mileage_total()
print(f"Total mileage of fleet: {mileage_total} km") 

fleet_history = fleet.get_fleet_history()
print(fleet_history)

try:
    car_3.refuel(-200)
except NotPositiveAmountError as e:
    print(e)

try:
    car_3.refuel(5000)
except FuelLimitError as e:
    print(e) 

try:
    car_3.drive(-30)
except NotPositiveAmountError as e:
    print(e) 

try:
    car_3.drive(1000)
except NotEnoughFuelError as e:
    print(e) 

fleet.remove_car(car_2) # removing a car which is not in the fleet 