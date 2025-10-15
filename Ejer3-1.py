# =====================================
# Ejercicio 3.1 - Comparación con SymPy
# ======================================


from sympy import symbols, exp, sin, diff
from math import exp as mexp, sin as msin, cos as mcos
import numpy as np

# --- Parte 1: Derivada analítica con SymPy ---
x = symbols('x')
f_sym = exp(sin(2*x))
f_prime_sym = diff(f_sym, x)

# Convertir a función numérica
f_prime_num = lambda val: float(f_prime_sym.subs(x, val))

# --- Parte 2: Derivada analítica según código 3.1 ---
def f(x):
    return mexp(msin(2*x))

def fprime(x):
    return 2 * mexp(msin(2*x)) * mcos(2*x)

# --- Parte 3: Comparación de resultados ---
puntos = np.linspace(0, 0.5, 6)

print("Comparación entre SymPy y fprime() del código 3.1:\n")
print(f"{'x':>6} {'SymPy f\'(x)':>18} {'fprime()':>18} {'Diferencia':>15}")
print("-" * 60)

for p in puntos:
    sym_val = f_prime_num(p)
    fprime_val = fprime(p)
    diff_val = abs(sym_val - fprime_val)
    print(f"{p:6.2f} {sym_val:18.10f} {fprime_val:18.10f} {diff_val:15.2e}")
