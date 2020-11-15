# El camino más corto posible utilizando BFS

Implementación de busqueda en anchura (breadth first search) para escoger el camino más corto posible en una grilla.

La idea es priorizar en la cola aquel casillero con menor costo.

Este problema en particular, sus casillas no son costos temporales, sino que corresponde a la rapidez con la que se puede avanzar si pasamos por dicha casilla. Por lo tanto, aquel casillero que tenga una mayor rapidez ira en la cola primero.

Cabe destacar que avanzar siempre por el casillero más rapido no siempre promete el mejor camino. Para escoger la mejor es recomendable utilizar otros algoritmos como Dijkstra.

A continuación visualizamos lo que genera el programa al generar un tablero de 6x5 aleatorio.
![Tablero de 6x5](https://i.imgur.com/o3pjU21.png)
