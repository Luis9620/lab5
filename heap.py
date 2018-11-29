class Heap:
    def __init__(self):
        self.heap_array = []

    def insert(self, k):            #Add new element to the heap, maintaining heap property
        self.heap_array.append(k)

        i = len(self.heap_array) - 1

        while (i - 1 // 2) > 0:             #Bubble up
            if self.heap_array[i] < self.heap_array[(i - 1) // 2]:
                temp = self.heap_array[(i - 1) // 2]
                self.heap_array[(i - 1) // 2] = self.heap_array[i]
                self.heap_array[i] = temp
            i = (i - 1) // 2
        return self.heap_array

    def print(self):
        print("Heap size: ", len(self.heap_array))
        print("H: ", self.heap_array)
        print()


    def extract_min(self):          #Remove and return smallest element in heap, maintaining heap property
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
            if min == i:            #Heap order has been re-established
                break
            temp = self.heap_array[i]
            self.heap_array[i] = self.heap_array[min]
            self.heap_array[min] = temp
            i = min

        # TODO: Complete implementation
        return min_elem

    def is_empty(self):
        return len(self.heap_array)
