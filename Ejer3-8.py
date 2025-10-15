import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# Definición de la función original
# --------------------------
def f(x):
    return (1 - np.cos(x)) / x**2

# Derivada analítica segunda de f(x)
def f_double_prime(x):
    return (2*(1 - np.cos(x)) - x**2 * np.cos(x) - 2*x*np.sin(x)) / x**4

# Versión reescrita (de problema 2.8): evitar cancelación
# Usando identidad trigonométrica 1 - cos(x) = 2 sin²(x/2)
def f_rewritten(x):
    return (2 * np.sin(x/2)**2) / x**2

# --------------------------
# Aproximación por diferencia central a la segunda derivada
# --------------------------
def central_diff_second(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h)) / h**2

# --------------------------
# Parte (a)
# --------------------------
x0 = 0.004
analytic_value = f_double_prime(x0)
print(f"Segunda derivada analítica en x = {x0} es: {analytic_value:.10e}")

# --------------------------
# Parte (b)
# --------------------------
h_values = np.logspace(-1, -6, 50)
errors_original = []

for h in h_values:
    approx = central_diff_second(f, x0, h)
    error = abs(approx - analytic_value)
    errors_original.append(error)

# --------------------------
# Parte (c)
# --------------------------
errors_rewritten = []

for h in h_values:
    approx = central_diff_second(f_rewritten, x0, h)
    error = abs(approx - analytic_value)
    errors_rewritten.append(error)

# --------------------------
# Gráfica log-log
# --------------------------
plt.figure(figsize=(7,5))
plt.loglog(h_values, errors_original, 'o-', label='f(x) original')
plt.loglog(h_values, errors_rewritten, 's-', label='f(x) reescrita')
plt.xlabel('h')
plt.ylabel('Error absoluto')
plt.title('Error en la aproximación de la segunda derivada')
plt.legend()
plt.grid(True, which='both', ls='--', alpha=0.6)
plt.show()
