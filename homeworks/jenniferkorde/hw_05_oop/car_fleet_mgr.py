class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0        
        self.fuel_level = 100.0 

    
    def drive(self, distance_km):
        
        fuel_per_km = 0.1
        max_distance = self.fuel_level / fuel_per_km

       
        if distance_km > max_distance:
            distance_km = max_distance

        self.mileage += distance_km
        self.fuel_level -= distance_km * fuel_per_km

        if self.fuel_level < 0:
            self.fuel_level = 0.0

    
    def refuel(self, amount):
       
        self.fuel_level += amount
        if self.fuel_level > 100.0:
            self.fuel_level = 100.0

    
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.mileage} km, fuel: {self.fuel_level}%"


class Fleet:

    def __init__(self):
        self.cars = []

    
    def add_car(self, car):
        self.cars.append(car)

    
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)

    
    def total_mileage(self):
        total = 0
        for car in self.cars:
            total += car.mileage
        return total

    
    def list_cars(self):
        print("Cars in fleet:")
        for car in self.cars:
            print(car)




car_1 = Car("Toyota", "Corolla", 2015)
car_2 = Car("Ford", "Focus", 2018)
car_3 = Car("Tesla", "Model 3", 2022)

fleet = Fleet()
fleet.add_car(car_1)
fleet.add_car(car_2)
fleet.add_car(car_3)

car_1.drive(150)
car_2.drive(500)
car_3.drive(200)

car_2.refuel(20)
car_3.refuel(10)

fleet.list_cars()
print("Total mileage in fleet:", fleet.total_mileage(), "km")