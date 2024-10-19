'''
Created on 3 oct 2024

@author: juana
'''

import math

def productorio(n:int, k:int)->int:
    res = 1
    for i in range(k + 1):
        res = (n - i + 1)*res
    return res

def secuencia_geo(a1, r, k):
    producto = (a1 ** k) * (r ** (k * (k - 1) // 2))
    return producto

def combinatorio(n, k):
    if k > n:
        return "Al ser k > n, no tiene sentido el combinatorio."
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def stirling(n, k):
    if k == 0 and n == 0:
        return 1  
    if k == 0 or n == 0:
        return 0  

    suma = 0
    for i in range(k):
        coef_binom = combinatorio(k + 1, i + 1)
        termino = (-1) ** i * coef_binom * (k - i) ** n
        suma += termino

    resultado = suma // math.factorial(k)
    return resultado

def newton(f, f_prime, x0, epsilon, max_iter=1000):

    x_n = x0
    for i in range(max_iter):
        f_x_n = f(x_n)
        if abs(f_x_n) <= epsilon:
            return x_n  
        
        f_prime_x_n = f_prime(x_n)
        if f_prime_x_n == 0:
            raise ValueError("La derivada es 0 en x = {}, no se puede continuar.".format(x_n))
        

        x_n = x_n - f_x_n / f_prime_x_n
    
    raise ValueError("El método de Newton no convergió después de {} iteraciones".format(max_iter))

def f(x):
    return 2*x**2  
def f_prime(x):
    return 4*x


