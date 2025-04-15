import numpy as np
from sympy import symbols, solve, Eq
print("Por favor digite cuantas recursiones tendrá su ecuación recursiva")
n = int(input())
print("Por favor digite los coeficientes de la ecuación de recurrencia")
i = 0
l = []
for i in range (n+1):
    l.append(int(input()))
print(l)
l2 = []
print("Por favor digite las condiciones iniciales")
i = 0
for i in range(n):
    l2.append(int(input()))
    
p = np.roots(l)
print(p)
C = symbols('C0:%d' % n)
equations = []
for k in range(n):
    # La solución general es sum(C_i * r_i^k para i de 0 a n-1)
    lhs = sum(C[i] * (p[i]**k) for i in range(n))
    equations.append(Eq(lhs, l2[k]))

print("\nSistema de ecuaciones:")
for eq in equations:
    print(eq)

# Resolver el sistema
solution = solve(equations, C)

if solution:
    print("\nSolución para las constantes:")
    for key, value in solution.items():
        print(f"{key} = {value}")
else:
    print("\nNo se pudo encontrar una solución para las constantes.")
