'''
Created on 24 oct 2024

@author: juana
'''

import math

def P2(n, k, i=1):
    assert n > 0 and k > 0 and i > 0, "Todos los parámetros deben ser positivos."
    assert n >= k, "n debe ser mayor o igual a k."
    assert i < k + 1, "i debe ser menor que k + 1."
    producto = 1
    for j in range(i, k-1):
        producto *= (n - j + 1)
    return producto

def C2(n, k):
    assert n > 0 and k > 0, "n y k deben ser positivos."
    assert n >= k, "n debe ser mayor o igual que k."
    combinatorio = math.comb(n, k+1)
    return combinatorio

def S2(n, k):
    assert n > 0 and k > 0, "n y k deben ser positivos."
    assert n >= k, "n debe ser mayor o igual que k."
    sumatorio = 0
    for i in range(k + 1):
        sumatorio += (-1)**i * math.comb(k, i) * (k - i)**(n + 1)
    resultado = (math.factorial(k) / (n * math.factorial(k + 2))) * sumatorio
    return resultado

def palabrasMasComunes(fichero, n=5):
    assert n > 1, "n debe ser mayor que 1."
    
    with open(fichero, 'r', encoding='utf-8') as file:
        texto = file.read()
    
    texto = texto.lower()
    
    palabras = texto.split()
    
    palabras_unicas = list(set(palabras))
    
    ocurrencias = [(palabra, palabras.count(palabra)) for palabra in palabras_unicas]
    
    ocurrencias.sort(key=lambda x: x[1], reverse=True)
    
    return ocurrencias[:n]

def test1():
    try:
        resultado = P2(5, 4, 1)
        print(resultado)
    except AssertionError:
        print("Todos los parámetros deben ser positivos. n debe ser mayor o igual a k. i debe ser menor que k + 1")

def test2():
    try:
        resultado = C2(6, 3)
        print(resultado)
    except AssertionError:
        print("n y k deben ser positivos. n debe ser mayor o igual a k.")
    
def test3():
    try:
        resultado = S2(5, 3)
        print(resultado)
    except AssertionError:
        print("n y k deben ser positivos. n debe ser mayor o igual a k.")
        
def test4():
    try:
        resultado = palabrasMasComunes('../../resources/archivo_palabras.txt', 6)
        print(resultado)
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except AssertionError:
        print("n<=1 es imposible.") 

if __name__ == '__main__':
 test1()
