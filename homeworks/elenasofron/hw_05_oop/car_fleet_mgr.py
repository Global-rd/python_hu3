#Készíts egy Car osztályt, amely rendelkezik a következő tulajdonságokkal
class Car:

#Egy konstruktor, amely beállítja a fenti attribútumokat:
    def __init__(self, brand, model, year, mileage = 0, fuel_level = 100):
        # self.Car = Car
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

#Egy drive() metódus 1km = 0.1% uzemanyag
    def drive(self, distance):
        max_distance = self.fuel_level / 0.1 
        if distance > max_distance:
            print(f"Not enough fuel for {distance} km. You can drive only {max_distance:.1f} km.")
            distance =- max_distance

#Egy refuel() metódus, amely feltölti az üzemanyag-szintet egy adott mennyiséggel.
    def refuel (self, fuel):
        if fuel <= 0:
            Print("Invalid amount, it should be positive")
        self.fuel_level += fuel
        if self.fuel_level > 100 and fuel > 0:
            self.fuel_level = fuel
        print(f"Fuel amended {fuel}%. Fuel level is {self.fuel_level}%. now")

#Készíts egy Fleet osztályt, amely kezeli a Car objektumokat: 
class Fleet:
#Az osztály rendelkezzen egy listával, amelyben az autók találhatóak. 
    def __init__(self):
        self.cars = []
#Tartalmazzon metódusokat Car objektumok hozzáadására és eltávolítására a flottába/flottából
    def add_car(self, car):
        self.cars.append(car)
    def remove_car(self, car):
        for car in self.cars:
            if car == car:
                self.cars.remove(car)
                break
#Tartalmazzon egy metódust, amely összesíti a flotta összes autójának összes kilométerét. 
    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        return total
    
#Hozz létre néhány Car objektumot 
car1 = Car(brand="Opel", model="Vectra", year=2005, mileage=35000, fuel_level=50)
car2 = Car(brand="Ford", model="Focus", year=2010, mileage=25000, fuel_level=60)
car3 = Car(brand="Skoda", model="Kodiaq", year=2020, mileage=10000, fuel_level=100)

Fleet = Fleet()
Fleet.add_car(car1)
Fleet.add_car(car2)
Fleet.add_car(car3)

#hajts végre néhány műveletet (vezetés, tankolás)
car1.drive(100)
car1.refuel(30)
car2.drive(150)
car2.refuel(50)
car3.drive(200)
car3.refuel(20)

#jelenítsd meg az autók  állapotát és a flotta összesítő adatait.
print(f"Fleet has {len(Fleet.cars)} cars.")
print(f"Start mileage: {car1.mileage} km, fuel level: {car1.fuel_level}%.")
print(f"Start mileage: {car2.mileage} km, fuel level: {car2.fuel_level}%.")
print(f"Start mileage: {car3.mileage} km, fuel level: {car3.fuel_level}%.")
