class car:
    def __init__(self, brand, modell, year,mileage=0,fuel_level=100):
        self.barnd = brand
        self.modell = modell
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level
    def drive(self, distance):
        self.mileage += distance
        self.fuel_level -= distance / 10
        if self.fuel_level < 0:
            self.fuel_level = 0
            print(f'Drove {distance} km. Mileage is now {self.mileage} km. Fuel level is now {self.fuel_level}%.')
    def refuel(self, amount):
        self.fuel_level += amount
        if self.fuel_level > 100 and amount > 0:
            self.fuel_level = amount
        print(f'Refueled {amount}%. Fuel level is now {self.fuel_level}%.')
class Fleet(car):
    def __init__(self):
        self.cars = []
    def add_car(self, car):
        self.cars.append(car)    
    def remove_car(self, car):
        self.cars.remove(car)
    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        return total
car1 = car('Toyota', 'Corolla', 2020, 15000, 80)
car2 = car('Honda', 'Civic', 2019, 20000, 60)
fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
print(f'Fleet has {len(fleet.cars)} cars.')
print(f'Total mileage of fleet: {fleet.total_mileage()} km.')
print(f'Car 1 mileage before driving: {car1.mileage} km, fuel level: {car1.fuel_level}%.')
print(f'Car 2 mileage before driving: {car2.mileage} km, fuel level: {car2.fuel_level}%.')
car1.drive(100)
car1.refuel(30)
car2.drive(150)
car2.refuel(50)
print(f'Car 1 mileage before driving: {car1.mileage} km, fuel level: {car1.fuel_level}%.')
print(f'Car 2 mileage before driving: {car2.mileage} km, fuel level: {car2.fuel_level}%.')




