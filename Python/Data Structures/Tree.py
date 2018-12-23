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

class BinaryTree:

    __root = None

    def __init__(self, list_data=None):
        self.__root = None
        if list_data != None:
            self.create(list_data)

    def is_empty(self, node='root'):
        """
            Return True if node is empty and False otherwise
        """
        cur_node = self.__root if node == 'root' else node
        return cur_node == None

    def create(self, list_data):
        """
            Create a binary tree base on given 'list_data'
        """
        for data in list_data:
            self.add(data)

    def add(self, data):
        """
            Add new data to the binary tree
        """
        new_node = TreeNode(data)
        if self.is_empty():
            self.__root = new_node
        else:
            self.__add_child(self.__root, new_node)

    def __add_child(self, parent, new_node):
        if new_node.get_data() <= parent.get_data():
            if self.is_empty(parent.get_left_child()):
                parent.set_left_child(new_node)
            else:
                self.__add_child(parent.get_left_child(), new_node)
        else:
            if self.is_empty(parent.get_right_child()):
                parent.set_right_child(new_node)
            else:
                self.__add_child(parent.get_right_child(), new_node)

    def find(self, key, node='root'):
        """
            Return True if there is key in the binary tree and False otherwise
        """
        cur_node = self.__root if node == 'root' else node
        if self.is_empty(node):
            return False
        elif key == cur_node.get_data():
            return True
        else:
            return self.find(key, cur_node.get_left_child() if key <= cur_node.get_data() else cur_node.get_right_child())

    def get_all_data(self, node='root'):
        """
            Return list of sorted data in the binary tree 
        """
        datas = list()
        cur_node = self.__root if node == 'root' else node
        if not self.is_empty(cur_node):
            datas.extend(self.get_all_data(cur_node.get_left_child()))
            datas.append(cur_node.get_data())
            datas.extend(self.get_all_data(cur_node.get_right_child()))
            return datas
        else:
            return []

def main():
    list_data = [7, 5, 3, 11, 20, 4, 1, 13, 17, 10]
    tree = BinaryTree(list_data)
    print(tree.get_all_data())
    print(tree.find(15))
    tree.add(15)
    print(tree.get_all_data())
    print(tree.find(15))

if __name__ == '__main__':
    main()