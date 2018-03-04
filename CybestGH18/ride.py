class Ride:
  def __init__(self, id, startRow, startCol, finishRow, finishCol, earliestStart, latestFinish):
    self.id = id
    self.startRow = startRow
    self.startCol = startCol
    self.finishRow = finishRow
    self.finishCol = finishCol
    self.earliestStart = earliestStart
    self.latestFinish = latestFinish
    self.totalSteps = self.latestFinish - self.earliestStart
  
  def __str__(self):
    return ", ".join(map(str, [self.startRow, self.startCol, self.finishRow, self.finishCol, self.earliestStart, self.latestFinish, self.totalSteps]))
  
  def setVehicle(self, vehicle):
    self.vehicle = vehicle
  
  def distanceFromStart(self, vehicle=None):
    vehicle = vehicle or self.vehicle
    return abs(self.startRow - vehicle.row) + abs(self.startCol - vehicle.col)
  
