class Vehicle:
  def __init__(self, id, row=0, col=0):
    self.id = id
    self.row = row
    self.col = col
    self.ride = None
    self.inRide = False
    self.stepsTaken = 0
    self.stepsToTake = 0
    self.stepsBeforeStart = 0
    self.stepsBeforeFinish = 0
    self.rides = []
  def step(self, simStep):
    if simStep < self.ride.earliestStart and self.stepsTaken == self.stepsBeforeStart:
      # wait
      return
    self.stepsTaken += 1
  def setRide(self, ride):
    self.ride = ride
    self.rides.append(ride)
    self.stepsBeforeStart = ride.distanceFromStart(self)
    self.stepsToTake = self.stepsBeforeStart + ride.totalSteps
    self.inRide = True

  def setIdle(self):
    self.row = self.ride.finishRow
    self.col = self.ride.finishCol
    self.ride = None
    self.stepsTaken = 0
    self.stepsBeforeStart = 0
    self.stepsToTake = 0
    self.inRide = False
    

    