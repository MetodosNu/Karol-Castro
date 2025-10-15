import numpy as np
import matplotlib.pyplot as plt

def f(x):
    g = 1 + 3*(1 - x)       # = 4 - 3x
    # usamos abs dentro del log como en el enunciado
    with np.errstate(divide='ignore', invalid='ignore'):
        y = x**6 + 0.1 * np.log(np.abs(g))
    return y

# dominio
x_coarse = np.linspace(0.5, 1.5, 100)     # malla gruesa (100 puntos)
x_fine   = np.linspace(0.5, 1.5, 10000)   # malla fina (10000 puntos)
xs = [x_coarse, x_fine]

y_coarse = f(x_coarse)
y_fine   = f(x_fine)

# detectar la singularidad analítica
x_sing = 4/3.0
print("Singularidad en x =", x_sing)

# Para graficar: reemplazar -inf/nan por np.nan (matplotlib separa la curva)
y_coarse_plot = y_coarse.copy()
y_fine_plot   = y_fine.copy()

y_coarse_plot[~np.isfinite(y_coarse_plot)] = np.nan
y_fine_plot[~np.isfinite(y_fine_plot)] = np.nan

# También crear una versión recortada (clipped) para poder "ver" la caída sin -inf
clip_min = -20.0   # elige un valor negativo grande para visualizar la caída
clip_max = np.nanmax(np.concatenate([y_coarse[np.isfinite(y_coarse)],
                                     y_fine[np.isfinite(y_fine)]]))
y_coarse_clipped = np.where(np.isfinite(y_coarse), np.clip(y_coarse, clip_min, clip_max), np.nan)
y_fine_clipped   = np.where(np.isfinite(y_fine),   np.clip(y_fine,   clip_min, clip_max), np.nan)

# ----------------- Traza -----------------
plt.figure(figsize=(12,5))

# izquierda: malla gruesa
ax1 = plt.subplot(1,2,1)
ax1.plot(x_coarse, y_coarse_plot, 'o-', markersize=4, label='100 puntos (gruesa)')
ax1.plot(x_coarse, y_coarse_clipped, 'o', alpha=0.0)  # para mantener límites si queremos
ax1.axvline(x_sing, color='k', linestyle='--', label=f'sing. x={x_sing:.3f}')
ax1.set_title('Malla gruesa (100 puntos)')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.grid(True)
ax1.legend()

# derecha: malla fina (línea continua)
ax2 = plt.subplot(1,2,2)
ax2.plot(x_fine, y_fine_plot, '-', linewidth=1, label='10000 puntos (fina)')
# también dibujamos la versión recortada para ver el "pozo" si quieres enfocar la escala
ax2.plot(x_fine, y_fine_clipped, '-', linewidth=1, alpha=0.0)
ax2.axvline(x_sing, color='k', linestyle='--', label=f'sing. x={x_sing:.3f}')

ax2.set_title('Malla fina (10000 puntos)')
ax2.set_xlabel('x')
ax2.grid(True)
ax2.legend()

plt.suptitle('Ejercicio 2.5 — Efecto de la resolución y singularidad en f(x)')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

# ----------------- Gráfica adicional con límites ajustados para visualizar la caída -----------------
plt.figure(figsize=(8,4))
plt.plot(x_fine, y_fine_clipped, '-', label='f(x) (clipped)')
plt.axvline(x_sing, color='k', linestyle='--', label=f'sing. x={x_sing:.3f}')
plt.ylim(clip_min, clip_max)   # mostrar el rango recortado
plt.xlabel('x')
plt.ylabel('f(x) (clipped)')
plt.title('Versión recortada para visualizar la caída en la singularidad')
plt.grid(True)
plt.legend()
plt.show()
