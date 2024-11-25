def mas_larga(lista_palabras):
    """
    Esta función toma una lista de palabras y devuelve la palabra más larga.
    Parámetros:
    lista_palabras: Lista de cadenas de texto.
    
    Devuelve:
    La palabra más larga en la lista.
    """
    return max(lista_palabras, key=len)

# Ejemplo de uso
palabras = ["manzana", "banana", "kiwi", "naranja"]
print(mas_larga(palabras))  # Output: "manzana"
