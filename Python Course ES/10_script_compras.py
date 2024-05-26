import random
import time
import os

def obtener_bola():
    bolas = {    #devuelve el color de la bola, y el descuento a aplicar en una tupla
        0 : ('BLANCA', 0),
        1 : ('AZUL', 0.10),
        2 : ('ROJA', 0.20),
        3 : ('VERDE', 0.25),
        4 : ('AMARILLA', 0.50),
    }
    aleatorio = random.randrange(0, len(bolas))
    return bolas[aleatorio]


def calcular_pago(ticket):  #calcula pago y devuelve mensaje, si es blanca es diferente porque no aplica descuento y queda mal devolver el mismo texto    
    color,desc = obtener_bola()
    a_pagar = ticket * (1-desc) 
    if color == 'BLANCA':
        return f'ALEATORIAMENTE OBTUVO UNA BOLA BLANCA, SU TOTAL SIGUE SIENDO ${ticket} :c\n'
    else:
        return f'\nALEATORIAMENTE OBTUVO UNA BOLA {color}\nSU NUEVO TOTAL ES DE ${a_pagar}\nCON UN DESCUENTO DEL {desc*100}%, SU TOTAL ERA DE {ticket}\n'


def girar_tombola(cuenta):
    #imprime la cuenta regresiva y una "barra de carga" jaja en pantalla
    limpiar_pantalla()
    for num in range(cuenta,-1,-1):
        print('GIRANDO TOMBOLA... CUENTA REGRESIVA',num)
        asteriscos = "*" * (cuenta-num) * 2 
        rayas = "-" * num * 2
        print(f'[{ asteriscos }{ rayas }]')
        time.sleep(1)
        limpiar_pantalla()

        
def limpiar_pantalla():
    os.system('cls')


while True:    
    cantidad = input("INGRESE EL VALOR DE SU COMPRA ('E' PARA SALIR): ")
    if cantidad.lower() == 'e':
        break
    
    try:
        cantidad = float(cantidad)
    except ValueError:
        limpiar_pantalla()
        print("ERROR: INGRESE UN VALOR NUMERICO O 'E' PARA SALIR")
        continue
    
    if cantidad < 100:
        limpiar_pantalla()
        print('NO APLICA A LA PROMOCION, SU COMPRA FUE MENOR A $100\n')   
        continue
    
    resultado = calcular_pago(cantidad)
    girar_tombola(10)
    print(resultado)
