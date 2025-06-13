''''
Cadenas de caracteres en Python
    Cadenas de caracteres son secuencias de caracteres que se utilizan para representar texto.
    Cadenas se pueden crear utilizando comillas simples (' ') o dobles (" ").
    Cadenas son inmutables, lo que significa que no se pueden cambiar una vez creadas.
    Los caracteres puedes ser letras, números, espacios y símbolos.
'''
# Sintaxis para declarar una cadena de caracteres
# NOMBRE_CADENA = "valor de la cadena"

print('Cadenas de caracteres en Python')
# Ejemplo de cadenas de caracteres
cadena1 = "Hola, mundo!"  # Usando comillas dobles
cadena2 = 'Python es genial.'  # Usando comillas simples
cadena3 = '''Este es un ejemplo de una cadena 
    de varias líneas 
        en una cadena.'''  # Usando comillas triples, tambien respeta saltos de línea y tabulaciones

# imprimir cadenas
print(cadena1)
print(cadena2)
print(cadena3)

nombre = "Juan"
apellido = 'Pérez'
mensaje = "Hola, " + nombre + " " + apellido + "!"  # Concatenación de cadenas