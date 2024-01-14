# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}  # id -> (stationName, time)
        self.timeStamp = {}  # `startStationName-endStationName` -> time difference

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        entryStation, entryTime = self.checkInMap[id]
        journey = entryStation + "-" + stationName
        timeDiff = t - entryTime

        if journey in self.timeStamp:
            self.timeStamp[journey].append(timeDiff)
        else:
            self.timeStamp[journey] = [timeDiff]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        journey = startStation + "-" + endStation
        timeDiffs = self.timeStamp[journey]
        timeSum = sum(timeDiffs)
        avg = timeSum / len(timeDiffs)

        return avg


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
