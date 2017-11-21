'''
                CALCULO IV
Avalição 2 - Trabalho de Cálculo numérico


Autor: Allex Magno Andrade
'''

import csv

# f(x) = x³ - 2x² - 3x + 10
def f(x):
    return pow(x, 3) - 2*pow(x, 2) - 3*x + 10

a = -3
b = -1

e = 1/10000000000
k = 0
listaX = []
listaY = []

k = 1

while (abs(f(a)) > e):
    if (abs(f(b)) < e or abs(b - a) < e):
        a = b
        break
    x2 = b - (f(b) / (f(b) - f(a))) * (b - a)
    listaX.append(x2)
    listaY.append(f(x2))
    print("x =", x2)
    print('f(x)=', f(x2))
    if (abs(f(x2)) < e or abs(x2 - b) < e):
        a = x2
        break
    a = b
    b = x2
    k += 1

print("raiz = ", a)
print('f(x)=', f(a))
print("iterações: ", k)

#Gerando arquivo em cvs

f = open('secante.csv', 'w')
try:
    writer = csv.writer(f)
    writer.writerow(('x', 'f(x)'))
    for i in range(k):
        writer.writerow((listaX.pop(), listaY.pop()))
finally:
    f.close()