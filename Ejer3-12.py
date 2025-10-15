import numpy as np
import matplotlib.pyplot as plt

f = 1               # f(xi)
f2 = 0.1            # f''(xi)
f3 = 100            # f'''(xi)
eps_m = 2.22e-16    # error de redondeo

# Valores de h
h = np.array([1e-1, 1e-2, 1e-3, 1e-4])

# Cálculo de los errores totales
# Ecuación (3.40)
E_340 = (h/2)*abs(f2) + (2*abs(f)*eps_m)/h

# Ecuación (3.41)
E_341 = (h**2/6)*abs(f3) + (abs(f)*eps_m)/h

# Muestra resultados
print("Valores de h: ", h)
print("Error total (Ecuación 3.40): ", E_340)
print("Error total (Ecuación 3.41): ", E_341)

# Grafica de resultados
plt.figure(figsize=(8,5))
plt.loglog(h, E_340, 'o-', label='Ecuación (3.40)')
plt.loglog(h, E_341, 's-', label='Ecuación (3.41)')
plt.xlabel('h')
plt.ylabel('Error total (E)')
plt.title('Comparación del error total para las ecuaciones (3.40) y (3.41)')
plt.grid(True, which='both', ls='--')
plt.legend()
plt.show()

"""
Observaciones:
- Para valores grandes de h, domina el error de aproximación (E_app), por lo que el error total aumenta proporcionalmente a h o h^2.
- Para valores muy pequeños de h, domina el error de redondeo (E_ro), debido al término 1/h, haciendo que el error total también crezca.
- Existe un valor óptimo de h que minimiza el error total.
- La ecuación (3.41), al tener orden h^2 en el término de aproximación, muestra un error menor que la (3.40) para el mismo rango de h.

"""
