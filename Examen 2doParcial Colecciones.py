alumnos = ["Ana", "Luis", "Paty"]
calificaciones = [9.0, 7.5, 8.2]

#Acceder por índice (desde 0)
print(alumnos[0]) #"Ana"
print(alumnos[-1]) #"Paty"

#Agregar y eliminar
alumnos.append("carlos")
alumnos.remove("Luis")

#Longitud
print(len(alumnos)) #3

#Recorrer
for a in alumnos:
    print(a)