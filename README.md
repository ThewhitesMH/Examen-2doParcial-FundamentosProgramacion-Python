Examen Parcial 2 - Fundamentos de Programacion

Instituto Tecnológico de Celaya
Profesor: Ing. Luis Gerardo López Ruiz
Fecha de entrega: 11 de Octubre del 2026

Este repositorio contiene la documentación y replicación en Python de todos los ejemplos de las diapositivas de clase, así como la práctica integradora, en sustitución del examen formal

Equipo de Trabajo:
- [Ramirez Leon Emanuel]
- [Bernal Jimenez Jose Julian]
- [Graincourt Lizardi Juan Rafael]
- [Gutierrez Almaguer Oscar]

Contenido del Repositorio:

El código está estructurado y documentado siguiendo el orden del material proporcionado

Los scripts cubren los siguientes temas:

1. Tipos de Datos y Operadores
- Números y Casteo: Uso de int, float, complex, conversión entre tipos y generación de aleatorios con random
- Booleanos y None: Evaluación de valores lógicos (True/False), casteo con bool() y validación del tipo de dato NoneType.
- Operadores: Ejemplos prácticos de operadores aritméticos (+, -, %, //, **), de asignación (incluyendo el operador walrus :=) y operadores lógicos (and, or, not).

2. Manejo de Strings
- Métodos de cadenas de texto (upper, lower, strip, replace, split)
- Búsquedas booleanas (in, not in), conteo de longitud (len) y técnicas de slicing con índices positivos y negativos

3. Colecciones en Python
- Listas: Colecciones ordenadas y mutables. Uso de append, insert, remove, pop y sort
- Tuplas: Colecciones ordenadas e inmutables, desempaquetado de variables y concatenación(end_span).
- Conjuntos / Sets: Colecciones no ordenadas sin duplicados, operaciones de unión, intersección y diferencia
- Diccionarios: Estructuras estructuradas, acceso seguro con get(), modificación e iteración con items().

4. Control de Flujo y Entrada de Datos
- Interacción (input): Captura de datos desde consola y casteo directo (int(), float(), str())
- Ciclo for: Iteraciones sobre secuencias con range(), bucles anidados y uso de sentencias de control (break, continue, pass)

Práctica Final: Calculadora Simple

El repositorio incluye el script final que integra los conocimientos de la clase
1. Captura el nombre de un alumno (o un ex) y solicita 3 calificaciones consecutivas
2. Convierte las entradas a float y las almacena en una lista
3. Calcula el promedio general mediante sum() y len()
4. Imprime el resumen de los datos e indica mediante condicionales si el usuario Aprobó (mayor o igual a 6.0) o Reprobó
