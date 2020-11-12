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
                cost = self.__getRandomCost()
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
    
    def __findPath(self):
        queue = []
        visited = np.zeros((self.n, self.m), dtype=bool)
        movements = {}
        queue.append(self.start)

        while(queue):
            square = queue.pop(0)

            # Si la posición del nodo (square) es igual a la posición de la meta, lo encontramos
            if(square.x == self.end.x and square.y == self.end.y): return movements

            # Si el nodo no está en la cola realizamos los movimientos
            if(square not in queue):

                nextSquareRigth = None
                nextSquareDown = None
                nextSquareLeft = None
                nextSquareUp = None

                # Movimiento hacia la derecha
                if(square.y + 1 < self.m and visited[square.x][square.y+1] == False and square.rightObstacle == False and self.__maze[square.x][square.y+1].leftObstacle == False):   
                    nextSquareRigth = self.__maze[square.x][square.y+1]
                    # Esta linea permite almacenar en un diccionario de donde proviene el 
                    # siguiente casillero, es decir, proviene del casillero actual
                    # por ejemplo:
                    # (2, 2, 0.5): (1, 2, 1.2)
                    # El nodo con coordenadas 2,2 y costo 0.5 fue generado por el nodo 1,2 con costo 1.2
                    movements[nextSquareRigth] = square
                
                # Movimiento hacia abajo
                if(square.x + 1 < self.n and visited[square.x+1][square.y] == False and square.downObstacle == False and self.__maze[square.x+1][square.y].upObstacle == False):
                    nextSquareDown = self.__maze[square.x+1][square.y]
                    movements[nextSquareDown] = square
                
                # Movimiento hacia la izquierda
                if(square.y - 1 >= 0 and visited[square.x][square.y - 1] == False and square.leftObstacle == False and self.__maze[square.x][square.y-1].rightObstacle == False):
                    nextSquareLeft = self.__maze[square.x][square.y-1]
                    movements[nextSquareLeft] = square
                
                # Movimiento hacia arriba
                if(square.x - 1 >= 0 and visited[square.x - 1][square.y] == False and square.upObstacle == False and self.__maze[square.x-1][square.y].downObstacle == False):   
                    nextSquareUp = self.__maze[square.x-1][square.y]
                    movements[nextSquareUp] = square
                
                # Ordenamos los casilleros a inspeccionar priorizando en la cola aquel
                # que tenga un menor costo temporal, por lo tanto los ordenaremos de menor a mayor

                squarePriorities = self.__compareCost(nextSquareRigth, nextSquareDown, nextSquareLeft, nextSquareUp)

                # Agregamos a la cola los casilleros con menor costo primero
                if squarePriorities is not None:
                    for square in squarePriorities:
                        queue.append(square)

                # Marcamos como visitado
                visited[square.x][square.y] = True

        return None
    
    def findPath(self):
        # Recorreremos el diccionario para saber de donde proviene la solución si es que existe
        path = self.__findPath()
        

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
    
    def __getRandomCost(self):
        option = bool(random.getrandbits(1))
        return 0.5 if option else 1.2
    
    def __compareCost(self, squareRight, squareDown, squareLeft, squareUp):
        squares = []

        if(squareRight is not None): squares.append(squareRight)
        if(squareDown is not None): squares.append(squareDown)
        if(squareLeft is not None): squares.append(squareLeft)
        if(squareUp is not None): squares.append(squareUp)

        return sorted(squares, key=lambda square: square.cost)