class Heap:
    def __init__(self):
        self.heap_array = []

    def insert(self, k):
        # add the new value to the end of the array.
        self.heap_array.append(k)
        # TODO: Complete implementation
        # percolate up from the last index to restore heap property.
        i = len(self.heap_array)-1
        while((i > 0) and (k < self.heap_array[(i - 1) // 2])):
            self.heap_array[i] = self.heap_array[(i - 1) // 2]
            i = i//2
        self.heap_array[i] = k
        return i


    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array[0]
        self.heap_array[0] = self.heap_array[len(self.heap_array)-1]
        self.heap_array.pop(len(self.heap_array) - 1)
        i = 0
        min = 0
        while((2 * i + 1) <= len(self.heap_array) - 1):
            if (2*i + 1 <= len(self.heap_array)-1 and self.heap_array[min] > self.heap_array[2*i + 1]):
                min = 2*i + 1
            if (2 * i + 2 <= len(self.heap_array)-1 and self.heap_array[min] > self.heap_array[2 * i + 2]):
                min = 2 * i + 2
            if min == i:
                break
            temp = self.heap_array[i]
            self.heap_array[i] = self.heap_array[min]
            self.heap_array[min] = temp
            i = min

        # TODO: Complete implementation
        return min_elem

    def is_empty(self):
        return len(self.heap_array) == 0