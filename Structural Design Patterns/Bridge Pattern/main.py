from abc import ABC, abstractmethod

class Engine(ABC):

    def __init__(self):
        pass
    
    @abstractmethod
    def start(self):
        pass

class PetrolEngine(Engine):

    def __init__(self):
        super().__init__()

    def start(self):
        return "Petrol engine started"
    

class ElectricEngine(Engine):

    def __init__(self):
        super().__init__()

    def start(self):
        return "Electric engine started"
    
class Car(ABC):

    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def drive(self):
        pass

class Sedan(Car):

    def __init__(self, engine: Engine):
        super().__init__(engine)

    def drive(self):
        return f"Driving a sedan. {self.engine.start()}"
    
class SUV(Car):
    def __init__(self, engine: Engine):
        super().__init__(engine)

    def drive(self):
        return self.engine.start() + " Driving an SUV."
    

def main():
    petrol_engine = PetrolEngine()
    electric_engine = ElectricEngine()

    sedan_with_petrol = Sedan(petrol_engine)
    suv_with_electric = SUV(electric_engine)
    sedan_with_electric = Sedan(electric_engine)
    suv_with_petrol = SUV(petrol_engine)
    print(suv_with_petrol.drive())
    print(sedan_with_electric.drive())

    print(sedan_with_petrol.drive())
    print(suv_with_electric.drive())
if __name__ == "__main__":
    main()