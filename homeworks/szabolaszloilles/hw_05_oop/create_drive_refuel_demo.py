from car_fleet_mgr import Car, Fleet

# Create cars
car1 = Car("Toyota", "Corolla", 2024)
car2 = Car("Ford", "Kuga", 2025)
car3 = Car("Hyundai", "Kona", 2019)

# Create fleet and add cars
fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

# First drives
car1.drive(150)
car2.drive(800)
car3.drive(500)

# Refuels
car1.refuel(30)
car2.refuel(50)
car3.refuel(10)

# Second drives
car1.drive(200)
car2.drive(300)
car3.drive(600)

# Invalid milage
car1.drive(-100)

# Invalid refuel
car1.refuel(-20)

# Show final state
fleet.show_fleet_status()