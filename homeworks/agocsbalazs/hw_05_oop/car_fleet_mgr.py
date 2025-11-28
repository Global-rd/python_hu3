class Car:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        self.mileage: float = 0.0   #km
        self.fuel_level: float = 100.0  # %
        #kell bele egy plusz attribútum, hogy a jármű benne van-e a flottában mert megtankolom, vezetem ha nincs ott is és hibára fut
        self.in_fleet: bool = False


    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"


    def drive(self, distance: float) -> None:
        #flotta lista ellenőrzés kapásból
        if not self.in_fleet:
            raise ValueError("This car is not in the fleet. Cannot drive or refuel.")
        
        if distance <= 0:
            raise ValueError("Distance must be positive.")
            
        fuel_needed: float = distance * 0.1  # assuming 0.1% fuel consumption per km  
        if fuel_needed > self.fuel_level:
            raise ValueError("Not enough fuel to drive the requested distance.")
        self.mileage += distance
        self.fuel_level -= fuel_needed
        print(f"{self.brand} {self.model} Drove {distance} km. Odometer: {self.mileage} km, Fuel level: {self.fuel_level}%.")



    #tankolás
    def refuel(self, amount: float) -> None:
        if not self.in_fleet:
            raise ValueError("This car is not in the fleet. Cannot drive or refuel.")
        if amount < 0:
            raise ValueError("Refuel amount must be positive.")
        if self.fuel_level + amount > 100:
            raise ValueError("Refuel amount exceeds tank capacity.")
        self.fuel_level += amount
        print(f"Refueled the {self.brand} {self.model} with {amount}%. Current fuel level: {self.fuel_level}%.")

#flotta osztály létrehozása
#kell egy lista a járművek tárolására
#hozzáadás és eltávolítás metódusok
#listázás metódus
class Fleet:    
    def __init__(self) -> None:
        self.cars = []    

    def add_car(self, car: Car) -> None:
        self.cars.append(car)
        #jelöljük hogy a jármű benne van a flottában
        car.in_fleet = True
        print(f"{car.brand} - {car.model} Car added to the fleet.")

    
    def remove_car(self, car: Car) -> None:
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} - {car.model} Car removed from fleet.")
            #jelöljük hogy a jármű nincs benne a flottában
            car.in_fleet = False
        else:
            print(f"{car.brand} - {car.model} Car not found in fleet.")
    
    def list_cars(self) -> None:
        if not self.cars:
            print("No cars in the fleet.")
        for car in self.cars:
            print(f"{car.brand} {car.model} ({car.year}) - Mileage: {car.mileage} km, Fuel level: {car.fuel_level}%")


    def sum_mileage_report(self) -> None:
        total_mileage: float = sum(car.mileage for car in self.cars)
        print(f"Total mileage of all cars in the fleet: {total_mileage} km.")
            
           
#adjunk meg néhány verdát és teszteljük a funkciókat   
car_1=Car("Toyota", "Highlander", 2022 )
car_2=Car("Ford", "Mustang", 1960 )
car_3=Car("Mitsubishui", "EVO", 1999 )
car_4=Car("Ford", "Escort MK II.", 1980 )
car_5=Car("Peugeot", "205", 1985 )

#flottához adás
fleet = Fleet()
fleet.add_car(car_1)
fleet.add_car(car_2)
fleet.add_car(car_3)
fleet.add_car(car_4)
fleet.add_car(car_5)

#flottából eltávolítás
fleet.remove_car(car_5)



#flotta listázás
fleet.list_cars()

#flotta összesített futásteljesítmény jelentés
fleet.sum_mileage_report()

#vezetés és tankolás
car_1.drive(380)
car_2.drive(240)
car_3.drive(310)
car_4.drive(530)

fleet.sum_mileage_report()
#hiba tesztelés
#car_5.drive(299)

car_1.refuel(20)
car_4.refuel(20)

#hiba tesztelés
#car_5.refuel(50)


#flotta listázás újra
fleet.list_cars()
fleet.sum_mileage_report()

     