''''
 Constantes en Python
    Constantes son valores que no cambian durante la ejecución del programa.
    En Python, no hay una forma de declarar constantes como en otros lenguajes,
    pero se pueden simular utilizando convenciones de nomenclatura.
    Por convención, se utilizan nombres en mayúsculas para indicar que una variable es una constante.
    Por ejemplo, PI es una constante que representa el valor de pi.
'''
import math
#sintax para declarar una constante
# NOMBRE_CONSTANTE = valor
#Ejemplo de constantes
print('Constantes en Python')
PI = 3.14159
NOMBRE_BASE_DATOS = "mi_base_de_datos.db"
MENSAJE_BIENVENIDA = "¡Bienvenido al programa!"
NOMBRE_USUARIO_VALIDO = "Admin"

#No se recomienda cambiar el valor de una constante
# Usar una constante del lenguaje Python, aunque en este caso no está en mayúsculas
print('Valor de math.pi:', math.pi)