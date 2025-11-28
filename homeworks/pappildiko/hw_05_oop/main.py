from car_fleet_mgr import Car, Fleet
import pprint

def main():
    # Create some cars
    car1 = Car("Toyota", "Corolla", 2018)
    car2 = Car("Ford", "Focus", 2020)
    car3 = Car("Tesla", "Model 3", 2023)
    car4 = Car("Hyundai", "i10", 2007)

    # Create a fleet and add/remove cars to/from it
    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)
    fleet.add_car(car4) # Car added to fleet: Hyundai i10
    fleet.remove_car(car4) # Car removed from fleet: Hyundai i10
    fleet.remove_car(car4) # This car is not in the fleet.

    # Perform some actions
    car1.drive(200)
    car2.drive(850)
    car3.drive(500)
    car1.drive(25)
    car2.drive(-35) # Ford Focus: Distance must be positive.
    car3.drive(1500000) # Tesla Model 3: Could only drive 500.0 km — ran out of fuel.
    # Tesla Model 3: Drove 500.0 km. Odometer: 1000.0 km, Fuel: 0.0%


    car2.refuel(30)
    car3.refuel(80)
    car2.refuel(0) # Ford Focus: Refuel amount must be positive.
    car3.refuel(20) # Tesla Model 3: Added +20.0%. Current fuel: 100.0%
    car1.refuel(600) # Toyota Corolla: Tank is now full (100%).
    

    # Show fleet summary
    fleet.show_fleet()





if __name__ == "__main__":
    main()