
# from math import sqrt

# a = int(input("Ingrese el coeficiente de 'a' "))
# b = int(input("Ingrese el coeficiente de 'b' "))
# c = int(input("Ingrese el coeficiente de 'c' "))


# in_root = (b**2) - 4*a*c

# if in_root < 0:
#     print('No hay soluciones')

# elif in_root == 0:
#     x1 = -b/(2*a)
#     print(f'La unica solucion es {x1}')
# else:
#     x1 = (-b + sqrt(in_root)) / (2*a)
#     x2 = (-b - sqrt(in_root)) / (2*a)
#     print(f'las soluciones son:\nx1 = {x1}\nx2 = {x2}')


a = int(input("Ingrese el coeficiente de 'a' "))
b = int(input("Ingrese el coeficiente de 'b' "))
c = int(input("Ingrese el coeficiente de 'c' "))


in_root = (b**2) - 4*a*c


def general(delta,a,b):
    if  delta < 0:
        return 'No hay soluciones'
    elif delta == 0:
        x1 = -b/(2*a)
        return f'La unica solucion es {x1}'
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        return f'las soluciones son:\nx1 = {x1}\nx2 = {x2}'

#Scrip para dar solución a ecuaciones cuadraticas
#import math (con esto importas todo el modulo)


# from math import sqrt #con esto solo importas una libreria de todo el modulo
 
# A=float(input("Ingresa el valor de A "))  #pedir a, b y c
# B=float(input("Ingresa el valor de B: "))
# C=float(input("Ingresa el valor de C: "))
# delta= (B**2 - 4*A*C)
 
 
# if (delta<0):#si
#   print("Tu ecuacion no tiene solución en el plano de los reales")

# elif delta == 0:
#   x1= -B/(2*A)
#   print(f"La unica solucion es x1 {x1:.2f}")

# else:
#   x1=-B + sqrt(delta) / (2*A)
#   x2=-B - sqrt(delta) / (2*A)
#   print(f"La primera solucion es: {x1:.2f}")
#   print(f"La segunda solucion es: {x2:.2f}")
