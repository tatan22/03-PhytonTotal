''''
Sistema de tienda online
crear el detalle de un producto de una tienda online.
El detalle del producto debe incluir:
* Nombre del producto
* Precio del producto
* Cantidad en el inventario
* Identifica si esta disponible o no

Hacer  algunaos cambios y mandar imprimir nuevamente el nuevo valor de las variables
'''
print('*** Sistema de Tienda Online ***\n ')
# Definimos las variables
nombre_producto = 'Laptop Gamer'
precio_producto = 1500.00
cantidad_inventario = 25
disponible = True

# Mostrar el detalle del producto
print('Producto:', nombre_producto)
print('Precio:$', precio_producto)
print('Cantidad en inventario:', cantidad_inventario)
print('Disponible:', disponible)

# Realizamos algunas modificaciones
nombre_producto = 'Smartphone'
precio_producto = 800.00

# Imprimir los cambios
print()
print('Producto:', nombre_producto)
print('Precio:$', precio_producto)
print('Cantidad en inventario:', cantidad_inventario)
print('Disponible:', disponible)  # La disponibilidad no ha cambiado

