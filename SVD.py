import numpy as np # Importar NumPy para manejo de matrices
from sklearn.decomposition import TruncatedSVD # truncatedSVD encargada de aplicar el SVD de forma reducida

# Matriz de ejemplo (puede representar cualquier conjunto de datos)
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

#crea el modelo SVD, se quiere reducir a 2 dimensiones principales 
svd = TruncatedSVD(n_components=2, random_state=42)

A_reducida = svd.fit_transform(A) #cálcula la descomposición SVD y reduce la dimensionalidad

# resultados
print("Matriz original A:\n", A) #la que se quiere descomponer
print("\nMatriz reducida (UΣ):\n", A_reducida) #cada fila es una representación en el espacio reducido
print("\nComponentes (V^T):\n", svd.components_) #las direcciones principales en el espacio original
print("\nValores singulares:\n", svd.singular_values_) #importancia de cada componente

# Reconstrucción aproximada de A
A_aprox = np.dot(A_reducida, svd.components_)
print("\nAproximación de A (UΣV^T):\n", A_aprox)
