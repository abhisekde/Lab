from list import DLList
class Queue:
    def __init__(self):
        self.__queue = DLList()
        self.__size = 0

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.__queue.addLast(item)
        self.__size = self.__size +1

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue empty')
        else:
            self.__size = self.__size -1
            return self.__queue.removeFirst()

    def peek(self):
        return self.__queue.peekFirst()
