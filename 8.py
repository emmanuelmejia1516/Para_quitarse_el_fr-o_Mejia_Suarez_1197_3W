def contar_nombres_con_letra(nombres, letra):
    """
    Esta función cuenta cuántos nombres en una lista comienzan con una letra específica.
    Parámetros:
    nombres: Lista de nombres (cadenas de texto).
    letra: Letra que se busca al principio de los nombres.
    
    Devuelve:
    El número de nombres que comienzan con la letra proporcionada.
    """
    return sum(1 for nombre in nombres if nombre.lower().startswith(letra.lower()))

# Ejemplo de uso
nombres = ["Ana", "Beatriz", "Carlos", "Alejandra", "Antonio"]
letra = input("Ingrese una letra: ")
print(f"Cantidad de nombres que comienzan con '{letra}': {contar_nombres_con_letra(nombres, letra)}")
