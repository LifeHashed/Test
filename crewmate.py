class Crewmate:
    def __init__(self):
        self.load = 0  # Total remaining size of treasures assigned
        self.treasures = []  # Max-heap to manage treasures by priority
