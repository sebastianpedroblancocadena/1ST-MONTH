#EJERCICIO 1
estudiantes = ["juan", "lopez", "martin"]
print("Original:", estudiantes)

estudiantes.insert(1, "maria")
print("Después de insert(1, 'maria'):", estudiantes)

estudiantes.remove("lopez")
print("Después de remove('lopez'):", estudiantes)

eliminado = estudiantes.pop(1)
print(f"Elemento eliminado con pop(1): {eliminado}")
print("Lista después de pop:", estudiantes)

posicion = estudiantes.index("juan")
print(f"'juan' está en el índice {posicion}")

print("¿'Ana' está?", "Ana" in estudiantes)
print("¿'martin' está?", "martin" in estudiantes)

eli2 = estudiantes.pop()
print(estudiantes)

#EJERCICIO 2
letras = ["a","b","c","d"]
letras.insert(0, "x")
letras.append("z")
print(len(letras))
letras.remove("c")
ultimo = letras.pop(-1)

print(f"lista: {letras}, el elemento eliminado: {ultimo}.")

#EJERCICIO 3
pila = []
while True:
  nombres = input(">>instrucciones(+ agregar, - atender, salir): ")
  if nombres == "salir":
    break
  elif nombres == "+":
    name = input(">>>INGRESE NOMBRE: ")
    pila.append(name)
  elif nombres == "-":
    if pila:
      atendido = pila.pop()
      print(f"Atendiendo a: {atendido}")
    else:
      print("no hay nadie en la pila")
print("quedan:", (len(pila)))

#EJERCICIO 4
fila = ["carlos","ana","pedro"]
fila.insert(0, "sebastian")
fila.pop()
print(fila)

"""1. ¿Qué diferencia hay entre remove() y pop()?:
  remove elima el primer digito con el valor o el unico, mientras que pop lo puedes usar para seleccionar el lugar(indice) y el valor.
2. ¿Qué devuelve pop() cuando lo usas?:
  me devuelve el valor que elimine.
3. ¿Cómo insertas un elemento al principio de una lista?:
  con .insert(0, "elemento")
4. ¿Para qué sirve elemento in lista?:
  para ver si pertenece a la variable o a lo que se pide, es bool, te lo podria devolver con true, false
"""
