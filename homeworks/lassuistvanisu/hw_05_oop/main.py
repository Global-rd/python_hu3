from  car_fleet_mgr import Fleet, Car, InvalidNumberError

def main():
    # Példa használat:
    fleet = Fleet()

    car1 = Car("Toyota", "Corolla", 2021)
    car2 = Car("Ford", "Focus", 2021)
    car3 = Car("Kia", "Ceed", 2020)

    # Flottához adás
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    # Műveletek az autókon
    try:
        car1.drive(50)
        car1.drive(800)
        car1.refuel(25)
        car1.drive(100)
    except InvalidNumberError as err:
        print("ERROR: Invalid number")
    
    print("Fleet status:")
    fleet.show_fleet()

    print("Total km:")
    print(fleet.total_mileage())

    # Flottából eltávolítás
    fleet.remove_car(car2)
    print("Fleet status after removal:")
    
    fleet.show_fleet()
    print("Total km:")
    print(fleet.total_mileage())


if __name__ == "__main__":
    main()