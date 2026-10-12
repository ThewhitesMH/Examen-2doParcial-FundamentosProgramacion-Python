nombre = input("Ingrese su nombre: ")
calificaciones = []
for i in range(3):
    calificacion = float(input(f"Ingrese la calificación {i+1}: "))
    calificaciones.append(calificacion)
    promedio = sum(calificaciones) / len(calificaciones)
    print("nombre: ", nombre)
    print("calificaciones: ", calificaciones)
    print("promedio: ", promedio)
    
    if promedio >= 6.0:
        print("Aprobado")
    else:
        print("Reprobado")