"""
Hozz létre egy car_fleet_mgr.py nevű fi le-t, és kódold le a következő feladat megoldását:
Készíts egy Car osztályt, amely rendelkezik a következő tulajdonságokkal:
● Márka (brand)
● Modell (model)
● Gyártási év (year)
● Kilométeróra állása (mileage), induló értéke 0.
● Üzemanyag-szint (fuel_level), induló értéke 100 (százalékban).
Az osztály tartalmazza a következő metódusokat:
● Egy konstruktor, amely beállítja a fenti attribútumokat.
● Egy drive() metódus, amely adott számú kilométerrel növeli a kilométeróra állását,
és csökkenti az üzemanyag-szintet (tételezzük fel, hogy 0.1% üzemanyag fogy megtett kilométerenként).
A drive() metódus csak annyit km-et engedjen vezetni, amennyire elegendő üzemanyag van.
● Egy refuel() metódus, amely feltölti az üzemanyag-szintet egy adott mennyiséggel. Figyelj a limitekre.
"""

class FuelLevelError(Exception):
    None

class RefillingError(Exception):
    None

class CarNotInFleet(Exception):
    None

class Car:
    """Constructs class Car to register different cars.
    atrributes:
        id: license plate
        brand: bran of car
        model: model of car
        year: year of construction of car
        mileage: sum of all kilometers
        fuel_level: level of fuel in %, =(100)"""
    
    fuel_consumption = float(0.1) # 0.1 % fuel consupmtion / kilometer

    def __init__(self, id, brand, model, year, mileage=0, fuel_level=100):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = float(fuel_level)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.id})"

    def drive(self, move_distance: int) -> None:
        """Registers move distance and fuel consumption.
            Distance mast be integer."""
        
        if not isinstance(move_distance, int):
            raise TypeError("A Vlue argument must be of type int.")
        
        if move_distance * self.fuel_consumption > self.fuel_level:
            raise FuelLevelError(f"{self} fuel level is not enough for this distance!")
        self.mileage += move_distance
        self.fuel_level -= move_distance * self.fuel_consumption
        print(f"Current distance of {self} is {self.mileage}, current fuel level is {self.fuel_level}")

    def refuel(self, amount_of_refilling):
        """ Refilling fuel with % of quantity.
        """
        if amount_of_refilling > (100 - self.fuel_level):
            raise RefillingError(f"{self} refilling quantity is too much.")
        self.fuel_level += amount_of_refilling
        print(f"{self} fuel level is {self.fuel_level} %.")


"""
Készíts egy Fleet osztályt, amely kezeli a Car objektumokat:
● Az osztály rendelkezzen egy listával, amelyben az autók találhatóak.
● Tartalmazzon metódusokat Car objektumok hozzáadására és eltávolítására a 
flottába/flottából.
● Tartalmazzon egy metódust, amely összesíti a flotta összes autójának 
összes kilométerét.
● Hozz létre néhány Car objektumot, add hozzá őket a flottához, hajts végre 
néhány műveletet (vezetés, tankolás), jelenítsd meg az autók állapotát és a 
flotta összesítő adatait.
"""

class Fleet:
    """Handle instance of members of cars must be (Car class).
    name: name of fleet
    """
    def __init__(self, name: str):
        self.name = name
        self.fleet_list = []

    def __str__(self):
        return f"{self.name}"

    def add_car_to_fleet(self, car_to_add: Car):
        """Add car to list of fleet.
        car_to_add: instance of Car object """
    
        self.fleet_list.append(car_to_add)
        print(f"{car_to_add} has been added to fleet.")

    def remove_car_from_fleet(self, car_to_remove: Car):
        """Remove car from list of fleet.
        car_to_remove: instance of Car object """

        for ccaarr in self.fleet_list:
            if ccaarr == car_to_remove:
                self.fleet_list.remove(ccaarr)
                print(f"{self}, {ccaarr} has been removed from fleet.")
                return
        print(f"{car_to_remove} was not found in {self} fleet.")

    def sum_of_all_mileage(self):
        """Remove car from list of fleet.
        car_to_remove: instance of Car object """

        total_miles = float(0.0)
        for ccaarr in self.fleet_list:
            total_miles += ccaarr.mileage
        print(f"All cars in {self} fleet have {total_miles} total_miles.") 

    def show_fleet_status(self):
        """Print teh status of all cars in the fleet"""

        print(f"\nStatus of all cars in the '{self.name}' fleet:")
        for car in self.fleet_list:
            print(f"{car.brand} {car.model} {car.id} - Year: {car.year}, Mileage: {car.mileage} km, Fuel level: {car.fuel_level: }%")
    
twingoq = Car("NXV-417", "Renault","Twingo", "2004")
huy = Car("MZE-434", "Hyundai", "I20", 2020)

try:
    for i in range(4):
        twingoq.drive(243)
        twingoq.refuel(10)
except:
    print("Valamit túltoltunk. :) ")

try:
    for i in range(3):
        twingoq.refuel(20)
except:
    print("Valamit túltoltunk. :) ")

try:
    for i in range(2):
        huy.drive(300)
        huy.refuel(4)
except:       
    print("Valamit túltoltunk. :) ")


fleet_of_SD = Fleet("fleetofrentinSD")
fleet_of_SD.add_car_to_fleet(twingoq)
fleet_of_SD.add_car_to_fleet(huy)
fleet_of_SD.sum_of_all_mileage()
fleet_of_SD.show_fleet_status()