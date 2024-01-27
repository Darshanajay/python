from abc import ABC,abstractmethod
class car(ABC):
    def show(self):
        print("every car has four weels")
    @abstractmethod
    def speed(self):
        pass
class maruti(car):
    def speed(self):
        print("speed is 100km/h")
class suzuki(car):
    def speed(self):
        print("speed is 40km/h")
obj = maruti()
obj.show()
obj.speed()


obj1=suzuki()
obj1.show()
obj1.speed()
