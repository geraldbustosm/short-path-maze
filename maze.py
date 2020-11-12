import numpy as np
import random
from square import Square

class Maze:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.__makeMaze()

    def __makeMaze(self):
        
        # Generando el tablero de tamaño nxm
        self.__maze = []
        for i in range(self.n):
            self.__maze.append([])
            for j in range(self.m):
                cost = self._getRandomCost()
                leftObstacle = bool(random.getrandbits(1))
                rightObstacle = bool(random.getrandbits(1))
                upObstacle = bool(random.getrandbits(1))
                downObstacle = bool(random.getrandbits(1))
                randomSquare = Square(i, j, cost, leftObstacle, rightObstacle, upObstacle, downObstacle)
                self.__maze[i].append(randomSquare)
        
        # Creamos el casillero de inicio y de fin
        self.start = Square(random.randint(0, self.n-1), random.randint(0, self.m-1), 0, False, False, False, False)
        self.end = Square(random.randint(0, self.n-1), random.randint(0, self.m-1), -1, False, False, False, False)

        # En caso de que la posición de partida sea igual a la final,
        # buscamos un nuevo valor para la posición final
        while(self.start.x == self.end.x and self.start.y == self.end.y):
            self.end.x = random.randint(0, self.n-1)
            self.end.y = random.randint(0, self.m-1)

        # Asignando las posiciones de spirit y la meta en el tablero
        self.__maze[self.start.x][self.start.y] = self.start
        self.__maze[self.end.x][self.end.y] = self.end
    
    def findPath(self):
        queue = []
        visited = np.zeros((self.n, self.m), dtype=bool)
        path = []
        queue.append(self.start)

        while(queue):
            print(queue)
            square = queue.pop(0)

            # Si la posición del nodo (square) es igual a la posición de la meta, lo encontramos
            if(square.x == self.end.x and square.y == self.end.y): return True

            # Si el nodo no está en la cola realizamos los movimientos
            if(square not in queue):

                # Movimiento hacia la derecha
                if(square.y + 1 < self.m and visited[square.x][square.y+1] == False and square.rightObstacle == False and self.__maze[square.x][square.y+1].leftObstacle == False):   
                    nextSquare = self.__maze[square.x][square.y+1]
                    queue.append(nextSquare)
                    # path
                
                # Movimiento hacia abajo
                if(square.x + 1 < self.n and visited[square.x+1][square.y] == False and square.downObstacle == False and self.__maze[square.x+1][square.y].upObstacle == False):
                    nextSquare = self.__maze[square.x+1][square.y]
                    queue.append(nextSquare)
                
                # Movimiento hacia la izquierda
                if(square.y - 1 >= 0 and visited[square.x][square.y - 1] == False and square.leftObstacle == False and self.__maze[square.x][square.y-1].rightObstacle == False):
                    nextSquare = self.__maze[square.x][square.y-1]
                    queue.append(nextSquare)
                
                # Movimiento hacia arriba
                if(square.x - 1 >= 0 and visited[square.x - 1][square.y] == False and square.upObstacle == False and self.__maze[square.x-1][square.y].downObstacle == False):   
                    nextSquare = self.__maze[square.x-1][square.y]
                    queue.append(nextSquare)
                
                # Marcamos como visitado
                visited[square.x][square.y] = True

        return False

    def showMaze2(self):
        for i in range(self.n):
            for j in range(self.m):
                if(self.__maze[i][j].cost == 0.5):
                    if(self.__maze[i][j].leftObstacle):
                        print('|', self.__maze[i][j].cost, ' ' , end='')
                    if(self.__maze[i][j].rightObstacle):
                        print(self.__maze[i][j].cost, '| ' , end='')
                    if(self.__maze[i][j].upObstacle):
                        print('0̅.̅5̅', ' ' , end='')
                    if(self.__maze[i][j].downObstacle):
                        print('0͟.͟5͟', ' ' , end='')
                elif(self.__maze[i][j].cost == 1.2):
                    if(self.__maze[i][j].leftObstacle):
                        print('|', self.__maze[i][j].cost, ' ' , end='')
                    if(self.__maze[i][j].rightObstacle):
                        print(self.__maze[i][j].cost, '| ' , end='')
                    if(self.__maze[i][j].upObstacle):
                        print('1̅.̅2̅', ' ' , end='')
                    if(self.__maze[i][j].downObstacle):
                        print('1͟.͟2͟', ' ' , end='')
                else:
                    print(self.__maze[i][j].cost, ' ' , end='')
                    
            print("")

    def showMaze(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.__maze[i][j].cost, ' ' , end='')
            print("")
    
    def _getRandomCost(self):
        option = bool(random.getrandbits(1))
        return 0.5 if option else 1.2
        