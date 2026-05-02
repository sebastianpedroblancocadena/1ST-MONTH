#semana 2.1
#listas"
#ejercicio 1
tareas = ["gimnasio", "pesas", "estudiar"]
print("Lista original:", tareas)

print("Primera tarea:", tareas[0])
print("Última tarea:", tareas[-1])

tareas[-1] = "dormir" 
print("Lista modificada:", tareas)
# Agregar al final con append
tareas.append("despertar")
tareas.append("hola")
tareas.append("chao")
print("Lista final:", tareas)
print("Cantidad de tareas:", len(tareas))

#ejercicio 2
compras = []
compras.append("leche")
compras.append("huevos")
compras.append("pan")
print(compras[0])
print(compras[-1])
compras[2] = "mantequlla"
print(compras)
#ejercicio 3
numeros = [10,20,30,40,50]
suma = numeros[0] + numeros[-1]
print(suma)
numeros.insert(2,30)
numeros.append(60)
print("cantidad de numeros:", len(numeros))
print(numeros)
#ejercicio 4
gimnasio = ["pesas","mancuernas","barras","cuerda"]
print(gimnasio[0])
print(gimnasio[-1])
gimnasio[2] = "maquina"
gimnasio.append("espejo")
print(gimnasio)
#ejercicio 5
estudiantes = ["ana","luis","pedro"]
estudiantes.append("juan")
print("el primer estudiante en llegar fue:", estudiantes[0])
estudiantes[1] ="sofia"
print("el ultimo estudiante en llegar fue:", estudiantes[-1])
print(estudiantes)