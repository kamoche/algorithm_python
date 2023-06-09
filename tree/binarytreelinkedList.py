class BinaryNode:

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    
class BinaryTree:

    def __init__(self) -> None:
        self.root = None

    

    def search(self, value):

        if self.root:

            queue = []
            queue.append(self.root)

            while queue:
                current = queue.pop(0)

                if current.value == value:
                    return True
                
                if current.left is not None:
                    queue.append(current.left)
                
                if current.right is not None:
                    queue.append(current.right)
            
        return False
    
    def insert(self, value):
        current_node = self.root
        new_node = BinaryNode(value)

        queue = []
        queue.append(current_node)

        while queue:

            current_node = queue.pop(0)

            if current_node.left is None:
                current_node.left = new_node
                break
            queue.append(current_node.left)
            if current_node.right is None:
                current_node.right = new_node
                break
            queue.append(current_node.right)

    
    def in_order(self):
        current_node = self.root
        
        def in_order_ruc(current_node):
            if current_node is None:
                return
            in_order_ruc(current_node.left)
            print(current_node.value, end="")
            in_order_ruc(current_node.right)
        
        in_order_ruc(current_node)

    def post_order(self):
        current_node = self.root
        
        def order_ruc(current_node):
            if current_node is None:
                return
            order_ruc(current_node.left)
            order_ruc(current_node.right)
            print(current_node.value, end="")
        
        order_ruc(current_node)

    def pre_order(self):
        current_node = self.root
        
        def in_order_ruc(current_node):
            if current_node is None:
                return
            print(current_node.value, end="")
            in_order_ruc(current_node.left)
            in_order_ruc(current_node.right)
        
        in_order_ruc(current_node)

    def find_deepest_node(self):
        current_node = self.root
        queue = []
        queue.append(current_node)

        while queue:
            current_node = queue.pop(0)

            if current_node.left  is not None:
                queue.append(current_node.next)
            
            if current_node.right is not None:
                queue.append(current_node.next)

        return current_node
    
    def delete_deepest_node(self):
        current_node = self.root
        queue = []
        queue.append(current_node)
        previous_node = None

        while queue:
            previous_node = current_node
            current_node = queue.pop(0)

            if current_node.left is None:
                previous_node.right = None
                return
            elif current_node.right is None:
                current_node.left = None
                return
            else:
                queue.append(current_node.left)
                queue.append(current_node.right)
























    def delete_node(self, value):

        if self.root is None:
            return False
        current_node = self.root
        queue = []
        queue.append(current_node)

        while queue:
            current_node = queue.pop(0)

            if current_node.value == value:
                current_node.value = self.find_deepest_node()
                self.delete_deepest_node()
                return True
            if current_node.left is not None:
                queue.append(current_node.left)
            
            if current_node.right is not None:
                queue.append(current_node.right)
        
        return False

                






    