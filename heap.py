class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array=[]):
        '''
        Initializes the heap with a comparison function
        '''
        self.comparison_function = comparison_function
        self.heap = init_array
        self.build_heap()
    
    def build_heap(self):
        '''
        Builds the heap from an initial array
        Time Complexity: O(n)
        '''
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)
    
    def heapify_down(self, index):
        '''
        Moves the element at index down to maintain heap property
        '''
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.comparison_function(self.heap[left], self.heap[smallest]):
            smallest = left
        if right < len(self.heap) and self.comparison_function(self.heap[right], self.heap[smallest]):
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)
    
    def heapify_up(self, index):
        '''
        Moves the element at index up to maintain heap property
        '''
        parent = (index - 1) // 2
        if index > 0 and self.comparison_function(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)
    
    def insert(self, value):
        '''
        Inserts a value into the heap
        Time Complexity: O(log(n))
        '''
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def extract(self):
        '''
        Extracts the top element from the heap
        Time Complexity: O(log(n))
        '''
        if len(self.heap) == 0:
            return None
        top = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return top
    
    def top(self):
        '''
        Returns the top element of the heap
        Time Complexity: O(1)
        '''
        if len(self.heap) > 0:
            return self.heap[0]
        return None
