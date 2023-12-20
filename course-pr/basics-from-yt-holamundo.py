""" Modulo para usar reduce """
import functools

def multiply(num1,num2):
    """ Funcion que multiplica sin  usar el simbolo * """
    result = 0
    sign = abs(num1) == num1
    for _ in range(0,abs(num1)):
        result = result + num2 if sign else result - num2
    return result

def get_biggest(array):
    """Fucion que devuelve el numero mas alto de un array, recorriendolo una vez"""
    return functools.reduce(lambda a,b: a if a>b else b, array)

def clean(array):
    """Funcion que aplana un array con un una funcion reduce"""
    elements = functools.reduce(lambda acc,element: acc+[element] if element else acc, array,[])
    return elements

def clean2(array):
    """Funcion que aplana un array con un ciclo for"""
    cleaned_array = [elem for elem in array if elem is not None and elem != 0]
    return cleaned_array

def flatten(array):
    """Funcion que aplana un array, con arrays como elementos"""
    flattened = functools.reduce(lambda a,b: a+b if isinstance(b,list) else a,array,[])
    return flattened
d = flatten([[1,[2]],[1,[2]],[1,[2]]])
print(d)