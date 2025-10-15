import numpy as np

# (a) sqrt(x+1) - sqrt(x)
def original_a(x):
    return np.sqrt(x + 1) - np.sqrt(x)

# Reescrita multiplicando por el conjugado:
# (√(x+1) - √x) * (√(x+1) + √x) / (√(x+1) + √x) = 1 / (√(x+1) + √x)
def stable_a(x):
    return 1 / (np.sqrt(x + 1) + np.sqrt(x))


# (b) 1/(x+1) - 2/x + 1/(x-1)
def original_b(x):
    return 1/(x + 1) - 2/x + 1/(x - 1)

# Reescrita con denominador común (para evitar cancelación cuando x es grande)
# f(x) = (x^2 - 2x(x^2-1) + x^2 - 1) / (x(x+1)(x-1))
def stable_b(x):
    return 2 / (x**3 - x)


# (c) 1/√x - 1/√(x+1)
def original_c(x):
    return 1/np.sqrt(x) - 1/np.sqrt(x + 1)

# Reescrita multiplicando por el conjugado:
# (√(x+1) - √x) / (√x√(x+1)(√(x+1)+√x)) = 1 / (√x√(x+1)(√(x+1)+√x))
def stable_c(x):
    return 1 / (np.sqrt(x) * np.sqrt(x + 1) * (np.sqrt(x + 1) + np.sqrt(x)))


# Prueba numérica
xs = [10, 100, 1000, 1e6]

print(" x\t| (a) original vs estable")
for x in xs:
    print(f"{x:.0f}\t| {original_a(x):.8e}  vs  {stable_a(x):.8e}")

print("\n x\t| (b) original vs estable")
for x in xs:
    print(f"{x:.0f}\t| {original_b(x):.8e}  vs  {stable_b(x):.8e}")

print("\n x\t| (c) original vs estable")
for x in xs:
    print(f"{x:.0f}\t| {original_c(x):.8e}  vs  {stable_c(x):.8e}")
