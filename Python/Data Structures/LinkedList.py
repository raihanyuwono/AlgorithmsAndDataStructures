class Node:

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

class SingleLinkedList:
    
    _head = None
    _tail = None

    def get_head(self):
        return self._head.get_data()

    def get_tail(self):
        return self._tail.get_data()

    def is_empty(self):
        return self._head == None

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.set_next(self._head)
            self._head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.set_next(new_node)
            self._tail = new_node

    def find(self, data):
        current = self._head
        while current != None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False

    def to_list(self):
        nodes = list()
        current = self._head
        while current != None:
            nodes.append(current.get_data())
            current = current.get_next()
        return nodes

class DoubleLinkedList(SingleLinkedList):
    
    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._head.set_prev(new_node)
            new_node.set_next(self._head)
            self._head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.set_prev(self._tail)
            self._tail.set_next(new_node)
            self._tail = new_node


def main():
    linked_list = SingleLinkedList()
    linked_list.add_last(4)
    linked_list.add_last(1)
    print(linked_list.find(5))
    print(linked_list.to_list())
    linked_list.add_first(5)
    linked_list.add_last(10)
    print(linked_list.find(5))
    print(linked_list.to_list())
    print(linked_list.get_head())
    print(linked_list.get_tail())

if __name__ == '__main__':
    main()