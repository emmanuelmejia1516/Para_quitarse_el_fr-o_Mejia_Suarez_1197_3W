def filtrar_palabras(lista_palabras, n):
    """
    Esta función filtra las palabras de la lista que tienen más de 'n' caracteres.
    Parámetros:
    lista_palabras: Lista de palabras (cadenas de texto).
    n: Número entero que define el límite de caracteres.
    
    Devuelve:
    Lista de palabras que tienen más de 'n' caracteres.
    """
    return [palabra for palabra in lista_palabras if len(palabra) > n]

# Ejemplo de uso
palabras = ["perro", "gato", "elefante", "caballo"]
print(filtrar_palabras(palabras, 5))  # Output: ['elefante', 'caballo']
