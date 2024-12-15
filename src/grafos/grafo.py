'''
Created on 21 nov 2024

@author: damat
'''
from __future__ import annotations

from typing import TypeVar, Generic, Dict, Set, Optional, Callable
import matplotlib.pyplot as plt
import networkx as nx

# Definición de tipos genéricos
V = TypeVar('V')  # Tipo para vértices
E = TypeVar('E')  # Tipo para aristas

class Grafo(Generic[V, E]):
    def __init__(self, es_dirigido: bool = True):
        self.es_dirigido: bool = es_dirigido
        self.adyacencias: Dict[V, Dict[V, E]] = {}

    @staticmethod
    def of(es_dirigido: bool = True) -> "Grafo[V, E]":
        return Grafo(es_dirigido)

    def add_vertex(self, vertice: V) -> None:
        if vertice not in self.adyacencias:
            self.adyacencias[vertice] = {}

    def add_edge(self, origen: V, destino: V, arista: E) -> None:
        self.add_vertex(origen)
        self.add_vertex(destino)
        self.adyacencias[origen][destino] = arista
        if not self.es_dirigido:
            self.adyacencias[destino][origen] = arista

    def successors(self, vertice: V) -> Set[V]:
        return set(self.adyacencias.get(vertice, {}).keys())

    def predecessors(self, vertice: V) -> Set[V]:
        if not self.es_dirigido:
            return self.successors(vertice)
        return {v for v, adyacentes in self.adyacencias.items() if vertice in adyacentes}

    def edge_weight(self, origen: V, destino: V) -> Optional[E]:
        return self.adyacencias.get(origen, {}).get(destino)

    def vertices(self) -> Set[V]:
        return set(self.adyacencias.keys())

    def edge_exists(self, origen: V, destino: V) -> bool:
        return destino in self.adyacencias.get(origen, {})

    def subgraph(self, vertices: Set[V]) -> "Grafo[V, E]":
        subgrafo = Grafo(self.es_dirigido)
        for v in vertices:
            if v in self.adyacencias:
                subgrafo.add_vertex(v)
                for destino, arista in self.adyacencias[v].items():
                    if destino in vertices:
                        subgrafo.add_edge(v, destino, arista)
        return subgrafo

    def inverse_graph(self) -> "Grafo[V, E]":
        if not self.es_dirigido:
            raise ValueError("El grafo no es dirigido, no tiene grafo inverso.")
        
        inverso = Grafo(self.es_dirigido)
        for origen, destinos in self.adyacencias.items():
            for destino, arista in destinos.items():
                inverso.add_edge(destino, origen, arista)
        return inverso

    def draw(self, titulo: str = "Grafo", 
             lambda_vertice: Callable[[V], str] = str, 
             lambda_arista: Callable[[E], str] = str) -> None:
        g_nx = nx.DiGraph() if self.es_dirigido else nx.Graph()
        for origen, destinos in self.adyacencias.items():
            for destino, arista in destinos.items():
                g_nx.add_edge(lambda_vertice(origen), lambda_vertice(destino), label=lambda_arista(arista))

        pos = nx.spring_layout(g_nx)
        nx.draw(g_nx, pos, with_labels=True, node_size=700, node_color="skyblue", font_weight="bold", font_size=10)
        labels = nx.get_edge_attributes(g_nx, "label")
        nx.draw_networkx_edge_labels(g_nx, pos, edge_labels=labels)
        plt.title(titulo)
        plt.show()
        G = nx.DiGraph() if self.es_dirigido else nx.Graph()
    
        for vertice in self.vertices():
            G.add_node(vertice, label=lambda_vertice(vertice))  
        for origen in self.vertices():
            for destino, arista in self.adyacencias[origen].items():
                G.add_edge(origen, destino, label=lambda_arista(arista))  
    
        pos = nx.spring_layout(G)  
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=500, 
                labels=nx.get_node_attributes(G, 'label'))  
    
        edge_labels = nx.get_edge_attributes(G, "label")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
        plt.title(titulo)
        plt.show()

        
    def __str__(self) -> str:
        resultado = []
        for vertice, vecinos in self.adyacencias.items():
            if vecinos:  # Si el vértice tiene vecinos
                aristas = ", ".join(f"{destino} ({peso})" for destino, peso in vecinos.items())
            resultado.append(f"{vertice} -> {aristas}")
        else:  # Si el vértice no tiene vecinos
            resultado.append(f"{vertice} ->")
        return "\n".join(resultado)
            
if __name__ == '__main__':
    grafo = Grafo.of(es_dirigido=True)
    grafo.add_vertex("A")
    grafo.add_vertex("B")
    grafo.add_vertex("C")
    grafo.add_edge("A", "B", 5)
    grafo.add_edge("B", "C", 3)
    grafo.draw(titulo="Mi Grafo Dirigido")
    grafo.inverse_graph().draw(titulo="Inverso del Grafo Dirigido")
    print(grafo)
