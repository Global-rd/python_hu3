
FUEL_CONSUMPTION = 0.1

class Car:  
    def __init__(self, brand: str, model: str, year: int , mileage :int =  0, fuel_level: float=100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level
        
    
    def drive(self, distance: int):        
        if distance < 0:
            raise ValueError("A megtett távolság nem lehet negatív")
        max_distance = self.fuel_level / FUEL_CONSUMPTION        
        km = min(max_distance,distance)
        fuel = km * FUEL_CONSUMPTION
        self.mileage += km
        self.fuel_level -=fuel     

    def refuel(self, refuel: int):
        if refuel < 0:
            raise ValueError("A tankolás mennyisége nem lehet negatív")
        max_reload = 100 - self.fuel_level
        if (refuel > max_reload):
            self.fuel_level = 100
            return
        self.fuel_level += refuel
    
    def __str__(self) -> str:
        return f"{self.brand} {self.model} - {self.year} - {self.mileage} - {self.fuel_level}%"
class Fleet:
    cars = []
    def __init__(self, name: str) -> None:
        self.name = name
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def remove_car(self, car: Car):
         self.cars.remove(car)

    def list_cars(self):
        print(f"Cars in {self.name}:")
        for car in self.cars:             
            print(car)
            
    def total_mileage(self):
        ttl_mileage = 0
        for car in self.cars:
            ttl_mileage += car.mileage
        return ttl_mileage
            
def main():
    car1 = Car("Mazda","3",1999,55555,100)
    car2 = Car("Hyundai","Tucson",2017,160000,30)
    car3 = Car("Toyota","Auris",2014,120000,80)

    print("--------------")

    fleet1 = Fleet("Teszt1")
    fleet1.add_car(car1)
    fleet1.add_car(car2)
    fleet1.add_car(car3)

    fleet1.list_cars()

    print("--------------")
    
    car2.drive(25)
    car3.refuel(40)        
    try:
        car3.drive(-10)
    except ValueError as e:
        print(f"Hibás paraméter: {e}")
    try:
        car1.refuel(-23)        
    except ValueError as e:
        print(f"Hibás paraméter: {e}")
    print("--------------")
    fleet1.list_cars()    

    print("--------------")
    print(f"Total km: {fleet1.total_mileage()}")

    fleet1.remove_car(car2)
    print("--------------")
    fleet1.list_cars()    


main()