# Numeros enteros (Integrer)
10
print(type(10))

# Numeros decimales --> (float)
10.5
print (type(10.5))

# Imput toma un valor que usuario mete. En ese caso lo guardo en en variable para que mas tarde se imprima en la pantalla.
# Todo lo que se interta en un programa es un string. 
# Si hay que convertir en un tipo de dato a otro, se tiene que hacer el  paso de conversion que solo es poner el tipo de dato delate y el dato en parentesis.
# No se puede poner un texto cualquiera para que se pase a un tipo de dato.
age = input("Inserta tu edad: ")
print(type(age))
new_age = int(age) + 5
print(new_age)

# Pasar al siguiente archivo llamado lista.py