def calculate_iva(lista):
    total = sum(lista)
    total_with_iva = total*1.16
    return total_with_iva

lista = [50,20,30]

calculate_iva(lista)