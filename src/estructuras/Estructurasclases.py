from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod

# Tipos genéricos
E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')

class Agregado_lineal(ABC, Generic[E]):
    """
    Clase base para los objetos agregados lineales.
    """

    def __init__(self):
        # Inicializa una lista vacía para almacenar elementos
        self._elements: List[E] = []

    def size(self) -> int:
        """
        Devuelve el número de elementos en la colección.
        :return: Int
        """
        return len(self._elements)

    def is_empty(self) -> bool:
        """
        Verifica si la colección está vacía.
        :return: Boolean
        """
        return self.size() == 0

    def elements(self) -> List[E]:
        """
        Devuelve una copia de la lista de elementos.
        :return: List
        """
        return self._elements.copy()
    
    @abstractmethod
    def add(self, e: E) -> None:
        """
        Agrega un elemento a la colección.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
        raise NotImplementedError("Método abstracto: debe ser implementado en la subclase.")

    def add_all(self, ls: List[E]) -> None:
        """
        Agrega todos los elementos de una lista a la colección.
        :param ls: Lista a agregar
        :raise NotImplementedError: Método abstracto
        """
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        """
        Remove el primer elemento de la colección.
        :return: Elemento eliminado
        :raise IndexError: Si la colección está vacía
        """
        if self.is_empty():
            raise IndexError("No se puede eliminar de un agregado vacío.")
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        """
        Elimina todos los elementos de la colección.
        :return: Lista eliminada
        """
        removed_elements = self._elements.copy()
        self._elements.clear()
        return removed_elements



class Lista_ordenada(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        # Inicializa la colección con una función de ordenación
        super().__init__()
        self._order = order

    @classmethod
    def of(cls, order: Callable[[E], R]) -> 'Lista_ordenada[E, R]':
        """
        Crea una instancia de la clase lista ordenada.
        :param order: Función de ordenación
        :return: Instancia de Lista_ordenada
        """
        return cls(order)

    def __index_order(self, e: E) -> int:
        """
        Busca el índice correspondiente a un elemento en la colección.
        :param e: Elemento a buscar
        :return: int
        """
        for i, element in enumerate(self._elements):
            if self._order(e) < self._order(element):
                return i
        return len(self._elements)

    def add(self, e: E) -> None:
        """
        Inserta un elemento en el lugar correspondiente
        :param e: Elemento a agregar
        """
        index = self.__index_order(e)
        self._elements.insert(index, e)



class Lista_ordenada_sin_repeticion(Lista_ordenada[E, R], Generic[E, R]):
    def add(self, e: E) -> None:
        """
        Agrega un elemento a la colección sin repetición.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
        if e in self._elements:
            print(f"Método: add({e}) -> Estado actual de la lista: {self.elements()}\n")
            return
        
        index = self._index_order(e)
        self._elements.insert(index, e)
        print(f"Método: add({e}) -> Estado actual de la lista: {self.elements()}\n")
        
    def _index_order(self, e: E) -> int:
        """
        Encuentra el índice donde el elemento debe insertarse, en orden de mayor a menor.
        :param e: Elemento a insertar
        :return: int
        """
        for i, element in enumerate(self._elements):
            if self._order(e) > self._order(element):  
                return i
        return len(self._elements)



class Cola(Agregado_lineal[E]):
    @classmethod
    def of(cls) -> 'Cola[E]':
        """
        Crea una instancia vacía de Cola.
        """
        return cls()

    def add(self, e: E) -> None:
        """
        Agrega un elemento a la cola al final.
        :param e: Elemento a agregar
        """
        self._elements.append(e)
        print(f"Método: add({e}) -> Estado actual de la cola: {self.elements()}\n")

    def remove_all(self) -> List[E]:
        """
        Elimina todos los elementos de la cola en el orden en que fueron añadidos.
        :return: Lista de elementos eliminados
        """
        removed_elements = self._elements.copy()  # Mantener el orden FIFO
        self._elements.clear()
        print(f"Método: remove_all() -> Elementos eliminados: {removed_elements}\n")
        return removed_elements
    
        



class Cola_prioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[Tuple[E, P]] = []
        

    def size(self) -> int:
        """
        Devuelve el número de elementos en la cola.
        :return: Int
        """
        return len(self._elements)


    def is_empty(self) -> bool:
        """
        Verifica si la cola está vacía.
        :return: Boolean
        """
        return self.size() == 0

    def elements(self) -> List[E]:
        """
        Devuelve una copia de la lista de elementos de mayor a menor prioridad
        :return: List
        """
        return [e for e, _ in sorted(self._elements, key=lambda x: x[1], reverse=True)]


    def add(self, e: E, priority: P) -> None:
        """
        Agrega un elemento y sus prioridades a la cola.
        :param e: Elemento a agregar
        :param priority: Prioridad del elemento
        """
        self._elements.append((e, priority))
        self._elements.sort(key=lambda x: x[1], reverse=True)
        print(f"Método: add({e}, {priority}) -> Estado actual de la cola: {self.elements()}\n")

    def remove(self) -> E:
        """
        Elimina el primer elemento de la cola. El primer elemento es el de mayor prioridad.
        :return: Elemento eliminado
        :raise IndexError: Si la cola está vacía
        """
        if self.is_empty():
            raise IndexError("No se puede eliminar de una cola de prioridad vacía.")
        removed_element = self._elements.pop(0)[0]
        print(f"Método: remove() -> Paciente atendido: {removed_element}\n")
        return removed_element

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        """
        Agrega todos los elementos y sus prioridades a la cola.
        :param ls: Lista de tuplas (elemento, prioridad)
        """
        for e, priority in ls:
            self.add(e, priority)

    def decrease_priority(self, e: E, new_priority: P) -> None:
        """
        Reduce la prioridad del elemento en la cola. El elemento debe estar en la cola, y la nueva prioridad debe ser menor
        :param e: Elemento a reducir prioridad.
        :param new_priority: Prioridad nueva para el elemento
        """
        for i, (element, priority) in enumerate(self._elements):
            if element == e:
                if new_priority >= priority:
                    print("NOTA: Debes probar a usar decrease_priority() con un valor mayor a la prioridad actual de 'Paciente B'.\n")
                    return
                self._elements[i] = (e, new_priority)
                self._elements.sort(key=lambda x: x[1], reverse=True)
                print(f"Método: decrease_priority({e}, {new_priority}) -> Estado actual de la cola: {self.elements()}\n")
                return
        print(f"Elemento {e} no encontrado en la cola.")




class Pila(Agregado_lineal[E]):
    """
    Una Pila es una estructura de datos que sigue el principio LIFO (Last In, First Out).
    Los elementos se apilan y solo se puede acceder al elemento en la parte superior.
    
    IMPORTANTE. Como la estructura subyacente es una lista, la parte superior de la pila es el primer 
    elemento de la lista.
    """
    def add(self, e: E) -> None:
        """
        Agrega un elemento a la pila (LIFO).
        :param e: Elemento a agregar.
        """
        self._elements.insert(0, e)  # Insertar al inicio simula LIFO
        print(f"Método: add({e}) -> Estado actual de la pila: {self.elements()}\n")

    def remove(self) -> E:
        """
        Elimina el último elemento agregado (LIFO).
        :return: Elemento eliminado.
        :raise IndexError: Si la pila está vacía.
        """
        if self.is_empty():
            raise IndexError("No se puede eliminar de una pila vacía.")
        removed_element = self._elements.pop(0)
        print(f"Método: remove() -> Elemento eliminado: {removed_element}\n")
        return removed_element