# Dynamic arry implimentation using static array
class DArray:
    def __init__(self, size = 16):
        assert size > 0, "Array size has to be at least 1"
        self.__capacity = size
        self.__length = 0
        self.__array = []
        for _ in range(size):
            self.__array.append(None) # allocate n memory

    def length(self):
        return self.__length

    def isEmpty(self):
        empty = True 
        if self.__length > 0:
            empty = False
        return empty

    def get(self, index):
        assert index >= 0, "Array index starts at 0"
        assert index < self.__length, "Array index out of bound"
        return self.__array[index]
    
    def set(self, index, item):
        assert index >= 0, "Array index starts at 0"
        assert index < self.__capacity, "Array index out of bound"
        self.__array[index] = item
        self.__length = self.__length +1

    def clear(self):
        for i in range(self.__length):
            self.__array[i] = None
            self.__length = self.__length -1
            
    def add(self, item):
        if self.__length +1 > self.__capacity:
            if self.__capacity == 0:
                self.__array.append(None)
                self.__capacity = 1
            else:
                for _ in range(self.__capacity):
                    self.__array.append(None) # allocate +n memory
                self.__capacity = self.__capacity *2 
        self.__array[self.__length] = item
        self.__length = self.__length +1
    
    def removeAt(self, index):
        assert index >= 0, "Array index starts at 0"
        assert index < self.__capacity, "Array index out of bound"
        item = self.__array[index]
        arr2 = []
        for _ in range(self.__capacity):
            arr2.append(None)
        j = 0
        for i in range(self.__length):
            if i == index: 
                continue
            else:
                arr2[j] = self.__array[i]
                j = j +1
        self.__array = arr2 
        self.__length = self.__length -1
        return item

    def removeItem(self, item):
        itemFound = False
        index = 0
        for i in range(self.__length):
            if self.__array[i] == item:
                itemFound = True
                t = self.removeAt(index)
            index = index +1
        return itemFound

    def indexOf(self, item):
        for i in range(self.__length):
            if self.__array[i] == item:
                return i
        return -1

    def contains(self, item):
        return self.indexOf(item) != -1

    def toString(self):
        str = "[ " 
        for i in range(self.__length):
            str = str + self.__array[i].__str__() + " "
        str = str + "]"
        return str
