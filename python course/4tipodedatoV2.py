# Primero hay que ver el archivo variables.py primero.
# Vamos a ver mas a fondo los Strings,como operar con ello, etc.
# dir nos enseña que se puede hacer con cierto tipo de dato, para manipularlos.
# En este caso he creado un variable llamado myStr, puede ser con cualquier nombre que nosotros lo ponemos.
myStr = "hello World"

print(dir(myStr))

# Hay mas metodos para manipular dato, estos son ejemplos de ello:
# Poner todo en mayuscula.
print(myStr.upper())
# Poner todo en minsucula
print(myStr.lower())
# Poner una en mayuscula y otro en minuscula. Puede variar.
print(myStr.swapcase())
# Poner la inicial de la  letra en mayuscula.
print(myStr.capitalize())

# Para remplazar letra, hay que escribir exactamente la palabra original para poder remplazar.
# Metodos encadenados. 
# Sirve para definir un metodo despues de otro. Util a la hora de escribir codigo.
print(myStr.replace('hello', 'Bye').upper())
# Para contar cuantas letras se ha escrito. 
# Caracter vacio tambien cuenta.
print(myStr.count("o"))
print(myStr.count(" "))

# Contar si un caracter comienza por una palabra o terminar con otra palabra.
# Respuesta en booleano.
# Sabe diferenciar mayuscula o miniscula.
print(myStr.startswith("h"))
print(myStr.startswith("he"))
print(myStr.startswith("hello"))

print(myStr.endswith("w"))
print(myStr.endswith("wo"))
print(myStr.endswith("World"))

# Para dividir datos o variables.
# Separada por un espacio por defecto.
# Se puede definir nosotros como hay que separar.
# Estos se crea automaticamente en un tipo lista.
print(myStr.split("o"))

# Buscar una letra determinado de la posicion.
# Respuesta en numero.
# Tambien puede encontrar espacio en blanco.
print(myStr.find("o"))
print(myStr.find(" "))

# Para saber la longitud completa de la letra.
# Respuesta en numero.
print(len(myStr))

# Buscar el indice de un caracter.
# Cuenta todo desde cero, la primera que se encuntra es la 1.
# Respuesta en numero la posicion del caracter.
print(myStr.index("h"))

# Para saber si es numerico
print(myStr.isnumeric())
# para saber si es alphanumerico
print(myStr.isalpha())

# Para mostrar el caracter a partir de una posicion.
# El numero 0 tambien cuenta como posicion.!!
print(myStr[4])
print(myStr[6])

# Para mostrar el caracter a partir de una posicion inverso.
print(myStr[-2])
print(myStr[-3])

# La concatenacion tambien puede aplicar a variables y strings.
# Hay varias maneras de hacerlos:
# la segunda hay que poner f ya que hay una variable dentro{}, para que python pueda interpretar.

print("bro " + myStr)
print(f"Bro {myStr}") # Disponible Python 3.6 arriba.
print("Bro {0}".format(myStr))

# Pasar al siguiente archivo llamado numeros.py