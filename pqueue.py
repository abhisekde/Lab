class PQueue:
    def __init__(self, elements = []):
        assert type(elements) == list, 'Invalid argument'
        self.__heap = [None for _ in elements]
        self.__capacity = max(1, len(elements))
        self.__size = 0
        for element in elements:
            self.add(element)
        if self.is_empty():
            self.__heap = [None]

    def size(self):
        return self.__size
    
    def is_empty(self):
        return self.__size == 0

    def add(self, item):
        if item == None:
            raise Exception('Invalid argument')
        if self.__size < self.__capacity:
            self.__heap[self.__size] = item
        else:
            self.__heap.append(item)
        self.__swim(self.__size)
        print(self.__heap)
        self.__size = self.__size +1

    def __swim(self, index):
        parent = int((index-1)/2)
        while parent >= 0 and self.__heap[parent] > self.__heap[index]:
            self.__swap(index, parent)
            index = parent
            parent = int((index-1)/2)

    def __sink(self, index):
        # find the min child
        left  = 2*index +1
        right = 2*index +2
        min = left
        if right < self.__size and self.__heap[right] < self.__heap[left]:
            min = right
        # check if parent is larger then child, if yes then swap
        if left < self.__size and self.__heap[min] < self.__heap[index]:
            self.__swap(index, min) 
            index = min
            return self.__sink(index)
        else:
             return True

    def __swap(self, index_1, index_2):
        print(index_1, index_2)
        item_1 = self.__heap[index_1]
        item_2 = self.__heap[index_2]
        self.__heap[index_1] = item_2
        self.__heap[index_2] = item_1

    def __repr__(self):
        out = ''
        if self.is_empty():
            return out 
        for i in range(self.__size):
            parent = i 
            left = 2*i +1
            right = 2*i +2
            if  left < self.__size:
                out = out + str(self.__heap[parent])
                out = out + '->(' + str(self.__heap[left])
                if right < self.__size:
                    out = out + ', ' + str(self.__heap[right]) + ')\n'
                else:
                    out = out + ', )\n'
            elif parent == 0 and self.__size == 1:
                out = out + str(self.__heap[parent])
        return out
        
    def removeAt(self, index):
        if self.is_empty():
            raise Exception('PQueue is empty')
        if index >= self.__size:
            raise Exception('Index out of bound')
        #swap with last element
        self.__swap(index, self.__size -1)
        value = self.__heap[self.__size -1]
        #remove the node
        self.__size = self.__size -1
        node = self.__heap[index]
        #try to swim up
        self.__sink(index)
        #if swim didn't work, try to sink down
        if node == self.__heap[index]:
            self.__swim(index)
        
        return value

    def pool(self):
        return self.removeAt(0)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__heap[0]
