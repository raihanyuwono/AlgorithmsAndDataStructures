class TreeNode:
    def __init__(self, data):
        self.__data = data
        self.__leftChild = None
        self.__rightChild = None
    
    def set_data(self, data):
        self.__data = data

    def set_left_child(self, leftChild):
        self.__leftChild = leftChild

    def set_right_child(self, rightChild):
        self.__rightChild = rightChild

    def get_data(self):
        return self.__data

    def get_left_child(self):
        return self.__leftChild

    def get_right_child(self):
        return self.__rightChild

class LinkedlistNode:

    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None

    def set_data(self, data):
        self.__data = data

    def set_next(self, next_node):
        self.__next = next_node

    def set_prev(self, prev_node):
        self.__prev = prev_node

    def get_data(self):
        return self.__data

    def get_prev(self):
        return self.__prev

    def get_next(self):
        return self.__next