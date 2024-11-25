def contar_mayores_20(edades):
    """
    Esta función cuenta cuántas personas tienen edades superiores a 20 años en una tupla de edades.
    Parámetros:
    edades: Tupla de edades.
    
    Devuelve:
    La cantidad de personas con edades superiores a 20.
    """
    return sum(1 for edad in edades if edad > 20)

# Ejemplo de uso
edades = (18, 25, 30, 19, 22, 21, 28, 15, 50, 14)
print(contar_mayores_20(edades))  # Output: 6
