import math

x = 2

#(a) Error absoluto
# f(x) = ln(x)
x_tilde_a = 1.9
f_true_a = math.log(x)
f_approx_a = math.log(x_tilde_a)

error_absoluto = abs(f_true_a - f_approx_a)

print("(a) Error absoluto en f(x) = ln(x):")
print(f"f(2) = {f_true_a:.6f}")
print(f"f(1.9) = {f_approx_a:.6f}")
print(f"Error absoluto = |ln(2) - ln(1.9)| = {error_absoluto:.6e}\n")


#(b) Error relativo
# f(x) = sqrt(x)
x_tilde_b = 1.95
f_true_b = math.sqrt(x)
f_approx_b = math.sqrt(x_tilde_b)

error_relativo = abs((f_true_b - f_approx_b) / f_true_b)

print("(b) Error relativo en f(x) = sqrt(x):")
print(f"f(2) = {f_true_b:.6f}")
print(f"f(1.95) = {f_approx_b:.6f}")
print(f"Error relativo = |sqrt(2) - sqrt(1.95)| / sqrt(2) = {error_relativo:.6e}\n")


#(c) Error hacia atrás (backward error)
# f(x) = e^x, f̃(2) = e^2 = 8 (aproximado)
f_true_c = math.exp(2)
f_tilde_c = 8

# Queremos δx tal que e^(2 + δx) = 8
# => δx = ln(8) - 2
delta_x = math.log(f_tilde_c) - 2
error_backward = abs(delta_x / 2)  # relativo al valor de x

print("(c) Error hacia atrás en f(x) = e^x:")
print(f"f(2) = {f_true_c:.6f}")
print(f"f̃(2) = {f_tilde_c}")
print(f"δx = ln(8) - 2 = {delta_x:.6e}")
print(f"Error hacia atrás relativo = |δx| / |x| = {error_backward:.6e}")
