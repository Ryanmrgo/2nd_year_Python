from abc import *
class Car(ABC):
    def __init__(self,regno=12345):
        self.regno=regno
    def openTank(self):
        print('Fill the fuel in the tank \n')
        print('Reg no for car',self.regno)
    @abstractmethod
    def steering(self):
        pass
    @abstractmethod
    def braking(self):
        pass
class Maruti(Car):
    def steering(self):
        print(' Maruti used manual steering\n')
        print('Drive the car')
    def braking(self):
        print(' Maruti used hydraylic brake\n')
        print('Apply break and stop it')
class Santro(Car):
    def steering(self):
        print(' Santro used power steering\n')
        print('Drive the car')
    def braking(self):
        print(' Santro used gas brake\n')
        print('Apply break and stop it')

m=Maruti(78934)
m.openTank()
m.steering()
m.braking()
s=Santro(89765)
s.openTank()
s.steering()
s.braking()
        
    
        
