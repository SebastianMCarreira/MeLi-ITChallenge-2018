enrut = [
    (9106, 137),
    (5339, 852),
    (3726, 3952),
    (994, 210),
    (5304, 1471),
    (5990, 3581),
    (3266, 4392),
    (5290, 439),
    (9299, 296),
    (9437, 479)
    ]

consultas = [7, 6, 8, 1, 6, 7, 7, 3, 7, 6]

def estaEnRango(x,y):
    extremoXm = x[0] - x[1]
    extremoXM = x[0] + x[1]

    extremoYm = y[0] - y[1]
    extremoYM = y[0] + y[1]
    rango = range(extremoYm,extremoYM)
    if extremoXm in rango and extremoXM in rango:
        return True
    else:
        return False

def obtenerNEnRango(x):
    enRango = 0
    for e in enrut:
        if e != x:
            if estaEnRango(e,enrut[x]):
                enRango+=1
    return enRango

result = ""
for c in consultas:
    hay = obtenerNEnRango(c-1)
    result+=str(hay)

print(result)
