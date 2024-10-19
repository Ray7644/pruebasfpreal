from typing import Optional

def contar_palabras(ruta_archivo, sep, cad):
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            
            contenido = contenido.lower()
            
            separar = contenido.split(sep)
            
            palabras = separar.count(cad.lower())
        return palabras

def buscar_lineas(fichero, cad):
    
    lineas_encontradas = []
    
    cad = cad.lower()
    
    with open(fichero, 'r', encoding='utf-8') as file:
        
        for linea in file:
            
            if cad in linea.lower():
                
                lineas_encontradas.append(linea.strip())  
            
    return lineas_encontradas

def encontrar_palabras_unicas(fichero):
    with open(fichero, 'r', encoding='utf-8') as archivo:
        
        contenido = archivo.read()
        
        palabras_unicas = set(contenido.split())
        
        return list(palabras_unicas)
    
    
def longitud_promedio_lineas(file_path: str, sep: str = ',') -> Optional[float]:
    total_longitud = 0
    num_lineas = 0
    
    with open(file_path, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            longitud_linea = len(linea.strip().split(sep))
            total_longitud += longitud_linea
            num_lineas += 1
            
    if num_lineas > 0:
        return total_longitud / num_lineas
    else:
        return None