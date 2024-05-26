def add():
    return sum(range(1,100001))


def add2():
    total = 0
    for num in range(1,100001):
        total += num
    return total


def add3(num):
    return sum(range(num + 1))


def commas(num):
    """ Esta funcion devuelve el numero separado por comas p.e. 30000 -> 30,000"""
    invertido = str(num)[::-1]
    groups = [invertido[i:i+3] for i in range(0, len(invertido), 3)]
    result = ",".join(groups)[::-1]
    return result

print(commas(add3(100000)))