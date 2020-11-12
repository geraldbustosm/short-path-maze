import numpy as np
import random
from PIL import Image, ImageDraw, ImageFont
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
            for sq in queue:
                print('(' + str(sq.x) + ',' + str(sq.y) + ')', end=" - ")
            
            print("")

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
                    for squarePriority in squarePriorities:
                        queue.append(squarePriority)

                # Marcamos como visitado
                visited[square.x][square.y] = True

        return None
    
    def findPath(self):
        # Recorreremos el diccionario para saber de donde proviene la solución si es que existe
        movements = self.__findPath()
        path = []

        if(movements is not None):
            path.append(self.end)
            movement = movements[self.end]
            while(movement != self.start):
                path.append(movement)
                movement = movements[movement]
            path.append(self.start)
        return path

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
    
    def drawMaze(self):
        # Amplificator
        amplificator = 100

        # Tamaño de la grilla
        h = self.n * amplificator
        w = self.m * amplificator
        obstacleBorder = 95
        
        # Creando una imagen
        imgFile = Image.new("RGB", (w, h)) 
        img = ImageDraw.Draw(imgFile)

        # Obteniendo una fuente
        font = ImageFont.truetype("arial.ttf", 20)

        for i in range(self.n):
            for j in range(self.m):
                # Posición inicial del rectangulo
                a = i * amplificator
                b = j * amplificator

                # Posición final del rectangulo
                x = (i + 1) * amplificator
                y = (j + 1) * amplificator

                # Creando la forma del rectangulo con dos pares ordenados (w1, h1) y (w2, h2)
                shape = [(b, a), (y, x)]

                # Info del nodo
                text = '(' + str(self.__maze[i][j].x) + ', ' + str(self.__maze[i][j].y) + ', ' + str(self.__maze[i][j].cost) + ')'
                
                # Pintamos la casilla segun el costo
                if(self.__maze[i][j].cost == 0.5):
                    color = "#cc3c39"
                elif(self.__maze[i][j].cost == 1.2):
                    color = "#ffd799"
                elif(self.__maze[i][j].cost == 0):
                    color = "#798ec7"
                else:
                    color = "green"
                img.rectangle(shape, fill = color, outline ="#658085")
                img.text((b+5, a+40), text=text, font=font, fill = "black")

                # Pintamos bordes si tiene obstaculos
                color = "black"
                diff = (amplificator - obstacleBorder)/2

                if((self.__maze[i][j].rightObstacle and j+1 < self.m) or (j+1 < self.m and self.__maze[i][j+1].leftObstacle)):
                    shape = [(b+diff+obstacleBorder, a), (y+diff, x)]
                    img.rectangle(shape, fill = color)

                if((self.__maze[i][j].downObstacle and i+1 < self.n) or (i+1 < self.n and self.__maze[i+1][j].upObstacle)):
                    shape = [(b, a+diff+obstacleBorder), (y, x+diff)]
                    img.rectangle(shape, fill = color)

                if((self.__maze[i][j].leftObstacle and j-1 >= 0) or (j-1 >= 0 and self.__maze[i][j-1].rightObstacle)):
                    shape = [(b-diff, a), (y-diff-obstacleBorder, x)]
                    img.rectangle(shape, fill = color)

                if((self.__maze[i][j].upObstacle and i-1 >= 0) or (i-1 >= 0 and self.__maze[i-1][j].downObstacle)):
                    shape = [(b, a-diff), (y, x-diff-obstacleBorder)]
                    img.rectangle(shape, fill = color)
        imgFile.show() 