from abc import abstractmethod
import copy

class Prototype:
    def __init__(self):
        pass

    @abstractmethod
    def clone(self):
        pass

class Car(Prototype):

    def __init__(self, name, brand, type):
        # some heavy db or network operation
        self.name = name
        self.brand = brand
        self.type = type

    def describe(self):
        print(self.name)
        print(self.brand)
        print(self.type)

    def copyCar(self, existingObj):
        print("cloning..")
        return copy.deepcopy(existingObj)

    def clone(self):
        return self.copyCar(self)
    
    def setName(self, name):
        self.name = name
    

def main():
    car1 = Car("Fortuner", "Toyota", "SUV")
    car1.describe()
    car2 = car1.clone()
    car2.setName("Hyrider")
    car2.describe()

if __name__ == "__main__":
    main()