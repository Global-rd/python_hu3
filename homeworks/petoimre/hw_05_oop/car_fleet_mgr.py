

class Car:

    def __init__(self, brand, model, year):
        self.car_brand = brand
        self.car_model = model
        self.car_year = year
        self.car_milage = 0
        self.car_fuel_level = 100

    def drive(self,driving_milage):
        if driving_milage <= (self.car_fuel_level*10):
            self.car_milage += driving_milage
            self.car_fuel_level -= driving_milage*0.1
        else:
            print(f"you can max. {self.car_fuel_level*10} km driving.")    

    def get_car_condition(self):
        print(f"Typ: {self.car_brand} {self.car_model} year: {self.car_year}, Fuel level: {self.car_fuel_level}, Milage: {self.car_milage}")    


    def refuel_percent(self, fill_percent):
        if (self.car_fuel_level + fill_percent) <= 100:
            self.car_fuel_level += fill_percent
        else:
            print(f"You can only fill in {100-self.car_fuel_level} percent fuel.")




car_1 = Car("Opel", "Astra", 2010)
car_1.get_car_condition()
car_1.drive(100)
car_1.get_car_condition()
car_1.drive(500)
car_1.get_car_condition()
car_1.drive(500)
car_1.refuel_percent(20)
car_1.get_car_condition()
car_1.drive(500)
car_1.get_car_condition()
car_1.refuel_percent(80)
car_1.get_car_condition()
car_1.refuel_percent(50)

car_2 = Car("Kia", "Rio", 2012)
car_2.get_car_condition()
car_2.drive(300)
car_2.get_car_condition()
car_2.drive(400)
car_2.get_car_condition()
car_2.drive(500)
car_2.refuel_percent(40)
car_2.get_car_condition()
car_2.drive(500)
car_2.get_car_condition()
car_2.refuel_percent(60)
car_2.get_car_condition()
car_2.refuel_percent(80)

car_3 = Car("BMW", "320", 2014)
car_3.get_car_condition()
car_3.drive(300)
car_3.get_car_condition()
car_3.drive(400)
car_3.get_car_condition()
car_3.drive(500)
car_3.refuel_percent(40)
car_3.get_car_condition()
car_3.drive(500)
car_3.get_car_condition()
car_3.refuel_percent(60)
car_3.get_car_condition()
car_3.refuel_percent(80)

