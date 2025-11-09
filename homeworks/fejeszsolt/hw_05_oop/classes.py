from pprint import pprint
import logging

class InvalidDistanceError(Exception):
    """
    Egyéni kivétel távolságra
    """
    pass

class InvalidTankError(Exception):
    """
    Egyéni kitétel tankolásra
    """
    pass


class Car:

    def __init__(self,brand, modell, year, license_plate, mileage: float=0.0, fuel_level: float=100.0):
        self.brand = brand
        self.modell = modell
        self.year = year
        self._mileage = mileage
        self._fuel_level = fuel_level
        self.license_plate = license_plate
        logging.info(f"A kocsi {self} létrejött")

    def __str__(self):
        return f"Rendszám: {self.license_plate} | {self.brand} {self.modell} ({self.year})"

    def drive (self, distance: float):
        """távolság ellenőrzése, kilóméter számlálása, üzemanyagszint csökkentése"""
        if distance <= 0: 
            raise InvalidDistanceError("Ne tolass! Csak előre!")

        
        if (distance*0.1) > self._fuel_level:
            max_distance = self._fuel_level*10
            raise InvalidDistanceError(f"Ehez a távolsághoz kevés az üzenyag. Maximum {max_distance} kilómétert tudsz megtenni")
        
        self._mileage += distance
        self._fuel_level -= (distance*0.1)
        logging.info (f"A kocsi {self} megtett {distance} kilómétert, és {self._fuel_level} üzemanyag maradt")

    def refuel (self, tank):
        """tankolt mennyiség ellenőrzése, üzemyanyag szint növelése"""
        if tank <= 0:
            raise InvalidTankError("Ne leszívdd a tankot, hanem töltsdd meg!")
        
        if self._fuel_level+tank > 100.0:
            empty_tank=100.0-self._fuel_level
            raise InvalidTankError (f"Kifolyik az üzemanyag, ez tűzveszélyes! max {empty_tank} fér a tankba")
        
        self._fuel_level +=tank
        logging.info(f"A kocsi {self} {tank} üzemanyaggal feltöltve")
                     
    def fulltank (self):
        """tankolás fulltankig"""
        empty_tank=100.0-self._fuel_level
        self._fuel_level += empty_tank
        logging.info(f"A kocsi {self} tankja tele")

    def get_mileage(self) -> float: 
        """kilóméteróra leolvasás"""
        return self._mileage
    
    def get_fuel_level(self) -> float:
        """üzemanyagszint lekérdezés"""
        return self._fuel_level

class InvalidLicenceError(Exception):
    """
    Egyéni kitétel tankolásra
    """
    pass


class Fleet:
    
    def __init__(self, name:str):
        self.name = name
        self.cars = []

    def __str__(self):
        return f"Flotta: {self.name}"
    
    def add_car(self, car: Car):
        """gépkocsi felvétele a flottába"""
        self.cars.append(car)
        logging.info(f"A kocsi {car} felvéve a  {self} flottába")


    def list_cars(self):
        """flotta kocsiainak kilistázása"""
        pprint(f"A {self.name} flottában elérhető gépkocsik: ")
        for car in self.cars:
            print(car)
        logging.info(f"A kocsik kilistázva")

    def remove_car(self, target_license_plate:str):
        """kocsi eltávolítása a flottából"""
        for car in self.cars:
            if car.license_plate == target_license_plate:
                self.cars.remove(car)
                logging.info(f"A kocsi {car} eltávolítva a {self} flottából")
                return
        raise InvalidLicenceError(f"Nincs {target_license_plate} kocsi a flottában.")
        



    def mileage_sum (self):
        """össz kilóméter szommázása"""
        sum_mileage=0
        for car in self.cars:
            sum_mileage += car.get_mileage()
        return sum_mileage

 