class Car:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100.0
    
    def drive(self, kilometers):

        fuel_needed = kilometers * 0.1
        
        if fuel_needed > self.fuel_level:
            max_km = self.fuel_level / 0.1
            self.mileage += max_km
            self.fuel_level = 0
            print(f" {max_km:.1f} km-t vezettél de elfogyott az üzemanyag!")
        else:
            self.mileage += kilometers
            self.fuel_level -= fuel_needed
            print(f"{kilometers} km-t vezettél.")
    
    def refuel(self, amount:float):
        if amount < 0:
            print(f"Negatív mennyiség nem tankolható!")
            return
        
        new_level = self.fuel_level + amount
        
        if new_level > 100:
            actually_refueled = 100 - self.fuel_level
            self.fuel_level = 100
            print(f"{actually_refueled:.1f}% (tank tele)")
        else:
            self.fuel_level = new_level
            print(f"Tank szint : {amount:.1f}%")
    
    def __str__(self):
        return (f"{self.brand} {self.model} ({self.year}) - "
                f"Kilométeróra: {self.mileage:.1f} km, "
                f"Üzemanyag: {self.fuel_level:.1f}%")
    


class Fleet:
    
    def __init__(self, name):
        self.name = name
        self.cars = []
    
    def add_car(self, car:Car):
        self.cars.append(car)
        print(f"Autó hozzáadva a flottához: {car.brand} {car.model}")
    
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Autó eltávolítva a flottából: {car.brand} {car.model}")
        else:
            print(f"Az autó nem található a flottában!")
    
    def total_mileage(self):
        return sum(car.mileage for car in self.cars)
    
    def show_fleet_status(self):
        print(f"\n{'='*100}")
        print(f"  {self.name} - Állapot")
        print(f"{'='*100}")
        
        if not self.cars:
            print("  A flotta üres.")
        else:
            for i, car in enumerate(self.cars, 1):
                print(f"{i}. {car}")
        
        print(f"{'-'*100}")
        print(f"  Flotta összes kilométer: {self.total_mileage():.1f} km")
        print(f"{'='*100}\n")


#Használat
if __name__ == "__main__":
    
    # Flotta létrehozása
    fleet = Fleet("Mezőfi Flotta")
    
    # Autók létrehozása
    print("Autók létrehozása\n")
    car_skoda = Car("Skoda", "Superb", 2019)
    car_vw = Car("VW", "Golf V R32", 2008)
    car_honda = Car("Honda", "Jazz", 2010)
    
    # Autók hozzáadása a flottához
    fleet.add_car(car_skoda)
    fleet.add_car(car_vw)
    fleet.add_car(car_honda)
    
    # Kezdeti állapot
    fleet.show_fleet_status()
    
    # Műveletek végrehajtása
    print("Műveletek végrehajtása\n")
    
    car_skoda.drive(150)
    
    car_vw.drive(300)
    
    car_honda.drive(1200)
    
    fleet.show_fleet_status()
    
    # Tankolás
    print("Tankolás\n")
    
    car_skoda.refuel(30)
    
    car_vw.refuel(100)
    
    car_honda.refuel(150)
    
    # Végső állapot
    fleet.show_fleet_status()
    
    # Autó eltávolítása
    print("Autó eltávolítása a flottából\n")
    fleet.remove_car(car_vw)
    
    # Állapot eltávolítás után
    fleet.show_fleet_status()