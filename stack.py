from list import DLList
# Stack with linked list
class Stack:
    def __init__(self):
        self.__stack = DLList()
        self.__top = None
    def push(self, item):
        return self.__stack.addFirst(item)

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack empty')
        return self.__stack.removeFirst()

    def size(self):
        return self.__stack.size()

    def isEmpty(self):
        return self.size() == 0

    def peek(self):
        if self.isEmpty():
            raise Exception('Stack empty')
        return self.__stack.peekFirst()
