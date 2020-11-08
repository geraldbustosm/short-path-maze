import numpy as np
import random

def make_maze(n, m):
    # Valores iniciales para la posición de partida y posición final
    spirit_position = [random.randint(0, n-1), random.randint(0, m-1)]
    goal_position = [random.randint(0, n-1), random.randint(0, m-1)]

    # En caso de que la posición de partida sea igual a la final,
    # buscamos un nuevo valor para la posición final
    while(spirit_position == goal_position): goal_position = [random.randint(0, n-1), random.randint(0, m-1)]

    # Posibles valores que pueden tomar las casillas
    possibles_boxes = ["-", ".", "ll", "a"]

    # Generando el tablero de tamaño nxm
    maze = []
    for i in range(n):
        maze.append([])
        for j in range(m):
            maze[i].append(possibles_boxes[random.randint(0, len(possibles_boxes)-1)])
    
    # Asignando las posiciones de spirit y la meta en el tablero
    maze[spirit_position[0]][spirit_position[1]] = "s"
    maze[goal_position[0]][goal_position[1]] = "x"
    return maze

def adjacency_matrix(maze):
    # Tamaño de la matriz de adyacencia
    n = len(maze)
    m = len(maze[0])
    size = n * m

    # Matriz auxiliar para obtener las posiciones
    numered_matrix = []
    count = 0
    for i in range(n):
        numered_matrix.append([])
        for j in range(m):
            numered_matrix[i].append(count)
            count = count + 1
            
    # Creando la matriz de adyacencia y asignando el tamaño de esta  
    adjacency = np.zeros((size, size))

    # Recorriendo la matriz numerada para rellenar la matriz de adyacencia
    for i in range(n):
        for j in range(m):
            if(j+1 < m):
                adjacency[numered_matrix[i][j]][numered_matrix[i][j+1]] = 1
            if(i+1 < n):
                adjacency[numered_matrix[i][j]][numered_matrix[i+1][j]] = 1
            if(j-1 >= 0):
                adjacency[numered_matrix[i][j]][numered_matrix[i][j-1]] = 1
            if(i-1 >= 0):
                adjacency[numered_matrix[i][j]][numered_matrix[i-1][j]] = 1

    return adjacency

maze = make_maze(2,2)
adjacency = adjacency(maze)

print(np.array(maze))
print(adjacency)