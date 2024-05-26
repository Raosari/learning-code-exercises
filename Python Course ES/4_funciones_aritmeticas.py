def operaciones(a,b,operacion):
    match operacion:
        case 1:
            return a+b
        case 2:
            return a-b
        case 3:
            return a*b
        case 4:
            return a/b
        

a = int(input('Ingrese el valor de \'a\''))
b = int(input('Ingrese el valor de \'b\''))
c = input('Ingrese la operacion que desea realizar\n-sumar\n-restar\n-multiplicar\n-dividir\n')

print(f'el resultado de {c} \'a\' y \'b\' es {operaciones(a,b,c):.2f}')