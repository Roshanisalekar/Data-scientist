class car():
    def start(self):
        print("car started")

    def stop(self):
        print("car stopped")

class toyotacar(car):

    def __init__(self,brand):
        self.brand=brand
        print(f"{self.brand}")
    
class fortuner(toyotacar):

    def __init__(self,color):
        self.color=color
        print(f"{color}")

c1=fortuner('red')
c1.start()
c1.stop()
c1.brand('bmw')