
#Variables para testeo, son anios que cumplen caracteristicas como divisible por 4, divisible por 100 o 400 por separado
bis_years = [2020, 2012, 2000, 2400]
not_bis_years = [2019, 1981,1900, 2100]

def leap_year(num):
    divisible_by4 = num % 4 == 0
    divisible_by100 = num % 100 == 0
    divisible_by400 = num % 400 == 0   
    if not divisible_by4:
        return 'No bisiesto'
    elif not divisible_by100 or divisible_by400:
        return 'Bisiesto'
    else:
        return 'No bisiesto'



# year = int(input('Ingrese el año que desea saber si es bisiesto  '))
for el in bis_years:
    print(leap_year(el))






