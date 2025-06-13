'''
Formato de cadena en Python
El formato de cadena en Python permite insertar valores dentro de una cadena de texto de manera
controlada y legible. Existen varias formas de formatear cadenas, aquí veremos algunas de las más comunes:

'''
# Formato de cadena con f-strings (Python 3.6+)
nombre = 'mundo'
formato_fstring = f'Hola {nombre}'
print(formato_fstring)  # Salida: Hola mundo

# Concatenación con el método format
nombre_format = 'mundo'
concatenacion_format = 'Hola {}'.format(nombre_format)
print(concatenacion_format)  # Salida: Hola mundo

# Concatenación con el método append (para listas)
lista_cadenas = ['Hola']
lista_cadenas.append('mundo')
concatenacion_append = ' '.join(lista_cadenas)
print(concatenacion_append)  # Salida: Hola mundo

# Concatenación con el método extend (para listas)
lista_cadenas_extend = ['Hola']
lista_cadenas_extend.extend(['mundo'])
concatenacion_extend = ' '.join(lista_cadenas_extend)
print(concatenacion_extend)  # Salida: Hola mundo

