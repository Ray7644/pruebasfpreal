'''
Created on 21 nov 2024

@author: juana
'''
from typing import List, TypeVar, Generic, Callable, Optional
from abc import ABC, abstractmethod

E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')

class Agregado_lineal(ABC, Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    def size(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return self.size() == 0

    def elements(self) -> List[E]:
        return self._elements.copy()
    
    @abstractmethod
    def add(self, e: E) -> None:
        raise NotImplementedError("Método abstracto: debe ser implementado en la subclase.")

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        if self.is_empty():
            raise IndexError("No se puede eliminar de un agregado vacío.")
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = self._elements.copy()
        self._elements.clear()
        return removed_elements
    
    def contains(self, e: E) -> bool:
        return e in self._elements

    def find(self, func: Callable[[E], bool]) -> Optional[E]:
        for element in self._elements:
            if func(element):
                return element
        return None

    def filter(self, func: Callable[[E], bool]) -> List[E]:
        return [element for element in self._elements if func(element)]
    
class ColaConLimite(Agregado_lineal[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")
        self._capacidad = capacidad

    def add(self, e: E) -> None:
        if self.is_full():
            raise OverflowError("La cola está llena.")
        self._elements.append(e)

    def is_full(self) -> bool:
        return self.size() >= self._capacidad

    @classmethod
    def of(cls, capacidad: int) -> 'ColaConLimite':
        return cls(capacidad)
    
class ListaSimple(Agregado_lineal[int]):
    def add(self, e: int) -> None:
        self._elements.append(e)
        
lista = ListaSimple()
lista.add(1)
lista.add(2)
lista.add(3)
lista.add(4)
lista.add(5)

def testcontains():
    print("\nPruebas para contains:")
    print(lista.contains(2))  
    print(lista.contains(6))  

def testfind():
    print("\nPruebas para find:")
    print(lista.find(lambda x: x > 3))  
    print(lista.find(lambda x: x > 0))  
    print(lista.find(lambda x: x > 6))

def testfilter():
    print("\nPruebas para filter:")
    print(lista.filter(lambda x: x % 2 == 0))  
    print(lista.filter(lambda x: x > 2))
    print(lista.filter(lambda x: x < 0))
    
def testcolaconlimite():
    cola = ColaConLimite.of(3)
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")

    try:
        cola.add("Tarea 4")  
    except OverflowError as e:
        print(e)  

    print(cola.remove())
    
if __name__ == '__main__':
    testcolaconlimite()
    testcontains()
    testfind()
    testfilter()