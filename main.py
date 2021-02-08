# Main file for showing off
from maze import Maze

m = Maze('maze_map.txt')
m.read_map()
m.draw_map()
print(f"Start Position:{m.start}, Goal Position:{m.goal}")
print(len(m.solve_map(m.map, m.start, m.goal)))
