

class Car:

    consumption=0.1 

    def __init__(self, brand, model, year): 
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100 #fuel_level százalékban értendő

    def drive(self,miles):  #km óra állás növelése, üzemanyag csökkentése, megtett km nem viheti minuszba a fogyasztást
        if miles<0:
            raise ValueError("Nem lehet negatív szám!")

        consumption=0.1 #százalékban értendő
        fuel=(miles*consumption) #a megteendő úthoz szükséges üzemanyag, %-ban értendő
        
        if fuel<= self.fuel_level:
            self.mileage +=miles
            self.fuel_level -=fuel
        else:
            p1=self.fuel_level/consumption           
            print(f"Csak {p1} utat tehetsz meg a rendelkezésre álló üzemanyaggal")
    
            
    def refuel(self, plus_fuel): #feltölti az üzemanyag szintet, figyelni a max 100%-ra fluel_level+tankolás nem lehet több mint 100%
        if plus_fuel<0:
            raise ValueError("Nem lehet negatív szám!")
        
        used_fuel=100-self.fuel_level #százalékban értendő
        if used_fuel<plus_fuel:
            print(f"Csak {used_fuel} százalékot tankolhatsz")
            self.fuel_level=100 #százalékban értendő, ha ez volt a feladat,hogy ilyenkor is tele tankolhasson
        else:
            self.fuel_level+=plus_fuel

car1=Car("Seat", "Ibiza", 2014)
car2=Car("Seat", "Ibiza", 2015)
car3=Car("Seat", "Ibiza", 2016)
car4=Car("Seat", "Ibiza", 2017)
car5=Car("Seat", "Ibiza", 2018)
car1.drive(10)
car1.refuel(20000)
car2.drive(-50)
car2.refuel(51)
car3.drive(2000)
car3.refuel(81)
car4.drive(500)
car4.refuel(300)

class Fleet:
    car_count=0

    @classmethod
    def get_car_count(cls):
        return cls.car_count
    
    def __init__(self):
        self.car_list=[]

    def add_car(self,car):
        self.car_list.append(car)
        Fleet.car_count +=1

  
    def del_car(self,car):
        if car in self.car_list:
            self.car_list.remove(car)
            Fleet.car_count -=1
        else:
            print("Nincs ilyen adat, ezért nem törölhető!")  

   
    def count_miles(self):
        sum_car_mileage=0
        for car in self.car_list:
            sum_car_mileage+=car.mileage
        return sum_car_mileage
        

    
#feladat utolsó bekezdése: a listában lévő autók kilistázása, Tipus, gyártmány, évjárat, kilóméteróra állás, benzin szint, db szám  
    def print_carinfo(self):
        for car in self.car_list:
            print(f"brand:{car.brand} model:{car.model} year:{car.year} mileage:{car.mileage} fuel level:{car.fuel_level}")
        print(f"car count:{Fleet.get_car_count()}")       

    
            

fleet=Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)
fleet.add_car(car4)
fleet.add_car(car5)
fleet.del_car(car3)


fleet.print_carinfo()
print(f"Fleet's count miles {fleet.count_miles()}")







