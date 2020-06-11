from abc import ABC, abstractmethod

class Table(ABC):
    def build(self, number):
        print("Number of legs requested:",number)
    @abstractmethod
    def order(self,number):
        pass

class CustOrder(Table):
    def order(self, number):
        print("We cannot build a table with only {} legs!".format(number))

if __name__ == "__main__":
    obj = CustOrder()
    obj.build("2")
    obj.order("2")
