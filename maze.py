from node import Node

class Maze:
    """ For refering nodes to search """

    def __init__(self, map):
        self.map_location = map
        self.map = {}
        self.goal = None
        self.start = None
        self.map_height = None
        self.map_width = None
        self.space_in = 1
        self.path = None

        
    
    def read_map(self):
        """ gets the location of the goal: @ and start: $ """ 

        # important
        start = None
        goal = None
        width = 0
        height = 0


        # reads the map from the file
        f = open(self.map_location, 'r')

        # Loop through and find needed info
        for line in f:
            for ind, i in enumerate(line.strip()):
                self.map[(ind, height)] = i

                # Start was found ?
                if i == '@':
                    start = (ind, height)
                # Goal was found ?
                if i == '$':
                    goal = (ind, height)
                
            height += 1

            width = len(line)
        
        # Saving the goal and start locations
        self.goal = goal
        self.start = start

        # width and height of the map
        self.map_height = height
        self.map_width = width

        # Closing the file
        f.close()
                             
    def draw_map(self):
        for y in range(self.map_height):
            for x in range(self.map_width):
                print('%%-%ds' % self.space_in % self.draw_tile(self.map, (x, y)), end='')
            print()


    def draw_tile(self, map, pos, **kwargs):
        """ Extracting data (value) from the map"""

        val = map.get(pos)
        
        # Check if path is needed to be print
        # replacing path if found with Xs
        if 'path' in kwargs and pos in kwargs['path']:
            val = 'X'
        
        # Check if we should print start point
        if 'start' in kwargs and pos == kwargs['start']: 
            val = '@'
        # Check if we should print the goal point
        if 'goal' in kwargs and pos == kwargs['goal']: 
            val = '$'
        # Return a tile value
        return val
    
    def solve_map(self, map, start, goal):
        """ Solving the map using Best First Search algo, i am not going to use priorityQueue here , maybe later """

        def neighbor_nodes(node):

            """ Getting all neighbors to a spacific node  """

            x_pos , y_pos = node.pos

            # all possible operators up, down, right and left to the node
            return [(x_pos-1, y_pos), (x_pos+1, y_pos), (x_pos, y_pos+1), (x_pos, y_pos-1)]

        
        def add_to_open(open, neighbor):

            """ Check if a neighbor should be added to open list """

            for node in open:
                if (neighbor == node and neighbor.f >= node.f):
                    return False

            return True

        # Creating open & closed list to keep track of visited nodes which path to take
        opened = []
        closed = []

        # Creating a starting node and goal node having no parents
        start_node = Node(start, None)
        goal_node = Node(goal, None)

        # Inserting the start Node to the Open list
        opened.append(start_node)

        # Looping until the goal is found (when the open list is empty)
        while len(opened):

            # Sorting the openlist
            opened.sort()

            # Getting the first element as the current node 
            current_node = opened.pop(0)

            # adding the current node to the closed list 
            closed.append(current_node)

            # Checking if the goal was found
            if current_node == goal_node:
                path = []

                # append path from end to start
                while current_node != start_node:
                    path.append(current_node.pos)
                    current_node = current_node.parent

                return path[::-1]

            # getting the neighbors to a node using the position x,y of the node which is stored in the map
            neighbors = neighbor_nodes(current_node)

            # get all the neighboring nodes 
            for n in neighbors:

                # getting stored val from the map
                val = map.get(n)

                # check if the value is not the goal (wall)
                if val == '#':
                    continue

                # if the value isn't a wall : means it's a valid path
                # link it to the current_node it's from 
                neighbor = Node(n, current_node)

                if neighbor in closed:
                    continue

                # here the fun part 
                # using manhattan distance to update the h, f, g
                # heuristic due to the goal
                neighbor.h = abs(neighbor.pos[0] - goal_node.pos[0]) + abs(neighbor.pos[1] - goal_node.pos[1])
                neighbor.g = abs(neighbor.pos[0] - start_node.pos[0]) + abs(neighbor.pos[1] - start_node.pos[1])
                neighbor.f =  neighbor.h


                # check if neighbor in the open list and f value is small
                if add_to_open(opened , neighbor):
                    opened.append(neighbor)

        return closed



