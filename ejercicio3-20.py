import numpy as np 
import matplotlib.pyplot as plt
from scipy.special import hermite # Importa los polinomios de Hermite
from math import factorial # Importa el factorial para normalización

#a)
def classical_probability_density(x, x0):
    """
    Calcula la densidad de probabilidad clásica Pc(x) para un oscilador armónico.
    x: posición en la que se quiere calcular la probabilidad
    x0: amplitud máxima de la oscilación
    """
    if np.abs(x) > x0: # Verifica si x está fuera de la amplitud máxima
        return 0 # Fuera de los límites, la probabilidad es 0
    # Si está dentro de los límites, calcula la densidad usando la fórmula clásica
    return 1 / (np.pi * np.sqrt(x0**2 - x**2)) # Densidad de probabilidad clásica para el oscilador

#b)
def quantum_harmonic_oscillator_eigenfunction_squared(x, n, m=1, omega=1, hbar=1):
    """
    Calcula el cuadrado de la función de onda del oscilador armónico cuántico.
    x: posición
    n: número cuántico
    m: masa de la partícula (por defecto 1)
    omega: frecuencia angular (por defecto 1)
    hbar: constante de Planck reducida (por defecto 1)
    """
    alpha = np.sqrt(m * omega / hbar) # Calcula el parámetro alfa que depende de m, omega y hbar
    y = alpha * x # Escala la posición x según alfa

    hermite_poly = hermite(n) # Obtiene el polinomio de Hermite de grado n
    H_n_y = hermite_poly(y) # Calcula el polinomio de Hermite para el valor de y

    # Calcula el cuadrado de la función de onda normalizada
    # La normalización garantiza que la integral sobre x sea 1 (probabilidad total = 1)
    psi_n_squared = (1 / (2**n * factorial(n) * np.sqrt(np.pi))) * np.exp(-y**2) * (H_n_y)**2
    #si n aumenta se aproxima a la solucion clasica

    return psi_n_squared * alpha # Devuelve la densidad de probabilidad cuántica normalizada

# Función que genera las gráficas comparativas
def plot_oscillators(): 
    x0 = 5  # Define la amplitud máxima para el oscilador clásico

    # Genera un rango de posiciones x en el intervalo
    x_vals = np.linspace(-x0 * 1.1, x0 * 1.1, 500)

    # Calcula la densidad de probabilidad clásica para cada valor de x usando la función definida previamente
    pc_vals = np.array([classical_probability_density(x, x0) for x in x_vals])

    # Reemplaza los valores infinitos con 0 para evitar problemas de graficado en los límites
    pc_vals[np.isinf(pc_vals)] = 0

    # Define los números cuánticos que se van a graficar
    n_values = [3, 10, 20, 150]

    # Crea una figura de tamaño adecuado para mostrar las gráficas
    plt.figure(figsize=(12, 8))

    # Graficar la solución clásica: la densidad de probabilidad Pc(x)
    plt.plot(x_vals, pc_vals, label='Clásico $P_c(x)$', color='red', linestyle='--')

    # Graficar las soluciones cuánticas para los diferentes valores de n
    for n in n_values:
        # Calcula el cuadrado de la función de onda cuántica para cada valor de n
        psi_squared_vals = np.array([quantum_harmonic_oscillator_eigenfunction_squared(x, n) for x in x_vals])
        # Graficar cada densidad de probabilidad cuántica
        plt.plot(x_vals, psi_squared_vals, label=f'Cuántico $|\psi_{n}(x)|^2$')

    # Añadir título y etiquetas a los ejes
    plt.title('Comparación de Osciladores Armónicos Clásico y Cuántico')
    plt.xlabel('Posición $x$')
    plt.ylabel('Densidad de Probabilidad')
    plt.legend() # Mostrar leyenda para las curvas
    plt.grid(True) # Mostrar la cuadrícula en el gráfico
    plt.ylim(bottom=0) # Asegurar que el eje y comience en 0 para una visualización más clara
    plt.show() # Muestra el gráfico generado

# Si el script es ejecutado directamente, se llama a la función para graficar
if __name__ == '__main__':
    plot_oscillators()
