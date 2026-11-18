print("Ejercicio 12: Precios del Buen Fin")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Catálogo
productos = ["Café", "Tequila", "Miel", "Mezcal", "Cacao"]
precios = [450, 1200, 300, 980, 150]

# Pedimos los datos
descuento = float(input("Porcentaje de descuento del Buen Fin: "))
consulta = input("¿Qué producto quiere consultar el cliente?: ")

# 1. Copia real de precios
promocion = precios[:]

# Aplicamos el descuento
for i in range(len(promocion)):
    promocion[i] = promocion[i] - promocion[i] * descuento / 100

# 2. Primeros 3 productos en promoción
productos_promo = productos[:3]

# 3. Borrar precios desde la posición 3 hasta el final
del promocion[3:]

print()
print("===== PRECIOS DEL BUEN FIN =====")
print("Productos en promoción:", productos_promo)
print("Precios originales:", precios)
print("Precios con descuento:", promocion)

# 4. Buscar el producto más caro de la promoción
mayor = promocion[0]
pos_mayor = 0

for i in range(len(promocion)):
    if promocion[i] > mayor:
        mayor = promocion[i]
        pos_mayor = i

print("⭐ El producto en promoción más caro es",
      productos_promo[pos_mayor], "a $", mayor)

print()
print("===== CONSULTA DEL CLIENTE =====")

# 5. Si el producto no está en el catálogo
if consulta not in productos:
    print("❌", consulta, "no está en nuestro catálogo.")
else:
    pos = -1

    for i in range(len(productos)):
        if productos[i] == consulta:
            pos = i

    print("Precio normal de", consulta, ": $", precios[pos], sep="")

    # 6. Revisar si está en promoción
    if consulta in productos_promo:
        print("🎉 Precio Buen Fin: $", promocion[pos], sep="")
    else:
        print("🏷️", consulta, "no entra a la promoción. Se cobra el precio normal.")