class Car:
    """
    Car class
    """

    FUEL_CONSUMPTION_RATE: float = 0.1  # fuel consumption rate in % per km

    def __init__(
        self,
        brand: str,
        modell: str,
        year: int,
        mileage: float = 0,
        fuel_level: float = 100,
    ) -> None:
        self.brand: str = brand
        self.modell: str = modell
        self.year: int = year
        self.mileage: float = mileage
        self.fuel_level: float = fuel_level

    def drive(self, distance: float) -> None:
        """Drive the car a certain distance if enough fuel is available."""

        used_fuel: float = distance * Car.FUEL_CONSUMPTION_RATE

        if self.fuel_level - used_fuel >= 0:
            self.fuel_level -= used_fuel
            self.mileage += distance
            print(f"Driven {distance} km")
            print(f"Remaining fuel: {self.fuel_level} %")
            print(f"Total mileage: {self.mileage} km")
        else:
            raise ValueError(
                f"Actual fuel level {self.fuel_level} is not enough to drive {distance} km!"
            )

    def _validate_fuel_amount(self, fuel_amount: float) -> None:
        """Validate that the fuel amount is positive."""
        if fuel_amount < 0:
            raise ValueError("Fuel amount must be positive!")

    def _is_tank_full(self) -> bool:
        """Check if the fuel tank is full."""
        return self.fuel_level == 100

    def _check_tank_capacity(self, fuel_amount: float) -> None:
        """Check if refueling would exceed tank capacity."""
        if self.fuel_level + fuel_amount > 100:
            raise ValueError(
                f"Refueling {fuel_amount} % would exceed the tank capacity!\n"
                f"Current fuel level: {self.fuel_level} %"
            )

    def _add_fuel(self, fuel_amount: float) -> None:
        """Add fuel to the tank."""
        self.fuel_level += fuel_amount
        print(f"The car is refueled to {self.fuel_level} %")

    def refuel(self, fuel_amount: float) -> None:
        """Refuel the car with the given amount of fuel."""
        self._validate_fuel_amount(fuel_amount=fuel_amount)

        if self._is_tank_full():
            print("The fuel tank is already full.")
            return

        self._check_tank_capacity(fuel_amount=fuel_amount)
        self._add_fuel(fuel_amount=fuel_amount)


class Fleet:
    """
    Fleet class
    """

    def __init__(self) -> None:
        self.cars: list[Car] = []

    def add_car(self, car: Car) -> None:
        """Add a car to the fleet."""
        self.cars.append(car)

    def remove_car(self, car: Car) -> None:
        """Remove a car from the fleet."""
        self.cars.remove(car)

    def get_total_mileage(self) -> float:
        """Get the total mileage of all cars in the fleet."""
        return sum(car.mileage for car in self.cars)


suzuki = Car(brand="Suzuki", modell="Vitara", year=2017, mileage=0, fuel_level=100)
toyota = Car(brand="Toyota", modell="Corolla", year=2015, mileage=50000, fuel_level=50)
mercedes = Car(
    brand="Mercedes", modell="C-Class", year=2018, mileage=30000, fuel_level=80
)
lada = Car(brand="Lada", modell="Niva", year=2010, mileage=150000, fuel_level=30)
peugeot = Car(brand="Peugeot", modell="208", year=2020, mileage=10000, fuel_level=90)

fleet_mgr = Fleet()
fleet_mgr.add_car(car=suzuki)
fleet_mgr.add_car(car=toyota)
fleet_mgr.add_car(car=mercedes)
fleet_mgr.add_car(car=lada)
fleet_mgr.add_car(car=peugeot)

total_mileage: float = fleet_mgr.get_total_mileage()
print(f"Total mileage of the fleet: {total_mileage} km")
print("----------------")

try:
    suzuki.drive(distance=200)
except ValueError as e:
    print(e)
print("----------------")

try:
    suzuki.drive(distance=200)
except ValueError as e:
    print(e)
print("----------------")

try:
    suzuki.refuel(fuel_amount=50)
except ValueError as e:
    print(e)
print("----------------")

try:
    suzuki.drive(distance=150)
except ValueError as e:
    print(e)
print("----------------")

total_mileage: float = fleet_mgr.get_total_mileage()
print(f"Total mileage of the fleet: {total_mileage} km")
