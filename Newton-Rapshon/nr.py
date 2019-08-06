from sympy import *
from math import *

x = symbols('x')

f = '-ln(x**3) - cos(x)*sin(x) + 4'
f_x = sympify(f)
df_x = diff(f_x, x)

xs = float(1)
x0 = xs
tol = 0.0001
cont = 0

while(True):

    xn = xs - (f_x.subs(x, xs)/df_x.subs(x, xs))

    cont += 1

    if(abs(xn-xs) <= tol):
        xs = xn
        break

    xs = xn

print('A raiz da função f(x) = ', f, 'é x = {0:.2f}'.format(xs))
print('Foram utilizados {:d} tentativas pelo método de Newton-Rapshon para encontrar a raiz, a partir de x_0 = {:.1f}'.format(cont, x0))
