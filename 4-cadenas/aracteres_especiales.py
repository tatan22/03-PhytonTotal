'''
Caracteres especiales en cadenas de texto
Las cadenas pueden incluir caracteres especiales

Estos caracteres se introducen usando el carácter de escape o barra invertida `\` (backslash).
    * Nueva línea: `\n` -> Inserta un salto de línea.
    * Tabulación: `\t` -> Inserta un tabulador.
    * Comillas simples: `\'` -> Permite incluir comillas simples dentro de una cadena delimitada por comillas simples.
    * Comillas dobles: `\"` -> Permite incluir comillas dobles dentro de una cadena delimitada por comillas dobles.
    * Barra invertida: `\\` -> Permite incluir una barra invertida dentro de una cadena.
    * Carácter nulo: `\0` -> Representa el carácter nulo, que no se muestra pero puede ser útil en ciertas situaciones.
'''
cadena1 = "Hola, mundo"
cadena2 = "Hola,\nmundo"  # Nueva línea
cadena3 = "Hola,\tmundo"  # Tabulación
cadena4 = "Hola, 'mundo'"  # Comillas simples
cadena5 = "Hola, \"mundo\""  # Comillas dobles
cadena6 = "Hola, \\mundo"  # Barra invertida
cadena7 = "Hola, \0mundo"  # Carácter nulo
cadena8 = "Hola, 'mundo'" # Comillas simples
cadena9 = 'Hola, "mundo"'# Comillas dobles
# cadena10 = "Hola, \ mundo"  # carater de escape, lanza error de sintaxis
print(cadena1)
print(cadena2)
print(cadena3)
print(cadena4)
print(cadena5)
print(cadena6)
print(cadena7)
print(cadena8)
print(cadena9)




