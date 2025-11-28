class Car:
    # Konstruktor __ kocsigyár:)
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0.0
        self.fuel_level = 100.0

    # drive method
    def drive(self, distance : float):
        if distance < 0:
            print(f"Error: {self.brand} {self.model}: You cannot drive negative kilometers!")
            return
        
        #fogyasztás: 0.1%/km Max távolság=fuel*10
        max_distance = self.fuel_level * 10 
	    
        #Mennyit tud vezetni, ha kevesebb az üzemanyag:
        actual_distance = min(distance, max_distance)
	
        if actual_distance == 0:
            print(f"{self.brand} {self.model}: Not enough fuel to drive.")
            return
	
        # Az attribútumok frissítése:
        self.mileage += actual_distance
        self.fuel_level -= actual_distance * 0.1
    
        # Biztosítjuk, hogy a szint ne menjen 0 alá:
        self.fuel_level = max(self.fuel_level, 0.0)
        print(f"{self.brand} {self.model} drove {distance} km. Mileage: {self.mileage} km, Fuel level: {self.fuel_level:.1f}%")

    #refuel method
    def refuel(self, refill : float):
        if refill < 0:
            print(f"Error: {self.brand} {self.model}: You cannot refuel negative amounts!")
        
        # Kiszámoljuk, mennyi hely van még a tankban (100% a limit)
        space_left = 100.0 - self.fuel_level
        actual_refill = min(refill, space_left)
	
        if actual_refill == 0:
            print(f"{self.brand} {self.model}: The tank is already full (100.0%).")
            return
        self.fuel_level += actual_refill

        if self.fuel_level == 100.0 and refill > actual_refill:
             print(f"{self.brand} {self.model} refueled to the top, {actual_refill:.1f}% was added.")
        else:
             print(f"The fuel tank of the {self.brand} {self.model} has been successfully refilled by {actual_refill:.1f}%. Current level: {self.fuel_level:.1f}%.")

    #Állapot lekérdezése car info method
    def car_info(self):
        return (f"{self.brand} {self.model} ({self.year}) | Km állás: {self.mileage:.1f} km | Üzemanyagszint: {self.fuel_level:.1f}%")


class Fleet:
    def __init__(self):
        # Egy üres lista, amiben az autók lesznek tárolva
        self.cars = []

    # autó hozzáadása
    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} added to the fleet.")

    # autó eltávolítása
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} removed from the fleet.")
        else:
            print("Car not found in fleet.")
    
    # össz km
    def total_mileage(self):
        return sum(car.mileage for car in self.cars)
    
    #flotta infók
    def fleet_info(self):
    
        if self.cars == []:
            print("There are no cars in the fleet!\n")
        else:
            print("\n--------------------------- Fleet Info ---------------------------------\n")
    
            for car in self.cars:
                print(f" {car.car_info()}\n")
                print("------------------------------------------------------------------------\n")
                

# -------- TEST --------


car1 = Car("Volvo", "V60", 2022)
car2 = Car("Ford", "Kuga", 2018)
car3 = Car("Ford", "Focus", 2015)

fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

car1.drive(150)
car2.drive(50)

car3.refuel(20)
car1.refuel(60)

print(car2.car_info())
  
fleet.fleet_info()