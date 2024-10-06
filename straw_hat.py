
    # This file contains the class definition for the StrawHat class.


from crewmate import CrewMate
from heap import Heap
from treasure import Treasure
from custom import comp1
from custom import comp2


class StrawHatTreasury:

    # Class to implement the StrawHat Crew Treasury


    def __init__(self, m):

        # Arguments:
        #     m : int : Number of Crew Mates (positive integer)
        # Returns:
        #     None
        # Description:
        #     Initializes the StrawHat
        # Time Complexity:
        #     O(m)


        # Write your code here
        self.crewmates_array = [(0,CrewMate()) for _ in range(m)]
        self.crewmates = Heap(comparison_function=comp2, init_array=self.crewmates_array)
        self.treasures_list = []

    def add_treasure(self, treasure : Treasure):

        # Arguments:
        #     treasure : Treasure : The treasure to be added to the treasury
        # Returns:
        #     None
        # Description:
        #     Adds the treasure to the treasury
        # Time Complexity:
        #     O(log(m) + log(n)) where
        #         m : Number of Crew Mates
        #         n : Number of Treasures

        chosen_crew = self.crewmates.extract()[1]
        chosen_crew.assign_treasure(treasure)
        self.crewmates.insert((chosen_crew.total_load, chosen_crew))
        self.treasures_list.append(treasure)

        # Write your code here



    def get_completion_time(self):

        # Arguments:
        #     None
        # Returns:
        #     List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        # Description:
        #     Returns all the treasure after processing them
        # Time Complexity:
        #     O(n(log(m) + log(n))) where
        #         m : Number of Crew Mates
        #         n : Number of Treasures

        treasures = sorted(self.treasures_list, key=lambda t: t.arrival_time)
        time = 0
        for i in range(len(treasures)):
            treasure = treasures[i]
            time = treasure.arrival_time
            chosen_crew = self.crewmates.extract()[1]
            x = self.crewmates.extract()[0]
            try:
                time_units = treasures[i+1].arrival_time - treasure[i].arrival_time
            except:
                time_units =  x
            chosen_crew.assign_treasure(treasure)
            time = chosen_crew.process_treasure(time_units, time)
            if treasure.size == 0:
                treasure.completion_time = time

        return sorted(self.treasures_list, key=lambda t: t.id)

        # Write your code here



    # You can add more methods if required

