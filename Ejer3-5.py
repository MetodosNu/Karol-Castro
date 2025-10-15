import numpy as np
import matplotlib.pyplot as plt

# Definimos la función y su segunda derivada analítica
def f(x):
    return np.sin(x)

def d2f_analitica(x):
    return -np.sin(x)

# Rango de evaluación
x = np.linspace(0, 2 * np.pi, 100)
h = x[1] - x[0]

# Segunda diferencia hacia adelante
# f''(x) ≈ (f(x+2h) - 2f(x+h) + f(x)) / h^2
d2f_forward = (f(x + 2*h) - 2*f(x + h) + f(x)) / h**2

# Segunda diferencia centrada
# f''(x) ≈ (f(x+h) - 2f(x) + f(x-h)) / h^2
d2f_central = (f(x + h) - 2*f(x) + f(x - h)) / h**2

# Derivada exacta
d2f_exacta = d2f_analitica(x)

# Graficamos los resultados
plt.figure(figsize=(10,6))
plt.plot(x, d2f_exacta, 'k', label='Derivada exacta (-sin(x))', linewidth=2)
plt.plot(x, d2f_forward, 'r--', label='Segunda diferencia hacia adelante')
plt.plot(x, d2f_central, 'b-.', label='Segunda diferencia centrada')
plt.title('Comparación de aproximaciones de segunda derivada')
plt.xlabel('x')
plt.ylabel('f\'\'(x)')
plt.legend()
plt.grid(True)
plt.show()

# --- Análisis del error ---
error_forward = np.abs(d2f_forward - d2f_exacta)
error_central = np.abs(d2f_central - d2f_exacta)

print(f"Error promedio (hacia adelante): {np.mean(error_forward):.5e}")
print(f"Error promedio (centrada):       {np.mean(error_central):.5e}")

"""
 COMENTARIOS:
 
 En la gráfica se observa:

- La curva negra representa la derivada exacta f''(x) = -sin(x).
- La línea roja (segunda diferencia hacia adelante) sigue la tendencia general, pero presenta un pequeño desfase y un error
  visible en los extremos.
- La línea azul (segunda diferencia centrada) coincide casi perfectamente con la derivada exacta.

Esto confirma la expectativa analítica sobre la dependencia del error con respecto a h:
    - La fórmula hacia adelante tiene error de orden O(h), por lo que disminuye linealmente al reducir h.
    - La fórmula centrada tiene error de orden O(h²), por lo que su precisión mejora mucho más rápido.

"""

