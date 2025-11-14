"""[P] Deriva la Ecuación (8.4) para el problema del proyectil bidimensional en presencia de resistencia del aire.
Implementa esto mediante programación usando rk4_gen() y grafica la trayectoria"""




import numpy as np                # importa NumPy y lo alias como np (operaciones numéricas, arrays)
import matplotlib.pyplot as plt   # importa matplotlib.pyplot para graficar, alias plt

def rk4_gen(f, y0, t, args=()):
    """
    Implementación el método Runge-Kutta de 4º orden. porque las ecuaciones del movimiento con resistencia del aire no
    tienen solución analítica. RK4 nos permite aproximar la trayectoria usando las derivadas de posición y velocidad.

    """
    n = len(t)                         # número de instantes de tiempo
    y = np.zeros((n, len(y0)))         # matriz para guardar solución: n filas, len(y0) columnas
    y[0] = y0                          # condición inicial en la primera fila
    
    for i in range(n - 1):             # bucle sobre intervalos de tiempo
        h = t[i+1] - t[i]              
        
        # Calcula la evolución temporal del estado usando cuatro evaluaciones de la derivada por paso (k1..k4) 
        # y promedia esas pendientes para obtener una aproximación precisa
        k1 = h * f(t[i], y[i], *args)
        k2 = h * f(t[i] + h/2.0, y[i] + k1/2.0, *args)
        k3 = h * f(t[i] + h/2.0, y[i] + k2/2.0, *args)
        k4 = h * f(t[i] + h, y[i] + k3, *args)
        
        y[i+1] = y[i] + (k1 + 2.0*k2 + 2.0*k3 + k4) / 6.0
        
    return y                            # devuelve la matriz solución (cada fila = estado en t[i])

def modelo_proyectil(t, S, k, g):
    """
    Esta función representa las ecuaciones físicas que describen cómo se mueve el proyectil cuando hay gravedad y resistencia del aire.
El método RK4 necesita esta función para saber cómo cambia la posición y la velocidad en cada instante.
    """
    x, vx, y, vy = S                    # desempaqueta el vector estado
    
    # Velocidad total (magnitud)
    v_mag = np.sqrt(vx**2 + vy**2)     
    
    # Derivadas
    dxdt = vx
    dvxdt = -k * vx * v_mag             # resistencia del aire proporcional a v * vx (modelo simple)
    dydt = vy
    dvydt = -g - k * vy * v_mag         # gravedad + resistencia vertical
    
    return np.array([dxdt, dvxdt, dydt, dvydt])

# --- Parámetros y condiciones iniciales del problema ---
k = 1.0               # coeficiente de resistencia del aire (más alto = más rozamiento)
g = 9.81              # gravedad [m/s^2]
x0 = 1.0              # posición inicial x [m]
vx0 = 2.0             # velocidad inicial en x [m/s]
y0 = 5.0              # posición inicial y [m]
vy0 = 7.808           # velocidad inicial en y [m/s]

# Vector de estado inicial S = [x0, vx0, y0, vy0]
S0 = np.array([x0, vx0, y0, vy0])

# --- Configuración del tiempo de integración ---
t_inicio = 0.0
t_fin = 2.5
N = 1000  # Número de pasos para una buena resolución
t_puntos = np.linspace(t_inicio, t_fin, N)  # array de tiempos uniformes

# --- Resolver el sistema de EDOs ---
# Pasamos las constantes (k, g) como argumentos adicionales
solucion = rk4_gen(modelo_proyectil, S0, t_puntos, args=(k, g))


# La solución tiene 4 columnas: x, vx, y, vy
x_t = solucion[:, 0]
vx_t = solucion[:, 1]
y_t = solucion[:, 2]
vy_t = solucion[:, 3]

# --- Graficar la trayectoria y(t) en función de x(t) ---
plt.figure(figsize=(10, 6))                    # crea una figura de 10x6 pulgadas
plt.plot(x_t, y_t, label=f'Trayectoria (k={k})')  # dibuja y vs x, etiqueta con el valor de k
plt.title('Trayectoria del Proyectil 2D con Resistencia del Aire')
plt.xlabel('Posición x(t) [m]')
plt.ylabel('Posición y(t) [m]')
plt.grid(True)
plt.legend()
# plt.axis('equal') # Descomenta esto para una escala 1:1 (útil para ver ángulos reales)
plt.show()                                     # muestra la figura
