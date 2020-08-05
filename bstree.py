class BSTree:

    class __Node:
        def __init__(self, value):
            assert type(value) == int, 'Value should be integer type'
            self.left = None
            self.right = None
            self.value = value
        
        def __repr__(self):
            return str(self.value)

    def __init__(self):
        self.__size = 0
        self.__root = None
        self.__trav = [None]
        self.__text = ''

    def size(self):
        return self.__size

    def add(self, value):
        assert type(value) == int, 'Value should be integer type'
        if self.__contains(self.__root, value):
            return False
        else:
            self.__root = self.__add(self.__root, value)
            self.__size = self.__size +1
            return True

    def __contains(self, node, item):
        if node == None:
            return False
        comp = item -node.value
        if comp == 0:
            return True
        elif comp < 0:
            return self.__contains(node.left, item)
        elif comp > 0:
            return self.__contains(node.right, item)

    def __add(self, node, item):
        if node == None:
            return BSTree.__Node(item)

        comp = item -node.value
        if comp < 0:
            node.left = self.__add(node.left, item)
        elif comp > 0:
            node.right = self.__add(node.right, item)
        return node

    def remove(self, item):
        if self.__contains(self.__root, item):
            self.__root = self.__remove(self.__root, item)
            self.__size = self.__size -1
            return True
        return False

    def __remove(self, node, item):
        comp = item -node.value
        if comp == 0:
            if node.left == None and node.right == None:
                node = None
            elif node.left == None:
                node.value = node.right.value
                node.right = self.__remove(node.right, node.value)
            elif node.right == None:
                node.value = node.left
                node.left = self.__remove(node.left, node.value)
            else:
                l_value = self.__dig_left(node.right)
                node.value = l_value
                node.right = self.__remove(node.right, l_value)
        elif comp < 0:
            node.left = self.__remove(node.left, item)
        else:
            node.right = self.__remove(node.right, item)
        return node

    def __dig_left(self, node):
        while node.left != None:
            return self.__dig_left(node.left)
        return node.value

    def __trav_pre(self, node):
        if node == None:
            t = ''
        else:
            t = str(node.value) 
            self.__text = self.__text + t 
            if node.left != None:
                self.__text = self.__text + ' ' + t + 'L: '
                self.__trav_pre(node.left)
            if node.right != None:
                self.__text = self.__text + ' ' + t + 'R: '
                self.__trav_pre(node.right)

    def __repr__(self):
        self.__text = ''
        self.__trav_pre(self.__root)
        return self.__text
