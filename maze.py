import numpy as np
import random

class Maze:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.__makeMaze()

    def __makeMaze(self):
        # Valores iniciales para la posición de partida y posición final
        self.start = [random.randint(0, self.n-1), random.randint(0, self.m-1)]
        self.end = [random.randint(0, self.n-1), random.randint(0, self.m-1)]

        # En caso de que la posición de partida sea igual a la final,
        # buscamos un nuevo valor para la posición final
        while(self.start == self.end): self.end = [random.randint(0, self.n-1), random.randint(0, self.m-1)]

        # Posibles valores que pueden tomar las casillas
        possibles_boxes = ["-", ".", "ll", "a"]

        # Generando el tablero de tamaño nxm
        self.__maze = []
        for i in range(self.n):
            self.__maze.append([])
            for j in range(self.m):
                self.__maze[i].append(possibles_boxes[random.randint(0, len(possibles_boxes)-1)])
        
        # Asignando las posiciones de spirit y la meta en el tablero
        self.__maze[self.start[0]][self.start[1]] = "s"
        self.__maze[self.end[0]][self.end[1]] = "x"
    
    def findPath(self):
        queue = []
        visited = []
        queue.append(self.start)

        while(queue):
            print(queue)
            x, y = queue.pop(0)

            if(x == self.end[0] and y == self.end[1]):
                return True

            # hacia derecha
            if(y + 1 < self.m and [x, y + 1] not in queue and [x, y + 1] not in visited and self.__maze[x][y+1] != "-"):
                ny = y + 1
                queue.append([x, ny])
            #hacia abajo
            if(x + 1 < self.n and [x + 1, y] not in queue and [x + 1, y] not in visited and self.__maze[x + 1][y] != "-"):
                nx = x + 1
                queue.append([nx, y])
            #hacia izquierda
            if(y - 1 >= 0 and [x, y - 1] not in queue and [x, y - 1] not in visited and self.__maze[x][y - 1] != "-"):
                ny = y - 1
                queue.append([x, ny])
            #hacia arriba
            if(x - 1 >= 0 and [x - 1, y] not in queue and [x - 1, y] not in visited and self.__maze[x - 1][y] != "-"):
                nx = x - 1
                queue.append([nx, y])
            visited.append([x, y])
        return False

    def __adjacencyMatrix(self):
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

    def showMaze(self):
        print(np.array(self.__maze))

    def showAdjacencyMatrix(self):
        print(self.__adjacencyMatrix())