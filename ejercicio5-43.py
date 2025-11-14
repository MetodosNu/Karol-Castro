"""
--PROBLEMA 5.43 
Modifique el programa action.py para abordar el contexto físico de una pelota lanzada verticalmente. 
Comience pensando qué fuerza implica este caso.
Tome x_0 = x_(n-1) = 0 y τ = 10.
Grafique su solución para la altura de la partícula como una función del tiempo.

--Objetivo:
Analizar la trayectoria de una pelota lanzada verticalmente hacia arriba y que luego regresa al suelo, utilizando el principio de mínima acción

--Se parte de unas condiciones de frontera:
x(0) = 0  (posición inicial en el suelo)
x(τ) = 0  (regresa al suelo)
τ = 10 s  (tiempo total del vuelo)
"""

from multi_newton import multi_newton
import numpy as np
import matplotlib.pyplot as plt   

# FUNCIÓN params()
def params(): # define los parámetros del problema
    nvar = 99      # Número de puntos interiores que discretizan el movimiento(variables desconocidas)
    m = 1.0        # Masa de la pelota (kg)
    g = 9.81       # Aceleración de la gravedad (m/s^2)

    # Condiciones de frontera:
    xini = 0.0      
    xfin = 0.0      
    tt = 10.0       

    # Cálculo del paso de tiempo
    dt = tt / (nvar + 1)    
    return nvar, m, g, xini, xfin, dt   

# FUNCIÓN fod()
# Define la Fuerza que actúa sobre la pelota F(x) = -m*g
def fod(der, x, m, g): # Calcula la fuerza y su derivada
    if der == 0:
        # Como la gravedad es constante, se devuelve F = -m*g para todos los puntos
        return -m * g * np.ones_like(x)
    else:
        # Su derivada con respecto a la posiciónes es cero porque la gravedad no depende de la altura
        return np.zeros_like(x)

# FUNCIÓN actfs()
def actfs(xs): # Construye el sistema de ecuaciones de Euler-Lagrange discretas
    nvar, m, g, xini, xfin, dt = params() 
    arr = np.zeros(nvar)   

    f_values = fod(0, xs, m, g)  # Calcula la fuerza en cada punto
    #Cada punto depende de sus vecinos anterior y siguiente (permite obtener la trayectoria que minimiza la acción)
    arr[0] = (m / dt) * (2 * xs[0] - xini - xs[1]) + dt * f_values[0]

    arr[1:-1] = (m / dt) * (2 * xs[1:-1] - xs[:-2] - xs[2:]) + dt * f_values[1:-1]

  
    arr[-1] = (m / dt) * (2 * xs[-1] - xs[-2] - xfin) + dt * f_values[-1]

    return arr

# FUNCIÓN actjac()
def actjac(actfs, xs): # Calcula la matriz Jacobiana (estructura tridiagonal)
    nvar, m, g, xini, xfin, dt = params()
    Jf = np.zeros((nvar, nvar))

    fp_values = fod(1, xs, m, g)

    np.fill_diagonal(Jf, 2 * m / dt + fp_values * dt) #diagonal principal (punto actual)
    np.fill_diagonal(Jf[1:, :], -m / dt) #subdiagonal  (puntos anteriores)
    np.fill_diagonal(Jf[:, 1:], -m / dt) #superdiagonal (puntos siguientes)

    actfs_xs = actfs(xs)
    return Jf, actfs_xs

# PROGRAMA PRINCIPAL
if __name__ == '__main__':

    # 1. Se definen los parámetros del problema
    nvar, m, g, xini, xfin, dt = params()
    tt = 10.0 

    # 2. Se crea una suposición inicial (necesaria para el método Newton); Se usa una función senoidal como aproximación
    t_interior = np.linspace(dt, tt - dt, nvar)
    xolds = 100 * np.sin(np.pi * t_interior / tt)  

    print("Calculando la trayectoria usando multi_newton...")

    # 3. Se llama al método multi_newton para resolver el sistema y obtener la trayectoria que minimiza la acción
    xnews = multi_newton(actfs, actjac, xolds)

    print("Cálculo completo")

    t_completo = np.linspace(0, tt, nvar + 2)
    x_completo = np.concatenate(([xini], xnews, [xfin]))

    # 6. Se calcula la solución analítica de un M.U.A (para comparación)
    #    Ecuación: x(t) = v0*t - 1/2*g*t^2 
    #    como la pelota parte y regresa al suelo se cumple x(0)=x(τ)=0 y eso da v0 = 0.5*g*τ=49.05 m/s
    v0_analitica = 0.5 * g * tt
    x_analitica = v0_analitica * t_completo - 0.5 * g * (t_completo ** 2)

    # 7. Graficar la trayectoria obtenida
    plt.figure(figsize=(10, 7))
    plt.plot(t_completo, x_completo, 'bo-', label='Solución Numérica (Mínima Acción)', markersize=4)
    plt.plot(t_completo, x_analitica, 'r--', label='Solución Analítica (Parábola)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Altura (m)')
    plt.title('Solución al Problema 5.43: Pelota Lanzada Verticalmente')
    plt.legend()
    plt.grid(True)
    plt.show()

"""""
INTERPRETACIÓN DEL RESULTADO

La solución numérica obtenida (azul) coincide casi perfectamente con la solución analítica (línea roja discontinua):
El principio de mínima acción reproduce la trayectoria parabólica esperada para una pelota lanzada verticalmente bajo la influencia de la gravedad.
La altura máxima alcanzada (~122.7 m) ocurre a los 5 segundos, momento en que la velocidad se anula temporalmente antes de caer.

Se demuestra que la formulación de mínima acción genera la misma trayectoria que la solución clásica de la cinemática.

""" 
