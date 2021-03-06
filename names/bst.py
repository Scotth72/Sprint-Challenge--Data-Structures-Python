class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        else:
            if target < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if not self.right:
                    return False
                else:
                    return self.right.contains(target)

    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()
    # def get_max(self):
    #     if not self.right:
    #         return self.value
    #     return self.right.get_max()
    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # this method wants to traverse every tree node
        # this has to call the fn on self.value
        fn(self.value)
        # how do we propagate to all the other nodes in the tree
        # is there a left child?
        if self.left:
            # if yes call its 'for_each' with the same fn
            self.left.for_each(fn)
        # is there a right child?
        if self.right:
            # if yes call its 'for_each' with the same fn
            self.right.for_each(fn)
