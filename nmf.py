from sklearn.decomposition import NMF # NMF para descomposición no negativa
import numpy as np # Importar NumPy para manejo de matrices

# Matriz de datos originales (solo valores positivos)
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Modelo NMF con 2 componentes
nmf = NMF(n_components=2, init='nndsvd', random_state=42) #descompone la matriz en dos matrices no negativas

# Ajuste del modelo
W = nmf.fit_transform(X) #el modelo se ajusta los datos  y genera la matriz W
H = nmf.components_

print("Matriz W:\n", W) # W es la matriz de características
print("Matriz H:\n", H) # H es la matriz de pesos
print("Aproximación X ≈ W·H:\n", np.dot(W, H)) 
