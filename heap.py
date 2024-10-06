class Heap:
    def __init__(self, comparison_function, elements=None):
        self.comparison_function = comparison_function
        self.heap = []
        if elements:
            self.heap = elements[:]
            self._build_heap()

    def _build_heap(self):
        for i in reversed(range(len(self.heap) // 2)):
            self._heapify_down(i)

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        parent = self._parent(index)
        if index > 0 and self.comparison_function(self.heap[index], self.heap[parent]):
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = self._left_child(index)
        right = self._right_child(index)
        smallest = index

        if left < len(self.heap) and self.comparison_function(self.heap[left], self.heap[smallest]):
            smallest = left
        if right < len(self.heap) and self.comparison_function(self.heap[right], self.heap[smallest]):
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        if not self.heap:
            raise IndexError("Extract from an empty heap.")
        if len(self.heap) == 1:
            return self.heap.pop()

        extracted = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return extracted

    def top(self):
        if not self.heap:
            raise IndexError("Top from an empty heap.")
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return ' '.join(str(e) for e in self.heap)

    def is_empty(self):
        return len(self.heap) == 0