'''
                CALCULO IV
Avalição 2 - Trabalho de Cálculo numérico


Autor: Allex Magno Andrade
'''

import csv
import os
# f(x) = x³ - 2x² - 3x + 10


def f(x):

    return pow(x, 3) - 2*pow(x, 2) - 3*x + 10
# Intervalo inicial [a, b] e precisão "e" e k quantidade de iterações começando em 1
a = -3
b = -1

e = 1/10000000000
k = 1
listaX = []
listaY = []

while b - a < e or k < 500:
    if abs(a) < e or abs(b) < e: break
    m = f(a)
    x = (a*f(b) - b*f(a))/(f(b)-f(a))
    listaX.append(x)
    listaY.append(f(x))
    print('x = ', x)
    print('f(x)=', f(x))
    if abs(f(x))< e: break
    if m*f(x) > 0:
        a = x
    else:
        b = x

    k += 1

print('foram ', k, 'iterações')
print('x = ', x)
print('f(x)=', f(x))

#Gerando arquivo em cvs

f = open('posicaFalsa.csv', 'w')
try:
    writer = csv.writer(f)
    writer.writerow(('x', 'f(x)'))
    for i in range(k):
        writer.writerow((listaX.pop(), listaY.pop()))
finally:
    f.close()