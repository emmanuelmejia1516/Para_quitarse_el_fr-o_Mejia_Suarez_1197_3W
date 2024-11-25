def contar_vocales(palabra):
    """
    Esta función cuenta cuántas veces aparece cada vocal (a, e, i, o, u) en una palabra.
    Parámetros:
    palabra: Cadena de texto a evaluar.
    
    Devuelve:
    Un diccionario con la cantidad de cada vocal en la palabra.
    """
    vocales = "aeiou"
    contador = {vocal: palabra.lower().count(vocal) for vocal in vocales}
    return contador

# Ejemplo de uso
palabra = input("Ingrese una palabra: ")
print(contar_vocales(palabra))
