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

def funcion_de_prueba(x):
    """
    Definición de una función de argumento x

    Argumentos de entrada:
        x: valor donde se quiere evaluar la función

    Resultado obtenido:
        Imagen de la función en x 
    """
    return np.cos(x)

# Valor verdadero de la integral definida
Valor_verdadero_integral = 1/np.sqrt(2)

# Aproximación con 10 subintervalos
n1 = 10
n2 = 100

a1 = puntoMedio(0,np.pi/4,funcion_de_prueba,n1)
# Error relativo de la aproximación
Error_a1 = np.abs(a1-Valor_verdadero_integral)/np.abs(Valor_verdadero_integral)

a2 = puntoMedio(0,np.pi/4,funcion_de_prueba,n2) 
Error_a2 = np.abs(a2-Valor_verdadero_integral)/np.abs(Valor_verdadero_integral)

print(f"""
      Mediante Punto Medio:\n
Valor aproximado: {a1:.8e}; Error realavito: {Error_a1:.8e} con {n1} subintervalos\n
Valor aproximado: {a2:.8e}; Error realavito: {Error_a2:.8e} con {n2} subintervalos\n
""")
a1 = trapezoide(0,np.pi/4,funcion_de_prueba,n1)
Error_a1 = np.abs(a1-Valor_verdadero_integral)/np.abs(Valor_verdadero_integral)

a2 = trapezoide(0,np.pi/4,funcion_de_prueba,n2) 
Error_a2 = np.abs(a2-Valor_verdadero_integral)/np.abs(Valor_verdadero_integral)

print(f"""
      Mediante Trapezoide:\n
Valor aproximado: {a1:.8e}; Error realavito: {Error_a1:.8e} con {n1} subintervalos\n
Valor aproximado: {a2:.8e}; Error realavito: {Error_a2:.8e} con {n2} subintervalos\n
""")
# Confome el número de subintervalos aumenta el Error relativo de la aproximación disminuye
