import logging
from classes import Car, Fleet, InvalidDistanceError, InvalidTankError, InvalidLicenceError
from pprint import pprint
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


car1 = Car(brand="Trabant", modell="601", year="1970", license_plate="aaa-111")
car2 = Car(brand="Audi", year="2025", modell="A3", license_plate= "AUDI-001")
car3 = Car(brand="Renault", year="2023", modell="Megane", license_plate="TPU-569")
car4 = Car(brand= "Peugeot", modell="208", year="2020",license_plate="NGA-958")

fleet1 = Fleet("Python Kft.")

Fleet.add_car(fleet1, car=car1)
Fleet.add_car(fleet1, car=car2)
Fleet.add_car(fleet1, car=car3)
Fleet.add_car(fleet1, car=car4)

car1.drive(distance=189.3)
car2.drive(distance=111.1)
car3.drive(distance=50.9)
car1.drive(distance=65.5)
car4.drive(distance=250.2)
car2.drive(distance=72.3)

Car.fulltank(car1)
Car.refuel(car2, 18)

print(f"{car4} üzemanyagszint: {car4.get_fuel_level()}")

print(f"{car1} eddig megtett kilómétere: {car1.get_mileage()}")


Fleet.list_cars(fleet1)

print(f"Összkilóméter: {fleet1.mileage_sum()}")

Fleet.remove_car(fleet1, target_license_plate="NGA-958")

Fleet.list_cars(fleet1)