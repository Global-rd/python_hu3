class Car:
    """
    Cars class
    """

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
        used_fuel: float = distance * 0.1
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

    def refuel(self, fuel_amount: float) -> None:
        if fuel_amount < 0:
            raise ValueError("Fuel amount must be positive!")

        if self.fuel_level == 100:
            print("The fuel tank is already full.")
            return

        if self.fuel_level + fuel_amount > 100:
            raise ValueError(
                f"Refueling {fuel_amount} % would exceed the tank capacity! Current fuel level: {self.fuel_level} %"
            )

        self.fuel_level = self.fuel_level + fuel_amount
        print(f"The car is refueled to {self.fuel_level} %")


suzuki = Car(brand="Suzuki", modell="Vitara", year=2017, mileage=0, fuel_level=100)

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
