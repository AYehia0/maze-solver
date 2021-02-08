# Main file for showing off
from maze import Maze

m = Maze('maze_map.txt')
m.read_map()
path = m.solve_map(m.map, m.start, m.goal)
m.draw_steps(path)
