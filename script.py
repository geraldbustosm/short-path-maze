import numpy as np
import random

def make_maze(n, m):
    # Variables iniciales
    spirit_position = [random.randint(0, n-1), random.randint(0, m-1)]
    goal_position = [random.randint(0, n-1), random.randint(0, m-1)]
    possibles_boxes = ["-", ".", "ll", "a"]

    # Nos aseguramos que la posicion de partida sea distinta a la posicion final
    while(spirit_position == goal_position): goal_position = [random.randint(0, n-1), random.randint(0, m-1)]

    # Generando el tablero de tamaño nxm
    maze = []
    for i in range(n):
        maze.append([])
        for j in range(m):
            maze[i].append(possibles_boxes[random.randint(0, len(possibles_boxes)-1)])
    
    maze[spirit_position[0]][spirit_position[1]] = "s"
    maze[goal_position[0]][goal_position[1]] = "x"
    return maze

maze = make_maze(10,10)
print(np.array(maze))