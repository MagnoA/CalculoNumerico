'''
                CALCULO IV
Avalição 2 - Trabalho de Cálculo numérico


Autor: Allex Magno Andrade
'''

import csv

# f(x) = x³ - 2x² - 3x + 10
def f(x):
    return pow(x, 3) - 2*pow(x, 2) - 3*x + 10

# Intervalo inicial [a, b] e precisão "e" e k quantidade de iterações começando em 1
a = -3
b = -1

e = 1/10000000000
k = 0
listaX = []
listaY = []

while (b - a) > e:
    m = f(a)
    x = (a+b)/2
    print('Valor de x =', x)
    listaX.append(str(x))
    listaY.append(str(f(x)))

    if(m*f(x)) > 0:
        a = x
    else:
        b = x
    k += 1
    if k > 500: break

print('Foram ', k, 'iterações')
print('Raiz encontrada x = ', x)
print('Valor de y = f(x) = ', f(x))

#Gerando arquivo em cvs

f = open('bisseccao.csv', 'w')
try:
    writer = csv.writer(f)
    writer.writerow(('x', 'f(x)'))
    for i in range(k):
        writer.writerow((listaX.pop(), listaY.pop()))
finally:
    f.close()


