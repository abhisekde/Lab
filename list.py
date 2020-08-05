# Doubly linked list
class DLList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    class __Node:
        def __init__(self, value=None):
            self.value = value
            self.prev = None
            self.next = None

        def toString(self):
            return "<->" + self.value.__str__() + "<->"

    def Node(self, item):
        return DLList.__Node(item)

    def clear(self):
        trav = self.__head
        while trav.next != None:
            next = trav.next
            trav.value = None
            trav.prev = None
            trav.next = None
            trav = next
        self.__size = 0
        self.__head = None
        self.__tail = None

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.size() == 0

    def addItem(self, item):
        self.addLast(item)

    def addFirst(self, item):
        node = self.Node(item)
        if self.isEmpty():
            self.__tail = node
            self.__head = node
        else:
            self.__head.prev = node
            node.next = self.__head
            self.__head = node
        self.__size = self.__size + 1
        
    def addLast(self, item):
        node = self.Node(item)
        if self.isEmpty():
            self.__tail = node
            self.__head = node
        else:
            self.__tail.next = node
            node.prev = self.__tail
            self.__tail = node
        self.__size = self.__size + 1

    def peekFirst(self):
        if self.isEmpty():
            raise Exception("Empty list")
        return self.__head.value
    
    def peekLast(self):
        if self.isEmpty():
            raise Exception("Empty list")
        return self.__tail.value

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("Empty list")
        else:
            trav = self.__head
            value = trav.value
            self.__head = trav.next
            self.__size = self.__size -1
        if self.isEmpty():
            self.__tail = self.__head
        else:
            self.__head.prev = None
        trav = None
        return value

    def removeLast(self):
        if self.isEmpty():
            raise Exception("Empty list")
        else:
            trav = self.__tail
            value = trav.value
            self.__tail = trav.prev
            self.__size = self.__size -1
        if self.isEmpty():
            self.__head = self.__tail
        else:
            self.__tail.next = None
        trav = None
        return value

    def removeAt(self, index):
        if self.isEmpty():
            raise Exception("Empty list")
        else:
            trav = self.__head
            for i in range(0, int(self.size() * 0.5)):
                if i == index:
                    return self.__removeNode(trav)
                elif trav.next != None:
                    trav = trav.next
                else:
                    return None
            for i in range(int(self.size()*0.5), self.size()):
                if i == index:
                    return self.__removeNode(trav)
                elif trav.next != None:
                    trav = trav.next
                else:
                    return None

    def __removeNode(self, node):
        if node.next == None:
            return self.removeLast()
        elif node.prev == None:
            return self.removeFirst()
        else:
            self.__sise = self.size -1
            value = node.value
            node.prev.next = node.next
            node.next.prev = node.prev
            return value

    def indexOf(self, item):
        trav = self.__head
        index = 0
        while(trav != None):
            if trav.value == item:
                return index
            else:
                index = index +1
        return -1

    def contains(self, item):
        return self.indexOf(item) != -1
    
