'''
Created on 21 nov 2024

@author: damat

-------------
Pseudocódigo:
-------------

función bfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una cola vacía
    agregar inicio a la cola
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la cola no esté vacía:
        tomar el elemento que está al frente de la cola y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo:
                si vecino no está en visitados:
                    agregar vecino a la cola
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)

-------------------------------------------------------------
función dfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una pila vacía
    agregar inicio a la pila
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la pila no esté vacía:
        tomar el elemento más reciente agregado a la pila y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo, en orden inverso:
                si vecino no está en visitados:
                    agregar vecino a la pila
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)
-------------------------------------------------------------------------

función reconstruir_camino(predecesores, destino):
    crear una lista vacía llamada camino
    establecer vértice_actual como destino

    mientras vértice_actual no sea nulo:
        agregar vértice_actual al inicio de la lista camino
        cambiar vértice_actual al predecesor de dicho vértice_actual usando el diccionario predecesores

    devolver camino

'''
from typing import TypeVar, List, Set, Optional, Dict

from grafos.grafo import Grafo 
from estructuras.Estructurasclases import Cola, Pila

# Importa la clase Grafo desde su módulo

V = TypeVar('V')  # Tipo de los vértices
E = TypeVar('E')  # Tipo de las aristas

def bfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    cola = Cola[V].of()
    visitados = set()
    predecesores: Dict[V, Optional[V]] = {inicio: None}

    cola.add(inicio)
    visitados.add(inicio)

    while not cola.is_empty():
        actual = cola.remove()
        if actual == destino:
            return reconstruir_camino(predecesores, destino)

        for sucesor in sorted(grafo.successors(actual)):
            if sucesor not in visitados:
                visitados.add(sucesor)
                predecesores[sucesor] = actual
                cola.add(sucesor)

    return []  

def dfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    pila = Pila[V]()
    visitados = set()
    predecesores: Dict[V, Optional[V]] = {inicio: None}

    pila.add(inicio)

    while not pila.is_empty():
        actual = pila.remove()
        if actual == destino:
            return reconstruir_camino(predecesores, destino)

        if actual not in visitados:
            visitados.add(actual)
            for sucesor in grafo.successors(actual):
                if sucesor not in visitados:
                    predecesores[sucesor] = actual
                    pila.add(sucesor)

    return []  

def reconstruir_camino(predecesores: Dict[V, Optional[V]], destino: V) -> List[V]:
    camino = []
    actual = destino

    while actual is not None:
        camino.append(actual)
        actual = predecesores.get(actual)

    camino.reverse()
    return camino

def grafo_de_prueba() -> Grafo[str, int]:
    grafo = Grafo.of(es_dirigido=False)
    grafo.add_vertex("A")
    grafo.add_vertex("B")
    grafo.add_vertex("C")
    grafo.add_vertex("D")
    grafo.add_vertex("E")
    grafo.add_edge("A", "B", 1)
    grafo.add_edge("A", "C", 1)
    grafo.add_edge("B", "D", 1)
    grafo.add_edge("C", "D", 1)
    grafo.add_edge("D", "E", 1)
    return grafo

def test_bfs():
    print("Prueba BFS")
    grafo = grafo_de_prueba()
    camino = bfs(grafo, "A", "E")
    assert camino == ["A", "B", "D", "E"], f"Se esperaba ['A', 'B', 'D', 'E'], pero se obtuvo {camino}"
    print(f"Camino encontrado: {camino}")
    
def test_dfs():
    print("Prueba DFS")
    grafo = grafo_de_prueba()
    camino = dfs(grafo, "A", "E")
    assert camino in [["A", "B", "D", "E"], ["A", "C", "D", "E"]], f"Resultado inesperado: {camino}"
    print(f"Camino encontrado: {camino}")
    
def test_sin_camino():
    print("Prueba sin camino")
    grafo = grafo_de_prueba()
    grafo.add_vertex("F")  
    camino = bfs(grafo, "A", "F")
    assert camino == [], f"Se esperaba [], pero se obtuvo {camino}"
    print(f"Camino encontrado: {camino}")
    
if __name__ == "__main__":
    test_bfs()
    test_dfs()
    test_sin_camino()
