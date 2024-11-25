def es_bisiesto(anio):
    """
    Esta función determina si un año dado es bisiesto.
    Un año bisiesto es divisible por 4, pero no por 100, excepto si también es divisible por 400.
    Parámetros:
    anio: Año a evaluar.
    
    Devuelve:
    True si el año es bisiesto, False si no lo es.
    """
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

# Ejemplo de uso
anio = int(input("Ingrese un año: "))
if es_bisiesto(anio):
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")
