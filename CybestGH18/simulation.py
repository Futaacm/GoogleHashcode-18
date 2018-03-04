from vehicle import Vehicle
class Simulation():
  def __init__(self, data):
    self._data = data
    self.rows = data["rows"]
    self.cols = data["cols"]
    self.numVehicles = data["vehicles"]
    self.numRides = data["numRides"]
    self.startBonus = data["startBonus"]
    self.steps = data["steps"]
    self.rides = data["rides"]
    self.vehicles = [Vehicle(i) for i in range(self.numVehicles)]
    self.activeRides = []
    self.activeVehicles = []
    self.inactiveRides = self.rides[:]
    self.sortedRides = []
    self.step = 0
    self.output = []
    self.takeStep()

  def takeStep(self):
    while self.step < self.steps:
      idleVehicles = [vehicle for vehicle in self.vehicles if not vehicle.inRide]
      if len(idleVehicles) == 0:
        for vehicle in self.vehicles:
          vehicle.step(self.step)
          if vehicle.stepsTaken == vehicle.stepsToTake:
            vehicle.setIdle()
            vehicleRide = self.peekClosestRide(vehicle)
            if vehicleRide is not None:
              if vehicleRide.startRow == vehicle.row and vehicleRide.startCol == vehicle.col:
                self.activeRides.append(vehicleRide)
                self.inactiveRides.remove(vehicleRide)
                vehicle.setRide(vehicleRide)
      idleVehicles = [vehicle for vehicle in self.vehicles if not vehicle.inRide]
      for index, vehicle in enumerate(idleVehicles):
        vehicleRide = self.getClosestRide(vehicle)
        if vehicleRide == None:
          continue
        #print(vehicleRide)
        vehicle.setRide(vehicleRide)
        #self.output.append(vehicle)
        #self.output.sort(key=lambda vehicle: vehicle.ride.totalSteps)
        #vehicle.step()
      #print(map(lambda x: x.ride, self.ac))
      if len(self.activeRides) == self.numRides:
        break
      self.step += 1
    self.printOutput()
  
  def printOutput(self):
    for vehicle in self.vehicles:
      output = ""
      output += str(len(vehicle.rides)) + " "
      output += " ".join(map(lambda ride: str(ride.id), vehicle.rides))
      output = output.strip()
      print(output)
  def peekClosestRide(self, vehicle):
    if len(self.inactiveRides) == 0:
      return None
    sortedRides = self.inactiveRides[:]
    sortedRides.sort(key=lambda ride: ride.totalSteps)
    sortedRides.sort(key=lambda ride: ride.distanceFromStart(vehicle))
    #sortedRides.sort(lambda ride: ride["distToVehicle"])
    #self.activeRides.append(sortedRides[0])
    #self.inactiveRides.remove(sortedRides[0])
    #print("A", list(map(str, self.activeRides)))
    #print("B", list(map(str, self.inactiveRides)))
    return sortedRides[0]
  def getClosestRide(self, vehicle):
    if len(self.inactiveRides) == 0:
      return None
    sortedRides = self.inactiveRides[:]
    sortedRides.sort(key=lambda ride: ride.totalSteps)
    sortedRides.sort(key=lambda ride: ride.distanceFromStart(vehicle))
    #sortedRides.sort(lambda ride: ride["distToVehicle"])
    self.activeRides.append(sortedRides[0])
    self.inactiveRides.remove(sortedRides[0])
    #print("A", list(map(str, self.activeRides)))
    #print("B", list(map(str, self.inactiveRides)))
    return sortedRides[0]

if __name__ == "__main__":
  import sys
  import process_input as ps
  simulation = Simulation(ps.process_input(sys.argv[1]))