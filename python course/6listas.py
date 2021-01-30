# Vamos aprender listas
# Se puede guardar listas dentro de una variable.
demo_list = [1, "hello", 1.5, True, [1, 2, 3]]
colors = ["rojo", "verde", "azul"]

# Las listas solo reconoce 1 argumento. Si queremos que reconozca mas, hay que agrupar dentro de un tipo de dato llamado tupla --> (tuple)
numbers_list = list((1, 2, 3, 4))
print(numbers_list)

# Crear una lista basada en rango
# En este caso solo imprime en la pantalla los valores dentro de 1 al 10 y no imprime el 10.
r = list(range(1, 10))
print(r)

# Obtener mas informacion de la lista. operaciones con las listas y muchas mas.
print(len(demo_list))
print(colors[2])
print(colors[-3])

# Saber si un dato esta dentro de un variable.
print("green" in colors) # En este caso esta en ingles.
print("verde" in colors)

# En las listas tambien se puede cambiar nombres.
# El numero 0 tambien cuenta como posicion.
print(colors)
colors[0] = "amarillo"
print(colors)

# Para añadir un dato usamos append.
colors.append("violeta")
print(colors)
# Para agregar varios datos.
# Toma solo un argumento y eso se soluciona con una tupla.
# Si para que se reconociera como dato separado, no funciona meterle dentro de una lista.