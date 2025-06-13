'''
Inmutabilidad en cadenas de texto
    Una vez que se creada una cadena, los caracteres dentroi de ella no pueden ser modificados.
    Si deseamos modificar una cadena, entonces tenemos que crear una nueva cadena.
    Las cadenas no se pueden modificar directamente, pero podemos crear una nueva cadena basada en la original con los cambios deseados.
'''
cadena1 = "Hola, mundo"
# cadena1[0] = "h"  # Esto generará un error porque las cadenas son inmutables
cadena2 = cadena1 # pero no estamos modificando la cadena original, simplemente estamos creando una nueva referencia a la misma cadena.
cadena1 = 'Adios' # Esto es válido, ya que estamos creando una nueva cadena,

