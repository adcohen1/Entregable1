import sympy as sp

n: int = int(input('Digite el grado su relación de recurrencia: '))
coeficientes = [0] * n
ci = [0] * n

for i in range(n):
    coeficientes[i] = int(input(f'Digite el coeficiente del termino f(n-{i + 1}) de la relación de recurrencia: '))

for i in range(n):
    ci[i] = int(input(f'Digite la condición inicial f({i}): '))

relacion: str = 'Su relación de recurrencia: \n\nf(n) = '
for i in range(n):
    if coeficientes[i] < 0:
        if i == 0:
            relacion += '-'
        else:
            relacion[:-2] = '-'

    # match:
    #   case coeficientes[i] > 1:
    #     relacion += f'{coeficientes[i]}f(n - {i + 1}) + '

    if coeficientes[i] == 0:
        continue
    elif coeficientes[i] == 1:
        relacion += f'f(n - {i + 1}) + '
    elif coeficientes[i] == -1:
        relacion += f'-f(n - {i + 1}) + '
    relacion += f'{coeficientes[i]}f(n - {i + 1}) + '

relacion = relacion[:-2]

print(relacion)

print(
    f'\nSu relación de recurrencia: \n\n\t f(n) = {a} * f(n - 1) + {b} * f(n - 2) \tf(0) = {c[0]}, f(1) = {c[1]} \n\ntiene el polinómio característico: \n\n\t x^2 - {a}x - {b} = 0')

x = sp.symbols('x')
r = sp.symbols('r1:3')

r = sp.Poly(x ** 2 - a * x - b).all_roots()
print(f'\ncon raices x1 = {r[0]} y x2 = {r[1]}')

s = sp.symbols('s1:3')

epsilon: float = 10 ** -6
if abs(r[0] - r[1]) > epsilon:
    f = s[0] * r[0] ** x + s[1] * r[1] ** x
else:
    f = (s[0] + s[1] * x) * r[0] ** x

fn = sp.lambdify((x, s), f)
Eq = [fn(x, s) - c[x] for x in range(2)]
print('\nSistema de ecuaciones')
for i in range(len(Eq)):
    print(Eq[i])
print('\nSolución del sistema de ecuaciones')
Sol = sp.solve(Eq)
print(Sol)
print('\nSolución no recurrente para f(n)')
print('f(n)=', f.subs(Sol))
