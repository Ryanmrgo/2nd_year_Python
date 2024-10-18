from abs import Car

class Santro(Car):
    def steering(self):
        print('Santro uses power steering')
        print('Drive the car')

    def braking(self):
        print('Santro uses gas brakes')
        print('Apply brakes and stop it')

m=Santro(7878)
m.openTank()
m.steering()
m.braking()

