

class Car:

    def __init__(self, license, brand, model, year):
        self.car_license = license
        self.car_brand = brand
        self.car_model = model
        self.car_year = year
        self.car_mileage = 0
        self.car_fuel_level = 100
        

    def __str__(self):
        return f"{self.car_license} {self.car_brand} {self.car_model}: Model year: {self.car_year}; Runned milage: {self.car_mileage}; Fuel level: {self.car_fuel_level} %"    


    def __repr__(self):
        return f"Car(license={self.car_license}, brand={self.car_brand}, model={self.car_model}, year={self.car_year})"


    def drive(self,driving_mileage):
        if driving_mileage <= 0:
            raise ValueError("You need to type bigger number then 0")
        if driving_mileage <= (self.car_fuel_level*10):
            self.car_mileage += driving_mileage
            self.car_fuel_level -= driving_mileage*0.1
        else:
            print(f"you can max. {self.car_fuel_level*10} km driving.")    


    def get_car_condition(self):
        print(f"{self.car_license}, {self.car_brand} {self.car_model}, year: {self.car_year}, Fuel level: {self.car_fuel_level} %, Mileage: {self.car_mileage} km")    

       
    def refuel_percent(self, fill_percent):
        if fill_percent <= 0:
            raise ValueError("You need to type bigger number then 0")
        if (self.car_fuel_level + fill_percent) <= 100:
            self.car_fuel_level += fill_percent
        else:
            print(f"You can max fill in {100-self.car_fuel_level} percent fuel.")


class Fleet:
    def __init__(self, location:str):
        self.loc = location
        self.cars = []


    def list_cars(self):
        print(f"The cars of the {self.loc} fleet:")
        for car in self.cars:
            print(f"{car.car_license}; {car.car_brand} {car.car_model}")


    def cars_condition_lis(self):
        print(f"Cars condition list of the {self.loc} fleet:")
        for car in self.cars:
            print(car)


    def add_car(self, car: Car):
        self.cars.append(car)


    def remove_car(self, license:str):
        for car in self.cars:
            if car.car_license == license:
                self.cars.remove(car)
                print(f"{license} removed from the fleet.")
                return
        print(f"No car {license} found in the fleet.") 


    def sum_all_milage(self):
        print(f"All cars of the fleet: {len(self.cars)} pcs. All mileage of the fleet's cars: {sum(car.car_mileage for car in self.cars)}")
        '''
        all_milage = 0
        for car in self.cars:
            all_milage += car.car_milage
        print(f"All cars of the fleet: {len(self.cars)} pcs. All mileage of the fleet's cars: {all_mileage}")
'''


car_1 = Car("ABC123","Opel", "Astra", 2010)
car_2 = Car("ABC456","Ford", "Focus", 2012)
car_3 = Car("XYZ123","Kia", "Rio", 2017)
car_4 = Car("XYZ456","Audi", "A6", 2011)
car_5 = Car("CDE789","BMW", "320", 2014)

Fleet_1 = Fleet("1.st. yard")

Fleet_1.add_car(car=car_1)
Fleet_1.add_car(car=car_2)
Fleet_1.add_car(car=car_3)
Fleet_1.add_car(car=car_4)
Fleet_1.add_car(car=car_5)

Fleet_1.list_cars()
Fleet_1.cars_condition_lis()

car_1.get_car_condition()
car_1.drive(100)
car_1.get_car_condition()
car_1.drive(500)
car_1.get_car_condition()
car_1.drive(500)
car_1.refuel_percent(10)
car_1.get_car_condition()
car_1.drive(147)
car_1.get_car_condition()
car_1.refuel_percent(80)
car_1.get_car_condition()
car_1.refuel_percent(50)


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


car_4.get_car_condition()
car_4.drive(300)
car_4.get_car_condition()
car_4.drive(400)
car_4.get_car_condition()
car_4.drive(500)
car_4.refuel_percent(40)
car_4.get_car_condition()
car_4.drive(500)
car_4.get_car_condition()
car_4.refuel_percent(60)
car_4.get_car_condition()
car_4.refuel_percent(80)


car_5.get_car_condition()
car_5.drive(450)
car_5.get_car_condition()
car_5.drive(290)
car_5.get_car_condition()
car_5.drive(315)
car_5.refuel_percent(30)
car_5.get_car_condition()
car_5.drive(455)
car_5.get_car_condition()
car_5.refuel_percent(35)
car_5.get_car_condition()
car_5.refuel_percent(75)

Fleet_1.sum_all_milage()

Fleet_1.remove_car("ABC123")

Fleet_1.list_cars()
Fleet_1.cars_condition_lis()

Fleet_1.sum_all_milage()


