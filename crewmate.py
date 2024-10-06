#     Python file to implement the class CrewMate
from heap import Heap
from treasure import Treasure
from custom import comp2
class CrewMate:

    # Class to implement a crewmate

    def __init__(self, comparison_function = comp2):
        self.treasures_list = []
        self.treasures = Heap(comparison_function , self.treasures_list)
        self.total_load = 0
        # Arguments:
        #     None
        # Returns:
        #     None
        # Description:
        #     Initializes the crewmate

        # Write your code here
    # Add more methods if required

    def assign_treasure(self, treasure : Treasure):
        self.treasures.insert((treasure.priority(), treasure))
        self.total_load += treasure.size

    def process_treasure(self, time_units, time):
        # """
        # Processes the treasure with the highest priority for a given amount of time.
        #
        # Arguments:
        #     time_units: The number of time units to process the current treasure.
        # """

        while not self.treasures.isEmpty() or time_units>0:
            treasure = self.treasures.extract()[1]
            processed_treasure = min(time_units, treasure.size)
            time_units -= processed_treasure
            time += processed_treasure
            treasure.size -= processed_treasure
            self.total_load -= processed_treasure
            if treasure.size != 0:
                self.treasures.insert((treasure.size, treasure))
            # If the treasure is fully processed, remove it from the heap
        return time

    #

    def isEmpty(self):
        # """
        # Checks if the crewmate has any treasures to process.
        #
        # Returns:
        #     True if the crewmate has no treasures, False otherwise.
        # """
        return self.treasures.size == 0
