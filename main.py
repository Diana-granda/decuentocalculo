def compra(producto,precio):
    print(f"Buenos días usted quiere comprar una {producto} con un precio de {precio} dolares.")
compra("moto yamaha zr", 2490)
compra("cocina", 250)

def calcular_descuento(producto, precio):
    descuento = precio * 0.1  # Supongamos un descuento del 15%
    precio_con_descuento = precio - descuento
    print(f"Tenemos una {producto} con un precio original de ${precio:.2f} dolares.")
    print(f"Si usted la compra ahora le ayudamos con un descuento del 15%, el precio final es de ${precio_con_descuento:.2f} dolares.")
calcular_descuento("moto yamaha zr", 2490)
calcular_descuento("cocina", 250)