# You can add any additional function and class you want to implement in this file
from heap import Heap
class TreasureHeap:
    def __init__(self):
        '''
        Initializes the TreasureHeap with a max-heap based on treasure priority.
        The priority is based on the waiting time and treasure size, defined in the Treasure class.
        '''
        # The heap uses a comparison function based on the treasure's priority.
        self.treasures = Heap(self.compare_treasures)

    def compare_treasures(self, x, y):
        # Replace this with the correct logic you need.
        if (x.size + x.arrival_time) == (y.size + y.arrival_time):
            # If the same, prioritize the one with the higher id
            return x.id < y.id
        # Otherwise, compare based on size + arrival_time
        return (x.size + x.arrival_time) > (y.size + y.arrival_time)

    def insert(self, treasure, current_time):
        # When inserting, we assume priority calculations are based on the current time.
        self.treasures.insert(treasure)

    def extract_max(self):
        return self.treasures.extract()

    def __len__(self):
        return len(self.treasures)
def crewmate_comparator(crewmate1, crewmate2):
    return crewmate1.load < crewmate2.load

class CrewmateHeap:
    def __init__(self):
        self.crewmates = Heap(crewmate_comparator)

    def insert(self, crewmate):
        self.crewmates.insert(crewmate)

    def extract_min(self):
        return self.crewmates.extract()

    def update(self, crewmate):
        self.insert(crewmate)

    def __len__(self):
        return len(self.crewmates)

    def __iter__(self):
        return iter(self.crewmates.heap)