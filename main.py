"""  
autores: 
    José-Job Flores Godoy (punto medio)
    Felipe Ernesto Paladino Choza 
    Santiago Osvaldo Blanco Canaparro

Este programa es un tributo al físico japonés Pierre de Fermat (1933-2012), y al 
operario de caja registradora Sebastián Torres (1982-2025)
"""

import numpy as np

def puntoMedio(a,b,fun,n):
    """Aproxima la integral definida de arg:fun en intervalo [arg:a,arg:b] utilizando arg:n subintervalos usando la Regla del punto medio

    Argumentos de entrada:
        a: inicio del intervalo
        b: fin del intervalo
        fun: función a integrar
        n: número de subintervalos

    Resultado obtenido:
        Valor aproximado de la integral definida de arg:fun en el intevalo [arg:a,arg:b] utilizando arg:n subintervalos

    Observación:
        a<b
    """
    deltaX = (b-a)/n # tamaño del incremento
    x0 = a
    aux = 0
    for ii in range(n):
        x1 = x0 + deltaX
        xm = (x1+x0)/2  # Cáclulo del punto medio
        aux = aux + fun(xm)
        x0 = x1
    return deltaX*aux

def trapezoide(a, b, fun, n):
    """
    Argumentos:
        a: extremo inferior del intervalo 
        b: extremo superior del intervalo 
        fun: integrando
        n: número de subintervalos

    Retorna:
        Valor aproximado de la integral definida de arg:fun en el intevalo [arg:a,arg:b] utilizando arg:n subintervalos

    Observación:
        a<b
    """
    deltaX = (b-a)/n
    x_a = a
    sum = fun(x_a)

    for i in range(1,n):
        x_i = a + i*deltaX
        sum += 2*fun(x_i)

    x_n = a + n*deltaX
    sum += fun(x_n)
    return (deltaX/2)*sum

# %%
# Para verificar que el algoritmo produce resultados correctos, evaluamos un integral definida conocida y comparamos con respecto al valor verdadero conocida. En este caso calculamos:
#        \int_0_{\pi/4} \cos(x)dx = 1/sqrt(2)

def f(x):
    """
    Definición de una función de argumento x

    Argumentos de entrada:
        x: valor donde se quiere evaluar la función

    Resultado obtenido:
        Imagen de la función en x 
    """
    return np.cos(np.sqrt(x))

def L_f(x):
    """
    Derivada de f respecto a x
    Integrando de la función longitud de arco
    """
    return np.sqrt( 1 + (-1*np.sin(np.sqrt(x))*1/(2*np.sqrt(x)))**2)

# Valor verdadero de la longitud de arco de f entre 1 y 5 
Valor_verdadero_integral = 4.17293704556202 
subintervalos = [2, 4, 8, 10, 20, 40, 80, 100, 1000]
a = 1
b = 5

print("Método: Punto Medio")
print("-------------------------------\n")
for i in subintervalos:
    pm = puntoMedio(a,b,L_f,i) 
    err = np.abs(pm-Valor_verdadero_integral)/np.abs(Valor_verdadero_integral)
    print(f"Valor aproximado: {pm:.8e}; Error realavito: {err:.8e} con {i} subintervalos\n")

print("-------------------------------\n")
print("Método: Trapezoide")
print("-------------------------------\n")
for i in subintervalos:
    tr = trapezoide(a,b,L_f,i) 
    err = np.abs(tr-Valor_verdadero_integral)/np.abs(Valor_verdadero_integral)
    print(f"Valor aproximado: {tr:.8e}; Error realavito: {err:.8e} con {i} subintervalos\n")
