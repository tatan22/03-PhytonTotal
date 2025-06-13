'''
Metodos de cadenas
las cadenas en python viene con una serie de metodos Utiles que facilitan su manipulacion
por Ejemplo:
- `upper()`: Convierte todos los caracteres de la cadena a mayúsculas.
- `lower()`: Convierte todos los caracteres de la cadena a minúsculas.
- `strip()`: Elimina los espacios en blanco al principio y al final de la cadena.
'''
# Ejemplo de uso de los métodos de cadenas
cadena = "  Hola Mundo  "

# Convertir a mayúsculas
# todos los metodos de cadenas devuelven una nueva cadena, no modifican la original
cadena_mayusculas = cadena.upper()
print(f'Cadena Original:{cadena_mayusculas}')  # Salida: "  Hola Mundo  "
print(f'Cadena en Mayusculas:{cadena_mayusculas}')  # Salida: "  HOLA MUNDO  "

# Convertir a minúsculas
cadena_minusculas = cadena.lower()
print(f'Cadena en Minusculas:{cadena_minusculas}')  # Salida: "  hola mundo  "

# Eliminar espacios en blanco al principio y al final
cadena_strip = cadena.strip()
print(f'Cadena sin espacios:{cadena_strip}')  # Salida: "Hola Mundo"
