class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        print(f'node value {self.value}')
    


class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None


    def insert(self, value):

        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root

        while True:

            if temp.value == value: return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


    def __r_contain(self, node, value):
            if node is None:
                return False
            if value == node.value:
                return True

            if value < node.value:
                return self.__r_contain(node.left, value)
            else:
                return self.__r_contain(node.right, value)
            
    def r_contain(self,value):

        return self.__r_contain(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        print("Current node value=", current_node.value)
        if value < current_node.value:
            current_node.left=self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        print(f'root {current_node.value if current_node else None} left {current_node.left.value if current_node.left else None} right {current_node.right.value if current_node.right else None}')
        return current_node
        
    def r_insert(self,value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    
    def min_value(self, current_node):

        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def __r_delete(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None: 
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                min_node_value = self.min_value(current_node.right)
                current_node.value = min_node_value
                current_node.right = self.__r_delete(current_node.right, min_node_value)
        return current_node
    
    # def help_traverse()

    def __in_order(self, current_node):
        
        if current_node is None:
            return None
        current_node.left = self.__in_order(current_node.left)
        print(current_node.value, end = " ")
        current_node.right = self.__in_order(current_node.right)
    
    def __pre_order(self, current_node):
        if current_node is None:
            return None
        print(current_node.value, end=" ")
        self.__pre_order(current_node.left)
        self.__pre_order(current_node.right)

    def r_pre_order(self):
        if self.root is None:
            return []
        self.__pre_order(self.root)
    
    def r_in_order_traverse(self):
        if self.root is None:
            return []
        return self.__in_order(self.root)
    
    def __r_post_order(self, current_node):
        if current_node is None:
            return None
        
        self.__r_post_order(current_node.left)
        self.__r_post_order(current_node.right)
        print(current_node.value, end=" ")

    def r_post_order(self):
        if self.root is None:
            return []
        self.__r_post_order(self.root)

    
    def BFS(self): #levelOrder
        current_node =self.root
        queue = []
        results = []
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
               
                queue.append(current_node.left)
               
            if current_node.right is not None:
        
                queue.append(current_node.right)
        return results
    
    def invert(self):
        current_node = self.root

        def invert_ruc(node):
            if not node:
                return 
            
            temp = node.left
            node.left = node.right
            node.right = temp

            invert_ruc(node.left)
            invert_ruc(node.right)

        invert_ruc(current_node)

    def maxDepth(self):
        if not self.root:
            return 0
        
        # current = self.root
        def max_depth_rec(node):
            # print(node)
            if not node:
                return 0
            # max_left = max_depth_rec(node.left)
            # max_right = max_depth_rec(node.right)
            # print(f'max left  {max_left} max right {max_right}')
            return 1 + max(max_depth_rec(node.left), max_depth_rec(node.right))
        
        res = max_depth_rec(self.root)
        
        return res
    

        

    
        

    

        
    




bsearch = BinarySearchTree()

bsearch.r_insert(4)
bsearch.r_insert(2)
bsearch.r_insert(7)
# bsearch.r_insert(1)
# bsearch.r_insert(3)
# bsearch.r_insert(6)
# bsearch.r_insert(9)
# bsearch.invert()
print(bsearch.maxDepth())
# bsearch.r_insert(18)
# bsearch.r_insert(24)
# bsearch.r_insert(50)
# bsearch.r_insert(35)
# bsearch.r_insert(31)
# bsearch.r_insert(44)
# bsearch.r_insert(70)
# bsearch.r_insert(66)
# bsearch.r_insert(90)

# bsearch.r_pre_order()
# bsearch.r_in_order_traverse()
# bsearch.r_post_order()
# bsearch.r_contain(12)



# print(bsearch.r_in_order_traverse())




# print("insert = ",bsearch.r_insert(40))



# print(bsearch.r_contain(2))
# print(bsearch.r_contain(90))
# print(bsearch.r_contain(3))
