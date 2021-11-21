class Car :
    brand = None
    lamp = False
    _gear = 1
    _capacity = 1500
    _speed = 0

    def __init__(self, brand, capacity) :
        self.brand = brand
        self._capacity = capacity

    def setSpeed(self, speed):
        self._speed = speed

    def _getSPeed(self):
        return  f"Speed: {self._speed} KM/H"

    def setGear(self, gear):
        self._gear = gear

    def _getGear(self):
        return f"Gear : {self._gear}"

    def _getCapacity(self):
        return f"Kapasistas {self._capacity}"

    def turnOnLamp(self):
        self.lamp = True

    def turnOffLamp(self):
        self.lamp = False

    def _getLamp(self):
        return F"Lampu {'Nyala' if self.lamp else 'Mati'}"

    def detail(self):
        print("------------------------")
        print(f"Brand : {self.brand}")
        print(self._getGear())
        print(self._getSPeed())
        print(self._getCapacity())
        print(self._getLamp())
        print("------------------------")


# Subclass
class Lamborgini(Car):
    def __init__(self, type):
        if(type == 'Aventador') :
            capacity = 3000
        elif (type == 'Huracan'):
            capacity = 5000
        else :
            capacity = 2000

        super(Lamborgini, self).__init__(F"Lamborgini {type}", capacity)

    def setSpeed(self, speed):
        self._speed = speed * self._gear
    def setGear(self, gear):
        self._gear = "Mundur" if gear < 0 else gear



## Super class
car = Car("Avanza", 1400)
car.setGear(4)
car.setSpeed(100)
car.turnOnLamp()
car.detail()
car.turnOffLamp()
car.detail()

## Subclass

lambo = Lamborgini('Aventador')
lambo.setGear(3)
lambo.setSpeed(300)
lambo.turnOnLamp()
lambo.detail()
lambo.setGear(-1)
lambo.turnOffLamp()
lambo.detail()





