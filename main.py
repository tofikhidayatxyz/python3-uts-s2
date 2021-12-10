class Kipas:
    brand = None
    rotasi = False
    _gear = 3
    _capacity = 103

    def __init__(self, brand, capacity):
        self.brand = brand
        self._capacity = capacity

    def setGear(self, gear):
        self._gear = gear

    def _getGear(self):
        return f"Gear : {self._gear}"

    def _getCapacity(self):
        return f"Kapasistas {self._capacity} Watt"

    def turnOnrotasi(self):
        self.rotasi = True

    def turnOffrotasi(self):
        self.rotasi = False

    def _getrotasi(self):
        return F"rotasi {'nyala ' if self.rotasi else 'Mati'}"

    def detail(self):
        print("------------------------")
        print(f"Brand : {self.brand}")
        print(self._getGear())
        print(self._getCapacity())
        print(self._getrotasi())
        print("------------------------")

    # Descructor
    def __del__(self):
        print('Class Destroyed byebye :)')



fan = Kipas("Miyako", 1200)

fan.detail();

del fan