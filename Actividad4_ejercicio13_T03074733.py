print("Ejercicio 13: Cotizaciones de proveedores")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Presupuesto máximo autorizado
presupuesto = 5000

# Lista vacía para guardar las 5 cotizaciones
cotizaciones = []

for numero_de_cotizacion in range(5):
    precio_cotizado = int(input("Precio de la cotización: "))
    cotizaciones.append(precio_cotizado)

total_cotizaciones = len(cotizaciones)

print()
print("Cotizaciones como llegaron:", cotizaciones)

# Ordenamiento burbuja
for vuelta in range(total_cotizaciones - 1):

    for lugar in range(total_cotizaciones - 1 - vuelta):

        # Sacar copia de los dos precios antes de compararlos
        precio_izquierda = cotizaciones[lugar]
        precio_derecha = cotizaciones[lugar + 1]

        if precio_izquierda > precio_derecha:
            cotizaciones[lugar] = precio_derecha
            cotizaciones[lugar + 1] = precio_izquierda

    print("Después de la vuelta", vuelta + 1,
          "las cotizaciones quedan:", cotizaciones)

print()
print("Cotizaciones de la más barata a la más cara:", cotizaciones)
print("💰 La cotización más barata es:", cotizaciones[0])
print("💸 La cotización más cara es:", cotizaciones[-1])

# Revisar presupuesto
if cotizaciones[0] <= presupuesto:
    print("✅ Se aprueba la compra con la cotización de",
          cotizaciones[0])
else:
    print("🛑 Ninguna cotización cabe en el presupuesto. Pide nuevas cotizaciones.")