def contar_mayusculas(cadena):
    """
    Esta función cuenta cuántas letras mayúsculas tiene una cadena dada.
    Parámetros:
    cadena: Cadena de texto a evaluar.
    
    Devuelve:
    La cantidad de letras mayúsculas en la cadena.
    """
    return sum(1 for c in cadena if c.isupper())

# Ejemplo de uso
texto = input("Ingresa una cadena: ")
print(f"El número de letras mayúsculas es: {contar_mayusculas(texto)}")
