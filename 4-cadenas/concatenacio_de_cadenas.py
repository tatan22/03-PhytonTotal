'''
Concatenació de cadenes
La concatenacion de cadenas es una operación que permite combinar dos o mas cadenas para formar
una nueva cadena
En Python existen varias formas, vamos a ver varias de ellas:

'''
# Concatenación con el operador +
concatenacion = 'Hola' + ' ' + 'mundo'
print(concatenacion)  # Salida: Hola mundo

# Concatenación con el método join
cadenas = ['Hola', 'mundo']
concatenacion_join = ' '.join(cadenas)
print(concatenacion_join)  # Salida: Hola mundo

# Concatenación con el operador % (antigua)
nombre_porcentaje = 'mundo'
concatenacion_porcentaje = 'Hola %s' % nombre_porcentaje
print(concatenacion_porcentaje)  # Salida: Hola mundo

# Concatenación con el operador +=
cadena = 'Hola'
cadena += ' mundo'
print(cadena)  # Salida: Hola mundo








