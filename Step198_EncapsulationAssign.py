#protected function, single underscore means "don't use o/s this class"
class Employee:
    def _init_(self):
        self._name = "Bob Smith"
        self._salary = "70,000"

    def pay(self):
        print("Bob got a raise!\nHis new salary is ${}.\n".format(self._salary))

#private function, can only be called within class
class MyCar:
    __maxspeed = 0
    __name = ""
    
    def __init__(self):
        self.__maxspeed = 15
        self.__name = "Chevy"

    def drive(self):
        print("This "+str(self.__name)+" goes "+str(self.__maxspeed)+" mph.")

    def setMaxSpeed(self,speed):
        self.__maxspeed = speed

if __name__ == "__main__":
    new = Employee()
    new._salary = "80,000"
    new.pay()

    car = MyCar()
    car.drive()
    print("I need a new car!!!\n")
    car.setMaxSpeed(320) #changes private variable using set method
    car.drive()
    print("MUCH better!")
