class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0            # induló érték
        self.fuel_level = 100       # induló érték (százalékban)

    def drive(self, distance: float):
        fuel_needed = distance * 0.1  # 0.1% fogy km-enként

        if fuel_needed > self.fuel_level:
            max_distance = self.fuel_level / 0.1
            print(f"Nincs elég üzemanyag! Csak {max_distance:.1f} km-t tudsz megtenni.")
            self.mileage += max_distance
            self.fuel_level = 0
        else:
            self.mileage += distance
            self.fuel_level -= fuel_needed
            print(f"{distance} km megtéve. Üzemanyag szint: {self.fuel_level:.1f}%.")

    def refuel(self, amount: float):
        """Tankolás növeli az üzemanyagszintet, de 100% fölé nem engedi."""
        if amount <= 0:
            print("A tankolás mennyisége legyen pozitív!")
            return

        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100

        print(f"Tankolva. Jelenlegi üzemanyagszint: {self.fuel_level:.1f}%.")

    def __str__(self):
        """Felhasználóbarát kiírás"""
        return f"{self.brand} {self.model} ({self.year}) - {self.mileage:.1f} km, {self.fuel_level:.1f}% üzemanyag"
    
class Fleet:
    def __init__(self):
        """Flotta létrehozása (autók listája)"""
        self.cars = []

    def add_car(self, car: Car):
        """Autó hozzáadása a flottához"""
        self.cars.append(car)
        print(f"{car.brand} {car.model} hozzáadva a flottához.")

    def remove_car(self, car: Car):
        """Autó eltávolítása a flottából"""
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} eltávolítva a flottából.")
        else:
            print("Az autó nincs a flottában!")

    def total_mileage(self):
        """A flotta összes autójának összesített kilométere"""
        return sum(car.mileage for car in self.cars)

    def show_fleet(self):
        """A flotta autóinak listázása"""
        print("\nFlotta tartalma:")
        for car in self.cars:
            print(f" - {car}")

c1=Car("Opel", "Astra", 2015 )
c2=Car("Ford", "Focus", 2015 )
fl = Fleet()
fl.add_car(c1); fl.add_car(c2)

c1.drive(120)
c2.drive(50)
c2.refuel(20)
fl.show_fleet()
print(f"\nÖsszesített kilométer: {fl.total_mileage():.1f} km")
