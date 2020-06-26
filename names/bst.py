class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)    
        # compare to the new value we want to insert
        new_node = BSTNode(value)
        
        # if new value < self.value
            # IF self.left is already taken by a node
                # make that (left) node, call insert 
            # set the left to the new node with the new value
        if value < self.value:
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(value)
        
            # if new value >= self.value
            # IF self.right is already taken by a node
                # make that (right) node call insert 
            # set the right child to the new node with new value
            
        elif value >= self.value:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(value)
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        # Compare the target to current value
        # If current target < value
        found = False
        if target < self.value:
            # Check the left subtree (self.left.contains(target))
            # If you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)
            
        # If current target >= value
        if target >= self.value:
            # Check if right subtree contains target
            # If you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found