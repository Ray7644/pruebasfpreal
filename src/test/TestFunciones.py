'''
Created on 3 oct 2024

@author: juana
'''
from funciones.funciones import productorio, secuencia_geo, combinatorio, newton, stirling, f, f_prime

def test1():
    a=int(4)
    b=int(2)
    resultado=productorio(a, b)
    print(f"El producto de {a} y {b} es {resultado}")
    
def test2():
    c=int(3)
    d=int(5)
    e=int(2)
    resultado2=secuencia_geo(c, d, e)
    print(f'El producto de la secuencia geométrica con a1 = {c}, r = {d} y k = {e} es: {resultado2}')
    
def test3():
    g=int(4)
    h=int(2)
    resultado3=combinatorio(g, h)
    print(f'El número combinatorio de {g} y {h} es: {resultado3}.0')
    
def test4():
    j=int(4)
    m=int(2)
    resultado4=stirling(j, m)
    print(f'El número S(n, k) siendo n = {j} y k = {m} es: {resultado4}')
    
def test5():
    y=int(3)
    z=float(0.001)
    resultado4=newton(f, f_prime, y, z, max_iter=1000)
    print(f'Resultado de la función 5 con a = {y} y e = {z}, f(x) = 2x^2 y f`(x) = 4x: {resultado4}')


if __name__ == '__main__':
    test1()
  