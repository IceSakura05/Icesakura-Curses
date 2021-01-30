# Variable es un nombre simbolico para un valor.
# Una variable es un sitio donde guardamos una determinada información.
# Cualquier tipo de dato (String --> Booleano, Integrer, ...)se puede guardar en una variable.
# Aprenderemos la base de la variables.
name = "Icesakura"
print(10 + 100)
print (name)

# Las Variables puede diferenciar -->(Case sensitive)
# Si se pone mayucula o minuscula, la variable distingue que son cosas diferentes.
# No es valido la siguiente forma de definir un variable.
# 2loquesea = "lo que sea"

# Es valido la siguiente:
# loquesea = "lo que sea"
# _loquesea = "lo que sea"
# _2loquesea = "lo que sea"
# loquesea_loquesea = "lo que sea" -->
book1 = "Digital Fortress"
Book2 = "Digital Fortrees"

# Para no andar definiendo variables sueltos, podemos hacer lo siguiente:
x, book = 100, "Digital Fortrees"
print(x)
print(book)
print(x, book)

# Convenciones --> Forma de escribir los programadores para ser mas sencillo de leer si es mas largo.(recomendacion a mencionar)
# Mas comunes la primera y segunda, pero todas son validas.
book_name = "lo que sea" # Snake Case
bookName = "lo que sea" # Camel Case
BookName = "lo que sea" # Pascal Case

# Valor que no se cambia --> (Constante)
# Escribir todo en mayuscula (depende del lenguaje puede ser mas estrico o no)
PI = 3.1416
MY_NAME = "Icesakura"

# Variables son dinamicos y se puede reasignar (al menos en Python)
# Otros lenguajes son diferentes

book_name = "lo que sea"
book_name = 1234123

# Pasar al siguiente archivo llamado tipodedatosV2.py