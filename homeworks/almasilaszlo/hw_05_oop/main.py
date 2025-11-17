from car_fleet_mgr import Car,Fleet
def main():
    fleet=Fleet()

    #create cars
    car_1=Car("BMW","X1",2020,0,100)
    car_2=Car("VW","Passat",2024,1444,50)
    car_3=Car("Skoda","Octavia",2000,100000,20)
    

    #add to fleet
    fleet.add_cars(car_1)
    fleet.add_cars(car_2)
    fleet.add_cars(car_3)
    print("\n")

    #move cars
    car_1.drive(100)
    car_2.drive(500)
    car_3.drive(300)
    print("\n")

    #refuel
    car_1.refuel(20)
    car_2.refuel(10)
    car_3.refuel(600)
    print("\n")

    #remove cars
    fleet.remove_car(car_1)
    print("\n")

    fleet.Summary()

    #print(f"The total distance in the fleet is: {fleet.Summary():,d} km") 
    #fleet.car_list()

if __name__ == "__main__":
    main()