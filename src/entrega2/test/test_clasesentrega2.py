'''
Created on 31 oct 2024

@author: juana
'''
from estructuras.Estructurasclases import Agregado_lineal, Cola, Cola_prioridad, Lista_ordenada, Lista_ordenada_sin_repeticion, Pila 

def test_lista_ordenada():
    print("TEST DE LISTA ORDENADA\n")
    print("------------------------------------------------")
    print("\nObjetivo: La Lista Ordenada mantiene los elementos en un orden específico, definido por un criterio.")
    print("En este caso, se ordena de menor a mayor.\n")
    print("------------------------------------------------\n")

    lista = Lista_ordenada.of(lambda x: x)
    elementos_a_agregar = [3, 1, 3, 2]
    print(f"Elementos a agregar: {elementos_a_agregar}\n")

    for e in elementos_a_agregar:
        lista.add(e)
        print(f"Método: add({e}) -> Estado actual de la lista: {lista.elements()}\n")

    print(f"\nResultado de la lista: {lista.elements()}\n")
    print("\nMétodo: elements() -> La lista está ordenada correctamente.\n")

    eliminado = lista.remove()
    print(f"Método: remove() -> Elemento eliminado: {eliminado}\n")

    eliminados = lista.remove_all()
    print(f"Método: remove_all() -> Elementos eliminados: {eliminados}\n")

    lista.add(0)
    print(f"Método: add(0) -> Estado actual: {lista.elements()}\n")
    lista.add(10)
    print(f"Método: add(10) -> Estado actual: {lista.elements()}\n")
    lista.add(7)
    print(f"Método: add(7) -> Estado actual: {lista.elements()}\n")

    print(f"Método: size() -> Tamaño de la lista es el esperado.\n")
    
    print("------------------------------------------------")

def test_lista_ordenada_sin_repeticion():
    print("------------------------------------------------\n")
    print("TEST DE LISTA ORDENADA SIN REPETICIÓN\n")
    print("------------------------------------------------\n")
    print("\nObjetivo: La Lista Ordenada Sin Repetición mantiene los elementos en orden sin permitir duplicados.")
    print("En este caso, se ordena de mayor a menor.\n")
    print("------------------------------------------------\n")

    lista = Lista_ordenada_sin_repeticion.of(lambda x: x)
    elementos_a_agregar = [23, 47, 47, 1, 2, -3, 4, 5]
    print(f"Elementos a agregar: {elementos_a_agregar}\n")

    for e in elementos_a_agregar:
        lista.add(e)

    eliminado = lista.remove()
    print(f"\nMétodo: remove() -> Elemento eliminado: {eliminado}\n")

    eliminados = lista.remove_all()
    print(f"Método: remove_all() -> Elementos eliminados: {eliminados}\n")

    lista.add(0)
    print(f"Método: add(0) -> Estado actual: {lista.elements()}\n")
    lista.add(7)
    print(f"Método: add(7) -> Estado actual: {lista.elements()}\n")
    print("------------------------------------------------")

def test_cola():
    print("------------------------------------------------")
    print("TEST DE COLA\n")
    print("------------------------------------------------")
    print("\nObjetivo: La Cola funciona bajo el principio de primero en entrar, primero en salir (FIFO).\n")
    print("------------------------------------------------\n")

    cola = Cola.of()
    elementos_a_agregar = [23, 47, 1, 2, -3, 4, 5]
    print(f"Elementos a agregar: {elementos_a_agregar}\n")

    for e in elementos_a_agregar:
        cola.add(e)

    cola.remove_all()
    print("------------------------------------------------")
    
def test_cola_prioridad():
    print("------------------------------------------------\n")
    print("TEST DE COLA DE PRIORIDAD\n")
    print("------------------------------------------------")
    print("\nObjetivo: La Cola de Prioridad permite atender elementos con mayor prioridad antes que otros.\n")
    print("------------------------------------------------\n")

    cola_prioridad = Cola_prioridad[str, int]()
    pacientes = [('Paciente A', 3), ('Paciente C', 1), ('Paciente B', 2)]
    print(f"Pacientes a agregar: {pacientes}\n")

    for paciente, prioridad in pacientes:
        cola_prioridad.add(paciente, prioridad)

    cola_prioridad.decrease_priority('Paciente B', 0)

    cola_prioridad.decrease_priority('Paciente B', 3)

    cola_prioridad.remove()
    cola_prioridad.remove()
    cola_prioridad.remove()
    print("------------------------------------------------")
    
def test_pila():
    print("------------------------------------------------")
    print("TEST DE PILA\n")
    print("------------------------------------------------")
    print("\nObjetivo: La Pila sigue el principio de último en entrar, primero en salir (LIFO).\n")
    print("------------------------------------------------\n")

    pila = Pila[int]()
    elementos = [1, 2, 3]
    print(f"Elementos a agregar: {elementos}\n")

    for elemento in elementos:
        pila.add(elemento)

    pila.remove()

    removed_elements = pila.remove_all()
    print(f"Método: remove_all() -> Elementos eliminados: {removed_elements}\n")
    print("------------------------------------------------")

if __name__ == '__main__':
    test_cola_prioridad()