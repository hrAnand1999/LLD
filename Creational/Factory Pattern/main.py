from vehicleFactory import Vehicle

def main():
    factory = Vehicle()

    vehicle = factory.getVehicle("CYCLE")

    if vehicle != None:
        vehicle.drive()
    else:
        print("Vehicle not found")

if __name__ == "__main__":
    main()