'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import Crewmate
from heap import Heap
from treasure import Treasure
from custom import *
def comp3(t1, t2):
        if t1.arrival_time + t1.size == t2.arrival_time + t2.size:
             return t1.id < t2.id
        return t1.arrival_time + t1.size < t2.arrival_time + t2.size

class StrawHatTreasury:
    def __init__(self, m):
        self.crewmates = CrewmateHeap()
        self.treasures = []
        self.current_time = 0

        for _ in range(m):
            crewmate = Crewmate()
            self.crewmates.insert(crewmate)

    def add_treasure(self, treasure):
        # self.current_time = max(self.current_time, treasure.arrival_time)

        least_loaded_crewmate = self.crewmates.extract_min()
        least_loaded_crewmate.treasures.append(treasure)
        # crrewmatetop.load = treasure.size + max(crewmatetop.workload,treasure.arrivaltime)
        least_loaded_crewmate.load = treasure.size + max(least_loaded_crewmate.load , treasure.arrival_time)
        self.crewmates.insert(least_loaded_crewmate)
        self.treasures.append(treasure)

    def get_completion_time(self):
        final_list = []
        for crewmate in self.crewmates:
            treasures_list = crewmate.treasures

            imp_list = Heap(comp3)
            t1 = 0
            t2 = 0
            for treasure in treasures_list:
                t2 = treasure.arrival_time
                while t2-t1>0:
                    if imp_list.__len__ is None:
                         t1 = t2
                         imp_list.insert(treasure)
                         continue
                    temp_tres = imp_list.extract()
                    if t2-t1 < temp_tres.size:
                         temp_tres.size -= t2-t1
                         t1 = t2
                         imp_list.insert(treasure)
                         continue
                    if t2 - t1 > temp_tres.size:
                         t1 += temp_tres.size
                         temp_tres.size = 0
                         temp_tres.completion_time = t1
                         final_list.append(temp_tres)

                         
                imp_list.insert(treasure)
                while(imp_list):
                     temp = imp_list.extract()
                     t2 += temp.size
                     temp.completion_time = t2
                     final_list.append(temp)

        return [(t.id, t.completion_time) for t in sorted(self.treasures, key=lambda t: t.id)]
