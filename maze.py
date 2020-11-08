import numpy as np
import random

class Maze:
    def __init__(self, n, m):
        # Valores iniciales para la posición de partida y posición final
        spirit_position = [random.randint(0, n-1), random.randint(0, m-1)]
        goal_position = [random.randint(0, n-1), random.randint(0, m-1)]

        # En caso de que la posición de partida sea igual a la final,
        # buscamos un nuevo valor para la posición final
        while(spirit_position == goal_position): goal_position = [random.randint(0, n-1), random.randint(0, m-1)]

        # Posibles valores que pueden tomar las casillas
        possibles_boxes = ["-", ".", "ll", "a"]

        # Generando el tablero de tamaño nxm
        self.__maze = []
        for i in range(n):
            self.__maze.append([])
            for j in range(m):
                self.__maze[i].append(possibles_boxes[random.randint(0, len(possibles_boxes)-1)])
        
        # Asignando las posiciones de spirit y la meta en el tablero
        self.__maze[spirit_position[0]][spirit_position[1]] = "s"
        self.__maze[goal_position[0]][goal_position[1]] = "x"

    def __adjacency_matrix(self):
        # Tamaño de la matriz de adyacencia
        n = len(self.__maze)
        m = len(self.__maze[0])
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
    
    def showAdjacencyMatrix(self):
        print(self.__adjacency_matrix())