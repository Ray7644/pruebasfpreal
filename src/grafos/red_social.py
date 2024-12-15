from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional
from datetime import date, datetime
from grafos.recorridos import bfs, dfs
from grafos.grafo import Grafo

@dataclass
class Usuario:
    def __init__(self, dni: str, nombre: str, apellidos: str, fecha_nacimiento: date):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento

    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> 'Usuario':
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellidos} (DNI: {self.dni})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Usuario):
            return self.dni == other.dni
        return False

    def __hash__(self) -> int:
        return hash(self.dni)

@dataclass
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    __n: int = 0  # Contador de relaciones. Servirá para asignar identificadores únicos a las relaciones.

    @staticmethod
    def of(interacciones: int, dias_activa: int) -> 'Relacion':
        Relacion.__n += 1
        return Relacion(Relacion.__n, interacciones, dias_activa)

    def __str__(self) -> str:
        return f"Relación {self.id}: {self.interacciones} interacciones, activa por {self.dias_activa} días"

class Red_social(Grafo[Usuario, Relacion]):
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        self.usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> 'Red_social':
        return Red_social(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> 'Red_social':
        """
        Crea una Red Social a partir de dos archivos:
        - `f1` contiene usuarios: DNI, nombre, apellidos, fecha de nacimiento.
        - `f2` contiene relaciones: DNI origen, DNI destino, interacciones, días activa.

        :param f1: Archivo de usuarios (CSV).
        :param f2: Archivo de relaciones (CSV).
        :param es_dirigido: Si la red es dirigida.
        :return: Instancia de Red_social.
        """
        red_social = Red_social.of(es_dirigido)

        with open('../../resources/usuarios.txt', 'r', encoding='utf-8') as archivo_usuarios:
            for linea in archivo_usuarios:
                dni, nombre, apellidos, fecha_str = linea.strip().split(',')
                fecha_nacimiento = date.fromisoformat(fecha_str)
                usuario = Usuario.of(dni, nombre, apellidos, fecha_nacimiento)
                red_social.add_vertex(usuario)
                red_social.usuarios_dni[dni] = usuario

        with open('../../resources/relaciones.txt', 'r', encoding='utf-8') as archivo_relaciones:
            for linea in archivo_relaciones:
                dni_origen, dni_destino, interacciones, dias_activa = linea.strip().split(',')
                interacciones = int(interacciones)
                dias_activa = int(dias_activa)

                if dni_origen in red_social.usuarios_dni and dni_destino in red_social.usuarios_dni:
                    origen = red_social.usuarios_dni[dni_origen]
                    destino = red_social.usuarios_dni[dni_destino]
                    relacion = Relacion.of(interacciones, dias_activa)
                    red_social.add_edge(origen, destino, relacion)

        return red_social
    
if __name__ == '__main__':
    raiz = '../../'
    rrss = Red_social.parse(raiz+'resources/usuarios.txt', raiz+'resources/relaciones.txt', es_dirigido=False)
    

    print("El camino más corto desde 25143909I hasta 87345530M es:")
    camino = dfs(rrss, rrss.usuarios_dni['25143909I'], rrss.usuarios_dni['87345530M'])
    g_camino = rrss.subgraph(camino)
    
    g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.dni}", lambda_arista=lambda e: e.id)
        
