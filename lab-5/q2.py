class Vehicle:
    def __init__(self, Owner=None, vehicleId=None, manufacturer=None):
        self.Owner = Owner
        self.vehicleId = vehicleId
        self.manufacturer = manufacturer

    def takeInput(self):
        self.Owner = input("Enter Owner name: ")
        self.vehicleId = input("Enter Vehicle Id: ")
        self.manufacturer = input("Enter Manufacturer name: ")


class passenger(Vehicle):
    def __init__(self, Pass=0):
        super().__init__()
        self.Pass = Pass

    def no_pass(self):
        self.Pass = int(input("Enter No of passengers in the car: "))

    def displayRc(cars):
        for rc in cars:
            print(
                f"Car Owner: {rc.Owner}\nVehicle Id: {rc.vehicleId}\nManufacturer: {rc.manufacturer}\nPassengers: {rc.Pass}\n")
            print("-------------")


def main():
    cars = []
    n = int(input("Enter the number of cars: "))

    for i in range(n):
        rc = passenger()
        rc.takeInput()
        rc.no_pass()
        cars.append(rc)
        print("\nentered")
    print("Car Information\n")
    passenger.displayRc(cars)


main()
