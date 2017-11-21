'''
                CALCULO IV
Avalição 2 - Trabalho de Cálculo numérico


Autor: Allex Magno Andrade
'''

import csv

# f(x) = x³ - 2x² - 3x + 10
def f(x):
    return pow(x, 3) - 2*pow(x, 2) - 3*x + 10

# y(x) = x - f(x)/f'(x)
def y(x):
    return x - ((pow(x, 3) - 2*pow(x, 2) - 3*x + 10) / (3*pow(x, 2) - 4*x - 3))


# Intervalo inicial [a, b] e precisão "e" e k quantidade de iterações começando em 1
a = -3
b = -1

e = 1/10000000000
k = 1
listaX = []
listaY = []

while (abs(f(a)) > e):
    x = y(a)
    print('x = ', x)
    print('f(x)=', f(x))
    listaX.append(x)
    listaY.append(f(x))

    if (abs(f(x)) < e or abs(x - a) < e):
        a = x
        break
    a = x
    k += 1

print(k, 'iteracoes')
print('raiz', x)

#Gerando arquivo em cvs

f = open('newton.csv', 'w')
try:
    writer = csv.writer(f)
    writer.writerow(('x', 'f(x)'))
    for i in range(k):
        writer.writerow((listaX.pop(), listaY.pop()))
finally:
    f.close()