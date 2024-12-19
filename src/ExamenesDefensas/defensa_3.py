'''
Created on 19 dic 2024

@author: juana
'''
from typing import NamedTuple, Dict, Optional
from grafos.grafo import Grafo
import matplotlib.pyplot as plt

class Gen:
    def __init__(self, nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str):
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser mayor o igual a cero.")

        self._nombre = nombre
        self._tipo = tipo
        self._num_mutaciones = num_mutaciones
        self._loc_cromosoma = loc_cromosoma

    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo(self):
        return self._tipo

    @property
    def num_mutaciones(self):
        return self._num_mutaciones

    @property
    def loc_cromosoma(self):
        return self._loc_cromosoma

    @classmethod
    def of(cls, nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str):
        return cls(nombre, tipo, num_mutaciones, loc_cromosoma)

    @classmethod
    def parse(cls, data: str):
        try:
            nombre, tipo, num_mutaciones, loc_cromosoma = data.strip().split(",")
            return cls.of(nombre, tipo, int(num_mutaciones), loc_cromosoma)
        except ValueError as e:
            raise ValueError("Formato de entrada inválido. Debe ser 'nombre,tipo,num_mutaciones,loc_cromosoma'") from e

    @classmethod
    def from_file(cls, file_path: str):
        genes = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    genes.append(cls.parse(line))
                except ValueError as e:
                    print(f"Línea ignorada por formato incorrecto: {line.strip()} ({e})")
        return genes

    def __repr__(self):
        return (
            f"Gen(nombre={self.nombre}, tipo={self.tipo}, num_mutaciones={self.num_mutaciones}, "
            f"loc_cromosoma={self.loc_cromosoma})"
        )

class RelacionGenAGen(NamedTuple):
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @property
    def coexpresados(self) -> bool:
        return self.conexion > 0.75

    @property
    def antiexpresados(self) -> bool:
        return self.conexion < 0.75

    @classmethod
    def of(cls, nombre_gen1: str, nombre_gen2: str, conexion: float):
        if not isinstance(nombre_gen1, str) or not isinstance(nombre_gen2, str):
            raise ValueError("Los nombres de los genes deben ser cadenas de texto.")
        if not (-1 <= conexion <= 1):
            raise ValueError("La conexión debe ser un número real entre -1 y 1, inclusive.")
        return cls(nombre_gen1, nombre_gen2, conexion)

    @classmethod
    def parse(cls, linea: str):
        partes = linea.strip().split(',')
        if len(partes) != 3:
            raise ValueError("La línea debe tener exactamente 3 partes separadas por comas: nombre_gen1, nombre_gen2 y conexion.")
        nombre_gen1, nombre_gen2, conexion_str = partes
        try:
            conexion = float(conexion_str)
        except ValueError:
            raise ValueError("El tercer elemento debe ser un número real válido.")
        return cls.of(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def leer_fichero(ruta_fichero: str):
        relaciones = []
        with open(ruta_fichero, 'r') as fichero:
            for linea in fichero:
                try:
                    relaciones.append(RelacionGenAGen.parse(linea))
                except ValueError as e:
                    print(f"Error al procesar la línea: {linea.strip()} -> {e}")
        return relaciones
    
    
class RedGenica(Grafo[Gen, RelacionGenAGen]):
    """
    Representa una red génica basada en Grafo.
    """

    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        self.genes_por_nombre: Dict[str, Gen] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> "RedGenica":
        """
        Método de factoría para crear una nueva Red Génica.

        :param es_dirigido: Indica si la red génica es dirigida (True) o no dirigida (False).
        :return: Nueva red génica.
        """
        return RedGenica(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> "RedGenica":
        """
        Método de factoría para crear una Red Génica desde archivos de genes y relaciones.

        :param f1: Archivo de genes.
        :param f2: Archivo de relaciones entre genes.
        :param es_dirigido: Indica si la red génica es dirigida (True) o no dirigida (False).
        :return: Nueva red génica.
        """
        # Primero, crear la red génica que se va a devolver
        red_genica = RedGenica(es_dirigido)

        # Segundo, leer y agregar genes
        genes = Gen.from_file(f1)
        for gen in genes:
            red_genica.add_vertex(gen)
            red_genica.genes_por_nombre[gen.nombre] = gen

        # Por último, leer y agregar relaciones entre genes
        relaciones = RelacionGenAGen.leer_fichero(f2)
        for relacion in relaciones:
            gen1 = red_genica.genes_por_nombre.get(relacion.nombre_gen1)
            gen2 = red_genica.genes_por_nombre.get(relacion.nombre_gen2)
            if gen1 and gen2:
                red_genica.add_edge(gen1, gen2, relacion)

        return red_genica
    

if __name__ == "__main__":
    gen_str = "BRA1,oncogen,3,17q21.9"
    gen = Gen.parse(gen_str)
    print(gen)

    try:
        gen_str_err = "BRCA1,oncogen,-3,17q21"
        gen_err = Gen.parse(gen_str_err)
    except ValueError as e:
        print(e)

    file_path = "../../resources/genes.txt"
    try:
        genes = Gen.from_file(file_path)
        print("Genes leídos del archivo:")
        for g in genes:
            print(g)
    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado.")
        
    ruta = "../../resources/red_genes.txt"
    relaciones = RelacionGenAGen.leer_fichero(ruta)
    for relacion in relaciones:
        print("--------------------------------\n")
        print(relacion)
        print(f"Coexpresados: {relacion.coexpresados}")
        print(f"Antiexpresados: {relacion.antiexpresados}")