# https://leetcode.com/problems/design-parking-system/

# NOT OPTIMIZED SOLUTION
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:

        if carType == 1:
            if self.big:
                self.big -= 1
                return True
            return False
        if carType == 2:
            if self.medium:
                self.medium -= 1
                return True
            return False

        if carType == 3:
            if self.small:
                self.small -= 1
                return True
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# OPTIMIZED SOLUTION

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parkMap = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.parkMap[carType]:
            self.parkMap[carType] -= 1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
