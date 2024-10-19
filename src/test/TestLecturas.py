'''
Created on 17 oct 2024

@author: juan
'''

from lecturas.lecturas import contar_palabras, buscar_lineas, encontrar_palabras_unicas, longitud_promedio_lineas


def test1():
    fichero = '../../resources/lin_quijote.txt'
    separador = " "
    palabra = 'Quijote'
    numero_de_ocurrencias = contar_palabras(fichero, separador, palabra)
    print(f"El número de veces que aparece la palabra Quijote en el fichero {fichero} es: {numero_de_ocurrencias}")

def test2():
    fichero = '../../resources/lin_quijote.txt'
    cad = 'Quijote'
    resultado = buscar_lineas(fichero, cad)
    print(f'Las líneas en las que aparece la palabra Quijote son: {resultado}')

def test3():
    fichero = '../../resources/archivo_palabras.txt'
    palabras_unicas = encontrar_palabras_unicas(fichero)
    print(f'Las palabras únicas en el fichero {fichero} son: {palabras_unicas}')
    
def test4():
    fichero = '../../resources/palabras_random.csv'
    fichero2 = '../../resources/vacio.csv'
    promedio = longitud_promedio_lineas(fichero)
    promedio2 = longitud_promedio_lineas(fichero2)
    print(f'La longitud promedio de las líneas del fichero {fichero} es: {promedio}')
    print(f'La longitud promedio de las líneas del fichero {fichero2} es: {promedio2}')
    
if __name__ == '__main__':
    test4()