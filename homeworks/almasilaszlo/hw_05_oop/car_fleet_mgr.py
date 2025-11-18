
class Car:

    def __init__(self, brand: str,model: str, year: int, mileage: int=0, fuel_level:float=0.0):
        self.brand=brand
        self.model=model
        self.year=year
        self.mileage=mileage
        self.fuel_level=fuel_level
    
    #drive
    def drive(self,distance):
        if distance<=0:
            print(f"ERROR! The distance could be only a positive integer!")
            return
        
        remaining_distance= self.fuel_level/0.1
        if distance>remaining_distance:
            print(f"Not enoug fuel level for {distance} km, you can drive only {remaining_distance} km!")
            return

        else:
            self.mileage+=distance
            self.fuel_level-= distance*0.1
            print(f"The car has been driven sucessfully {distance} km. The new fuel level is {self.fuel_level}%")
    
    #refuel
    def refuel(self,fuel):
        max_refuel= 100-self.fuel_level
        if fuel<=0:
            print(f"ERROR! The fuel could be only a positive integer!")
            return
        if fuel>max_refuel:
            print(f"Can't fuel {fuel}l to this car, maximum {max_refuel}l!")
            return
        else:
            self.fuel_level+=fuel
            print(f"Car has been sucesfully refueled with {fuel}l!")
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.mileage:,d} km, fuel: {self.fuel_level:.1f}%"
      


class Fleet:

    def __init__(self):
        self.cars=[]
    
    #adding car
    def add_cars(self, car):
        self.cars.append(car)
        print(f"Car {car} has been added to Fleet")
   
   #removing car
    def remove_car(self,car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Car {car} has been removed to Fleet")
        return
    
    # fleet summary
    def Summary(self):
        print(f"---Fleet data---")
        for car in self.cars:
            print(car)
        print(f"The total mileage of the fleet: {sum(car.mileage for car in self.cars):,d} km")

