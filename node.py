class Node:
    """ Node class used to save locations and make nodes """

    def __init__(self, pos:(), parent:() ):
        self.pos = pos
        self.parent = parent
        
        # Cost function
        self.f = 0 

        # Heurestic function
        self.h = 0

        # Estimated cost (number of steps made to goal)
        self.g = 0

    def __repr__(self):

        """ representation of the node if you print it """
        return f"Position:{self.pos}, Cost:{self.f}"
    
    
    def __lt__(self, other_node):
        """ Used for sorting the nodes """

        return self.f < other_node.f 

    def __eq__(self, other_node):
        """ Comparing Nodes positions """

        return self.pos == other_node.pos


# n = Node((1,1), None)
# n1 = Node((1,1), 2)

# print(n)

# print(n1 == n)