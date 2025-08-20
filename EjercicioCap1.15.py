# Importación de bibliotecas
import numpy as np  # Operaciones matemáticas eficientes y manejo de arrays
import matplotlib.pyplot as plt  # Visualización gráfica

# PARÁMETROS FÍSICOS DEL PROBLEMA

A = 1  # Amplitud de las ondas (valor dado en el problema)
k = 2 * np.pi / 0.3  # Número de onda (k = 2π/λ)
r0 = np.array([-1, 0])  # Posición de la primera fuente de onda (x,y)
r1 = np.array([1, 0])   # Posición de la segunda fuente de onda (x,y)

# CREACIÓN DE LA MALLA DE PUNTOS

# Definimos el rango de -4 a +4 en ambos ejes con 500 puntos cada uno para tener buena resolución en la visualización
x = np.linspace(-4, 4, 500)  # genera puntos equiespaciados en un intervalo
y = np.linspace(-4, 4, 500)  # '' genera puntos equiespaciados en un intervalo
X, Y = np.meshgrid(x, y)  # Convierte los vectores 1D en matrices 2D

# CÁLCULO DE LAS DISTANCIAS A LAS FUENTES

# Para cada punto (x,y) en la malla, calculamos su distancia a cada fuente:
R0 = np.sqrt((X - r0[0])**2 + (Y - r0[1])**2) # Distancia a la primera fuente (r0)
R1 = np.sqrt((X - r1[0])**2 + (Y - r1[1])**2) # Distancia a la segunda fuente (r1)

# CÁLCULO DEL PATRÓN DE INTERFERENCIA

# El patrón de interferencia es la suma de las dos ondas sinusoidales: W = A*sin(k*|r-r0|) + A*sin(k*|r-r1|)
W = A * np.sin(k * R0) + A * np.sin(k * R1)

# VISUALIZACIÓN DEL RESULTADO

# Creamos una figura de tamaño 10x8
plt.figure(figsize=(10, 8))

# Mostramos el patrón de interferencia usando imshow()
plt.imshow(W, #matriz de amplitudes
           extent=[-4, 4, -4, 4],  # Límites de los ejes x e y
           cmap='viridis',         # Mapa de colores (mejor contraste)
           origin='lower')         # Origen en esquina inferior izquierda

# Añadimos una barra de color para indicar la amplitud
plt.colorbar(label='Amplitud de la onda')

# Configuramos título y etiquetas de los ejes
plt.title('Patrón de Interferencia de Dos Ondas', fontsize=14)
plt.xlabel('Coordenada x (m)', fontsize=12)
plt.ylabel('Coordenada y (m)', fontsize=12)

# Marcamos las posiciones de las fuentes con puntos rojos
plt.scatter([r0[0], r1[0]],  # Coordenadas x de las fuentes
            [r0[1], r1[1]],  # Coordenadas y de las fuentes
            color='red',     # Color de los marcadores
            s=50,            # Tamaño de los marcadores
            label='Fuentes de onda')  # Etiqueta para la leyenda

plt.legend(fontsize=12) #muestra la leyenda
plt.tight_layout() #evita superposición de elementos
plt.show() #muestra el gráfico