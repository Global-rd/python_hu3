class Car:
    def __init__(self, brand, model, constr_year):
        
        self.brand = brand               
        self.model = model              
        self.constr_year = constr_year                 
        self.mileage = 0                 
        self.fuel_level = 100  

    def drive(self, run):
        fuel_cons = run * 0.1

        if fuel_cons > self.fuel_level:
            max_distance = self.fuel_level / 0.1
            print(f"You only have enough fuel for {max_distance:.1f} km.")
            return

        self.fuel_level -= fuel_cons
        self.mileage += run
        print(f"You have driven {run} km.")
    
    def refuel(self, fuel):
        try:
        
            if self.fuel_level == 100:
                print("Tank is full.")
                return

        
            if self.fuel_level + fuel > 100:
                raise ValueError("Too much fuel!")

        
            self.fuel_level += fuel
            print(f"Refueled {fuel} liters. Current fuel level: {self.fuel_level} %.")    

        except ValueError:
        
            max_amount = 100 - self.fuel_level
            print(f"Error: You cannot refuel {fuel} liters.")
            print(f"Maximum allowed: {max_amount} liters.")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.constr_year}) - {self.mileage} km, fuel: {self.fuel_level:.1f}%"

class Fleet:     
    def __init__(self):
        self.car_list=[]
    def add_car(self,car_list):
        self.car_list.append(car_list)
    def remove_car(self, car_list):
    
        try:
            self.car_list.remove(car_list) 
            print(f"{Car} removed from fleet!")
        except ValueError:
            print("This car is not member of the fleet.")
     
        

    def sum_mileage(self):
        sum_mileage=0
        for car in self.car_list:
            sum_mileage += car.mileage
        return sum_mileage 
    
    def show_fleet(self):
        print("\n--- Fleet conditions ---")
        for car in self.car_list:
            print(car)
        print(f"Total mileage: {self.sum_mileage():.1f} km\n")
    
if __name__ == "__main__":
    
        car1 = Car("Lada", "2104", 1980)
        car2 = Car("Lada", "2105", 1981)
        car3 = Car("LAda", "2107", 1982)

    
        fleet = Fleet()
        fleet.add_car(car1)
        fleet.add_car(car2)
        fleet.add_car(car3)

   
        car1.drive(200)      
        car2.drive(800)      
        car3.drive(300)      
        car2.refuel(30)      
        car2.drive(100)      

    

        fleet.show_fleet()

    