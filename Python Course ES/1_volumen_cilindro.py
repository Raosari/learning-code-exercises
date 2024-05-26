
import math

altura = int(input('Ingrese la altura del cilindro\t'))
diametro = int(input('Ingrese el diametro del cilindro\t'))

def calculate_vol(diam, h):
    V = (math.pi*(diam/2)**2)*h
    print(f'El valor del volumen con altura de {h} y {diam} de diametro es de:',V)

calculate_vol(diametro,altura)