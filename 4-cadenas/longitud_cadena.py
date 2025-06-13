'''
Obtebner la longitud de una cadena de caracteres.
    La longitud de una cadena se puede obtener utilizando la función `len()`,
    que devuelve el número de caracteres en la cadena.
    La funcion len() es una función con varios tipos de datos incluyendo cadenas, listas, tuplas
    y diccionarios.
    Cuando se calcula la longitud de una cadena se toman en cuanta todos los caracteres, de una
    cadena , incluyendo espacios, signos de puntuación y caracteres especiales etc.
    cadena = "Hola Mundo"
    longitud = len(cadena1) ->Devuelve largo de 12
'''
#Largo de una cadena
cadena1 = "Hola, Mundo!"
longitud = len(cadena1)
print(f'La longitud de la cadena "{cadena1}" es: {longitud}')  # Salida: La longitud de la cadena "Hola, Mundo!" es: 13