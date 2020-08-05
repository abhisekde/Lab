class UnionFind:
    def __init__(self, size):
        assert size > 0, 'Size can not be -ve' 
        self.__size = size
        self.__get_root = [i for i in range(size)] #initally all are root node
        self.__grp_size = [1 for _ in range(size)] #so size is 1
        self.__num_grps = size

    def find(self, node):
        assert node >= 0 and node < self.__size, 'Invalid index' 
        root = node
        n = node
        while self.__get_root[n] != n:
            n = self.__get_root[n]
            root = n
        #compress path
        n = node
        while self.__get_root[n] != root:
            p = self.__get_root[n] 
            self.__get_root[n] = root
            n = p
        return root

    def is_connected(self, node_x, node_y):
        assert node_x >= 0 and node_y >= 0 and node_x!= node_y and node_x < self.__size and node_y < self.__size, 'Invalid arguments'
        return self.find(node_x) == self.find(node_y)

    def unify(self, p, q):
        assert p >= 0 and q >= 0 and p!= q and p < self.__size and q < self.__size, 'Invalid arguments'
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        size_p = self.__grp_size[root_p]
        size_q = self.__grp_size[root_q]

        if size_p > size_q:
            self.__get_root[q] = p
            self.__grp_size[p] = self.__grp_size[p] + self.__grp_size[q]
        else:
             self.__get_root[p] = q
             self.__grp_size[q] = self.__grp_size[q] + self.__grp_size[p]      
        self.__num_grps = self.__num_grps -1

    def count_grp_size(self, node):
        assert node >= 0 and node < self.__size, 'Index can not be -ve' 
        return self.__grp_size[node]

