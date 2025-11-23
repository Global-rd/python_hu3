#Készíts egy Car osztályt, amely rendelkezik a következő tulajdonságokkal
class Car:

#Egy konstruktor, amely beállítja a fenti attribútumokat:
    def __init__(self, Brand, Model, Year, Mileage = 0, Fuel_level = 100):
        self.Car = Car
        self.Brand = Brand
        self.Model = Model
        self.Year = Year
        self.Mileage = Mileage
        self.Fuel_level = Fuel_level

#Egy drive() metódus 1km = 0.1% uzemanyag
    def drive(self, distance):
        max_distance = self.Fuel_level / 0.1 
        if distance > max_distance:
            print(f"Not enough fuel for {distance} km. You can drive only {max_distance:.1f} km.")
            distance =- max_distance

#Egy refuel() metódus, amely feltölti az üzemanyag-szintet egy adott mennyiséggel.
    def refuel (self, fuel):
        if fuel <= 0:
            Print("Invalid amount, it should be positive")
        self.Fuel_level += fuel
        if self.Fuel_level > 100 and fuel > 0:
            self.Fuel_level = fuel
        print(f"Fuel amended {fuel}%. Fuel level is {self.Fuel_level}%. now")

#Készíts egy Fleet osztályt, amely kezeli a Car objektumokat: 
class Fleet:
#Az osztály rendelkezzen egy listával, amelyben az autók találhatóak. 
    def __init__(self):
        self.cars = []
#Tartalmazzon metódusokat Car objektumok hozzáadására és eltávolítására a flottába/flottából
    def add_car(self, Car):
        self.cars.append(Car)
    def remove_car(self, Car):
        for Car in self.cars:
            if Car == Car:
                self.cars.remove(Car)
                break
#Tartalmazzon egy metódust, amely összesíti a flotta összes autójának összes kilométerét. 
    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        return total
    
#Hozz létre néhány Car objektumot 
car1 = Car(Brand="Opel", Model="Vectra", Year=2005, Mileage=35000, Fuel_level=50)
car2 = Car(Brand="Ford", Model="Focus", Year=2010, Mileage=25000, Fuel_level=60)
car3 = Car(Brand="Skoda", Model="Kodiaq", Year=2020, Mileage=10000, Fuel_level=100)

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
print(f"{self.Car} start mileage: {self.Mileage} km, fuel level: {self.Fuel_level}%.")
