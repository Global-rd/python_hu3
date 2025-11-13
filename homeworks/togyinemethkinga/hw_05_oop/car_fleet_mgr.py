class Car:

    def __init__(self, brand: str, model: str, year: int, mileage:float=0.00, fuel_level:float=100.00):
        # Megadjuk az adatokat.
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level
        # A km nem lehet negativ, ahogyan a % sem mehet 100 fölé.
        if self.mileage < 0.00:
            raise "Mileage can be at least 0."
        if self.fuel_level > 100.00:
            raise "The fuel level can't be more than 100."
        
    
    def drive(self):
        # A megtett km alapján kiszámoljuk az új km-állást
        try:
            self.taken_km = float(input("How many km have you done?"))
        except self.taken_km < 0:
            raise "Km can't be negative"
             
        if self.taken_km <= (self.fuel_level*10.00):
            self.fuel_level -= (self.taken_km*0.10)
            self.mileage += self.taken_km
            print(f"The {self.brand} {self.model}'s new mileage is {self.mileage} km and the new fuel level is {self.fuel_level} %.")
        else:
            print("It is impossible, not enough fuel.")


    def refuel(self): 
        # Tankolással feltöltjük az üzemanyag szintet.
        try:
            self.fuel = float(input("What percentage of fuel did you fill up?"))
        except self.fuel < 0:
            raise "Fuel can't be negative."
        
        if self.fuel <= 100-self.fuel_level:
            self.fuel_level += self.fuel
            print(f"Your new fuel level is {self.fuel_level} %.")
        else:
            print("It is too much fuel, please try again.")

    def __str__(self):
        # Normalizáljuk a kiirást.
        return f"{self.brand} {self.model} from {self.year}"
            
class Fleet:
   
    def __init__(self, name: str):
        self.name = name
        self.cars = [] 

    def add_car(self, car: Car):
        # Új autót adunk hozzá
        self.cars.append(car)

    def remove_car(self, brand, model):
        # Autó törlése
        for car in self.cars:
           if car.brand == brand and car.model == model:
                self.cars.remove(car)
                return
        print(f"{brand} {model} is not avaliable.")

    def car_listing(self):
        # Kilistázzuk az adott flottához tartozó autókat.
        print(f"The cars in {self.name} fleets are:")
        for car in self.cars:
            print(car)

    def sum_km(self):
        # Summázzuk az adott flottához tartozó autók km-állását.
        total_km = 0
        for car in self.cars:
            total_km += car.mileage
        print(f"The total kms in {self.name} fleet is {total_km} km.")



car1=Car("Honda","Jazz",2002)
car2=Car("Audi","S6",2016,70,80)
car3=Car("Ford","Focus",2010,180)

car1.drive()
car1.refuel()

fleet1=Fleet("X")
fleet2=Fleet("Y")

fleet1.add_car(car1)
fleet1.add_car(car2)
fleet1.add_car(car3)

fleet1.sum_km()

fleet1.remove_car("Honda","Jazz")

fleet1.car_listing()
fleet1.sum_km()
