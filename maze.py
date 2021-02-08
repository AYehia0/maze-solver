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

    


m = Maze('maze_map.txt')
m.read_map()
m.draw_map()