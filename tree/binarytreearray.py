class BinaryTree:

    def __init__(self, size) -> None:
        self.arr = ["" for x in range(size +1)]
        self.lastUsedIndex = 0

    def is_full(self):
        return True if len(self.arr) - 1 == self.lastUsedIndex else False
    
    def insert(self, value):
        if not self.is_full():
            self.lastUsedIndex +=1
            self.arr[self.lastUsedIndex] = value
            return True
        return False
    
    def pre_order(self, index):
        if index > self.lastUsedIndex:
            return 
        print(self.arr[index], end=" ")
        self.pre_order(index * 2)
        self.pre_order(index * 2 + 1)

    def in_order(self, index):
        if  index > self.lastUsedIndex:
            return 
        self.pre_order(index * 2)
        print(self.arr[index], end=" ")
        self.pre_order(index * 2 + 1)
    
    def post_order(self, index):
        if  index > self.lastUsedIndex:
            return 
        self.pre_order(index * 2)
        self.pre_order(index * 2 + 1)
        print(self.arr[index], end=" ")
    
    def bfs_or_order_level(self):
        result = []
        queue = []

        if self.lastUsedIndex > 0:
            queue.append(1)

        while queue:
            index = queue.pop(0)
            if index > self.lastUsedIndex:
                return result
            result.append(self.arr[index])
            queue.append(index * 2)
            queue.append(index * 2 + 1)


        return result
    
    def level_order(self):
        for x in range(1, self.lastUsedIndex + 1):
            print(self.arr[x], end= " ")

    def search(self, value):
        for x in range(1, self.lastUsedIndex + 1):
            if self.arr[x] == value:
                return x
        return -1 
    
    def delete_node(self, value):
        index = self.search(value)
        if index < 0:
            return False
        
        self.arr[index] = self.arr[self.lastUsedIndex]
        self.arr[self.lastUsedIndex] = ''
        self.lastUsedIndex -= 1

        return True
    



b_tree_array = BinaryTree(9)

b_tree_array.insert('N1')
b_tree_array.insert('N2')
b_tree_array.insert('N3')
b_tree_array.insert('N4')
b_tree_array.insert('N5')
b_tree_array.insert('N6')
b_tree_array.insert('N7')
b_tree_array.insert('N8')
b_tree_array.insert('N9')

print(b_tree_array.arr)
b_tree_array.pre_order(1)
print()
b_tree_array.in_order(1)
print()
b_tree_array.post_order(1)
print()
print(b_tree_array.bfs_or_order_level())
b_tree_array.level_order()
print()
b_tree_array.delete_node('N3')
print(b_tree_array.arr)
