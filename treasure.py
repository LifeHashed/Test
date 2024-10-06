'''
    Python file to implement the Treasure class
'''

class Treasure:
    '''
    Class to implement a treasure
    '''
    
    def __init__(self, id, size, arrival_time):
        # DO NOT EDIT THE __init__ method
        self.id = id
        self.size = size
        self.arrival_time = arrival_time
        self.completion_time = None
    
    def set_original_time(self):
        '''
        Sets the original size after initialization.
        '''
        if not hasattr(self, 'o_time'):
            self.o_time = self.size  # Store original size in o_time
    
    def reset_size(self):
        '''
        Resets the size to the original value stored in o_time.
        '''
        if hasattr(self, 'o_time'):
            self.size = self.o_time  # Reset size to original


    
    
    # You can add more methods if required