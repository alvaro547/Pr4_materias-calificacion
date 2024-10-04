print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Definimos una lista que contiene las materias del curso
materias = [
    "Pensamiento matemático",
    "Español",
    "Inglés",
    "Química",
    "Civismo",
    "Francés"
]

# Función para solicitar calificaciones y mostrar el mensaje
def mostrar_calificaciones(lista_materias):
    # Creamos un diccionario para almacenar las calificaciones
    calificaciones = {}
    
    # Iteramos sobre cada materia en la lista
    for materia in lista_materias:
        # Pedimos al usuario que ingrese la calificación para cada materia
        calificacion = input(f"Ingrese la calificación para {materia}: ")
        # Almacenamos la calificación en el diccionario
        calificaciones[materia] = calificacion

    # Mostramos las calificaciones
    for materia, calificacion in calificaciones.items():
        print(f"En {materia} has obtenido {calificacion}")

# Llamamos a la función para solicitar calificaciones y mostrar los resultados
mostrar_calificaciones(materias)
