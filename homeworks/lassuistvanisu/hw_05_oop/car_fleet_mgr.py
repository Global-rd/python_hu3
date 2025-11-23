class InvalidNumberError(Exception):
    """
    Egyedi hiba kezelés, ha negatív vagy 0 km adatot ad
    """
    pass


class Car:

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100 # %

    #Létrehozza a vezetést, azaz a km  és üzemanyag változást
    def drive(self, km):
        max_km = self.fuel_level / 0.1  # Mivel 1 km = 0.1% 1000 km-t tud megtenni teljesen feltöltve
        if km <= 0:
            raise InvalidNumberError("The mileage must be positive!")
        
        if km > max_km:
            print(f"You can't drive {km} km, you only have fuel for {int(max_km)} km. That's how far you can drive!")
            km = int(max_km)
        
        fuel_needed = km * 0.1
        self.mileage += km
        self.fuel_level -= fuel_needed
        
        if self.fuel_level < 0:
            self.fuel_level = 0
        print(f"Drived: {km} km. Current odometer: {self.mileage} km, fuel level: {self.fuel_level:.1f}%")

    #Feltölti az üzemanyagot maximum 100%-ra
    def refuel(self, amount):
        if amount <= 0:
            raise InvalidNumberError("The refueling amount must be positive!")

        self.fuel_level += amount

        if self.fuel_level > 100:
            self.fuel_level = 100
        print(f"Refueld: {amount}%. Current fuel level: {self.fuel_level:.1f}%")
    
    # Meghatározza a print(car) formátumát
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.mileage} km, fuel: {self.fuel_level:.1f}%"

class Fleet:
    #Inicializálás, üres autólista létrehozás
    def __init__(self):
        self.cars = []

    #Autó hozzáadása a flottához
    def add_car(self, car):
        self.cars.append(car)
        print(f"Added in fleet: {car}")

    #Autó eltávolítása a flottából
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Removed from fleet: {car}")
        else:
            print(f"The car cannot be found in the fleet: {car}")
    
    #Flotta összesített kilométere
    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    #Teljes flotta kiírás
    def show_fleet(self):
        
        if not self.cars:
            print("No cars added to the fleet.")
        for car in self.cars:
            print(car)

