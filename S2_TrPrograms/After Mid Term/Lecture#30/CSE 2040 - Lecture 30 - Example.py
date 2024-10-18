# CSE 2040 - Lecture 31 - Example 

# Illustrating use of three types of instance methods

class Vehicle:
    __numbVehicles = 0

    @classmethod
    def countVehicles(cls):
        cls.__numbVehicles = cls.__numbVehicles + 1

    @classmethod
    def getNumbVehicles(cls):
        return cls.__numbVehicles
    
    @staticmethod
    def checkMonth(mNumber):
        try:
            assert (mNumber >= 1 and mNumber <= 12)
            return True
        except AssertionError:
            print("Month number should be between 1 and 12")
            return False

    def __init__(self, vNo, vMonth, vYear):       
        if (Vehicle.checkMonth(vMonth) == True):
            self.__vehicleNumber = vNo
            self.__monthManufacture = vMonth
            self.__yearManufacture = vYear
            Vehicle.countVehicles()

    def setMonth(self,vMonth):
        if (Vehicle.checkMonth(vMonth) == True):
            self.__monthManufacture = vMonth

    def __str__(self):
        return ("Vehicle Number " + str(self.__vehicleNumber) + " is manufactured on " + str(self.__monthManufacture) + "-" + str(self.__yearManufacture))

# Main
if __name__ == "__main__":
    print()
    v1 = Vehicle(143,1,2018)
    v2 = Vehicle(146,12,2016)
    v3 = Vehicle(142,8,2018)
    v4 = Vehicle(151,9,2017)
    #v5 = Vehicle(156,14,2018)
    print(v1)
    print(v2)
    print(v3)
    print(v4)
    #print(v5)
    print()
    print("Number of vehiecles is " + str(Vehicle.getNumbVehicles()))
    print()
