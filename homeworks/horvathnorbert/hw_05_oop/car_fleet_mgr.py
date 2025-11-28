import os
import homework_classes as hc

os.system('cls' if os.name == 'nt' else 'clear')
    
car_1 = hc.Car("Opel", "Astra", 2010, 325000, 80)
car_2 = hc.Car("Kia", "Ceed", 2019, 175000, 60)
car_3 = hc.Car("Trabant", "601GTI", 1980, 555000, 20)

fleet = hc.Fleet("Homework fleet")

fleet.add_car(car_1)
fleet.add_car(car_2)
fleet.add_car(car_3)
fleet.remove_car(car_2)

car_1.refuel(10)
car_1.drive(500)
car_3.refuel(80)
car_3.drive(900)

print(f"\n")
print(f"Make: Model: Year: Odometer: Fuel level:")
print(f"--------------------------------------------------------------------")
fleet.list_cars()
print(f"--------------------------------------------------------------------")
print(f"The total number of kilometers driven by the fleets vehicles: {fleet.total_km()} km.")
print(f"\n")



