def bisiesto(anio):
    if anio % 4 == 0:
        return "Es bisiesto"
    else:
        return "No es bisiesto"
anio = 2024
esBisiesto = bisiesto(anio)
print(anio, esBisiesto)
