def binario_a_entero(binario):
    """
    Esta función convierte un número binario (como cadena) en su valor entero correspondiente.
    Parámetros:
    binario: Cadena que representa un número binario.
    
    Devuelve:
    El valor entero correspondiente al número binario.
    """
    return int(binario, 2)

# Ejemplo de uso
binario = "1010"
print(binario_a_entero(binario))  # Output: 10
