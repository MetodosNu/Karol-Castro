import numpy as np

# ---------------------------------------------------------
# f(x) = sin(x) mediante su serie de Taylor
# ---------------------------------------------------------
def sin_taylor(x, tol=1e-12, max_terms=100):
    term = x  # primer término (n=0)
    s = term
    n = 1
    while abs(term) > tol and n < max_terms:
        # Relación recursiva:
        # term_n = term_{n-1} * (-x^2) / ((2n)*(2n+1))
        term *= -x**2 / ((2*n)*(2*n+1))
        s += term
        n += 1
    return s, n

# ---------------------------------------------------------
# Evaluar en x = 0.1
# ---------------------------------------------------------
x1 = 0.1
approx1, terms1 = sin_taylor(x1)
print(f"x = {x1}")
print(f"Aproximación: {approx1:.15f}")
print(f"Valor real:   {np.sin(x1):.15f}")
print(f"Términos usados: {terms1}")
print(f"Error absoluto: {abs(approx1 - np.sin(x1)):.3e}\n")

# ---------------------------------------------------------
# Evaluar en x = 40 sin reducción
# ---------------------------------------------------------
x2 = 40
approx2, terms2 = sin_taylor(x2)
print(f"x = {x2} (sin reducción)")
print(f"Aproximación: {approx2:.15f}")
print(f"Valor real:   {np.sin(x2):.15f}")
print(f"Términos usados: {terms2}")
print(f"Error absoluto: {abs(approx2 - np.sin(x2)):.3e}\n")

# ---------------------------------------------------------
# Usar identidad trigonométrica para reducir el ángulo:
# sin(x) = sin(x mod 2π)
# ---------------------------------------------------------
x2_reduced = x2 % (2*np.pi)
approx2r, terms2r = sin_taylor(x2_reduced)
print(f"x = {x2} reducido a {x2_reduced:.6f} rad")
print(f"Aproximación (reducido): {approx2r:.15f}")
print(f"Valor real:              {np.sin(x2):.15f}")
print(f"Términos usados: {terms2r}")
print(f"Error absoluto: {abs(approx2r - np.sin(x2)):.3e}")
