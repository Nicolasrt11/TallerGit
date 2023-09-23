"""
Fecha : 20/09/2023
Autor: Nicolas Tapasco -- Zedvien Daniel Elias Vasquez Martinez -- Mayra Alejandra Franco Castaño
Objetivo: Se requiere un software que calcule si un aprendiz tiene el estilo de aprendizaje Asimilador.
Para ello deben realizarse 7 preguntas de respuesta SI o NO. Si el aprendiz obtuvo 4 o más respuestas
en SI entonces el sistema deberá indicarle que es Asimilador, de lo contrario le dirá que su estilo de aprendizaje es otro."""

print("Hola bienvenido al tesd de estilo de aprendizaje \n Responde \n Si = 1 \n No = 2")

question = int(input("Cuando aprendes algo nuevo, ¿prefieres que te presenten teorías o conceptos antes que ejemplos prácticos? :"))
qualification = 0
if question == 1:
    qualification += 1
while question != 1 and question != 2:
    question = int(input("Opcion incorecta intente de nuevo: "))
    if question == 1:
         qualification += 1

question = int(input("¿Te sientes más cómodo aprendiendo a través de la lectura de libros o materiales escritos? :"))
if question == 1:
    qualification += 1
while question != 1 and question != 2:
    question = int(input("Opcion incorecta intente de nuevo: "))
    if question == 1:
         qualification += 1

question = int(input("¿Encuentras útil hacer esquemas, resúmenes o diagramas para organizar la información que estás aprendiendo? :"))
if question == 1:
    qualification += 1
while question != 1 and question != 2:
    question = int(input("Opcion incorecta intente de nuevo: "))
    if question == 1:
         qualification += 1

question = int(input("¿Te gusta analizar y reflexionar sobre las ideas y conceptos antes de ponerlos en práctica? :"))
if question == 1:
    qualification += 1
while question != 1 and question != 2:
    question = int(input("Opcion incorecta intente de nuevo: "))
    if question == 1:
         qualification += 1

question = int(input("¿Tienes tendencia a destacar en asignaturas que requieren comprensión de teorías y conceptos, como las matemáticas o la física? :"))
if question == 1:
    qualification += 1
while question != 1 and question != 2:
    question = int(input("Opcion incorecta intente de nuevo: "))
    if question == 1:
         qualification += 1

question = int(input("¿Te sientes más cómodo en entornos de aprendizaje estructurados, como conferencias o clases magistrales? :"))
if question == 1:
    qualification += 1
while question != 1 and question != 2:
    question = int(input("Opcion incorecta intente de nuevo: "))
    if question == 1:
         qualification += 1

question = int(input("¿Prefieres aprender de manera independiente en lugar de trabajar en grupos o equipos? :"))
if question == 1:
    qualification += 1
while question != 1 and question != 2:
    question = int(input("Opcion incorecta intente de nuevo: "))
    if question == 1:
         qualification += 1

if qualification >= 4:
    print("tu estilo de aprendizaje es asimilador y tu calificacion es :", qualification) 
else :
    print("Tu estilo de aprendizaje es otro")
