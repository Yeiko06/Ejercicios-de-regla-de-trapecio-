import numpy as np
import matplotlib.pyplot as plt

# Definir la función a integrar
def f(x):
    return np.sin(x)

# Implementación de la regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])
    return integral, x, y

# Parámetros de integración
a, b = 0, np.pi
n_values = [5, 10, 20]
exact_integral = 2  # Solución analítica de la integral

for n in n_values:
    integral_approx, x_vals, y_vals = trapezoidal_rule(a, b, n)
    error = abs(exact_integral - integral_approx)
    print(f"n = {n}, Integral aproximada: {integral_approx:.6f}, Error: {error:.6f}")

# Gráfica de la función y la aproximación
x_fine = np.linspace(a, b, 100)
y_fine = f(x_fine)

plt.figure(figsize=(8, 5))
plt.plot(x_fine, y_fine, 'r-', label=r'$f(x) = \sin(x)$', linewidth=2)
for n in n_values:
    _, x_vals, y_vals = trapezoidal_rule(a, b, n)
    plt.fill_between(x_vals, y_vals, alpha=0.3, label=f"Aproximación n={n}")

plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Aproximación de la integral con la regla del trapecio")
plt.legend()
plt.grid()
plt.show()
