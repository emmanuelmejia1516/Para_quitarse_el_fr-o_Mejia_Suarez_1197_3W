def calcular_edades():
    """
    Esta función calcula cuántos años cumplirá cada persona durante el año en curso.
    """
    anio_actual = int(input("Ingresa el año en curso: "))
    
    personas = []
    for i in range(3):
        nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
        anio_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
        edad = anio_actual - anio_nacimiento
        personas.append(f"{nombre} cumplirá {edad} años en {anio_actual}.")
    
    for persona in personas:
        print(persona)

# Ejemplo de uso
calcular_edades()
