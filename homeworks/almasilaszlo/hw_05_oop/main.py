from car_fleet_mgr import Car,Fleet
def main():
    fleet=Fleet()

    #create cars
    car_1=Car("BMW","X1",2020,0,100)
    car_2=Car("VW","Passat",2024,1444,50)

    #add to fleet
    fleet.add_cars(car_1)
    fleet.add_cars(car_2)

    #move cars
    car_1.drive(100)
    car_2.drive(500)

    #refuel
    car_1.refuel(20)
    car_2.refuel(10)

    #remove cars
    #fleet.remove_car(car_1)
    print(fleet.mileage_SUM)

if __name__ == "__main__":
    main()