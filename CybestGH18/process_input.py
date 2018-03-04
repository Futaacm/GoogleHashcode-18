from ride import Ride
def process_input(filename):
  output = {}
  with open(filename) as file:
    metadata = list(map(lambda x: int(x), file.readline().split(" ")))
    output["rows"] = metadata[0]
    output["cols"] = metadata[1]
    output["vehicles"] = metadata[2]
    output["numRides"] = metadata[3]
    output["startBonus"] = metadata[4]
    output["steps"] = metadata[5]
    rides = []
    for index, line in enumerate(file):
      ride = {}
      lineProcessed = list(map(lambda x: int(x), line.split(" ")))
      ride["startRow"] = lineProcessed[0]
      ride["startCol"] = lineProcessed[1]
      ride["finishRow"] = lineProcessed[2]
      ride["finishCol"] = lineProcessed[3]
      ride["earliestStart"] = lineProcessed[4]
      ride["latestFinish"] = lineProcessed[5]
      rides.append(Ride(index, lineProcessed[0], lineProcessed[1], lineProcessed[2], lineProcessed[3], lineProcessed[4], lineProcessed[5]))
    output["rides"] = rides
  return output

if __name__ == "__main__":
  # test code
  import sys
  print(process_input(sys.argv[1]), sep="\n")
  


