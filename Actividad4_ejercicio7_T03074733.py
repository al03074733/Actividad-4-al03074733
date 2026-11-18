print("Ejercicio 7: Zona de envío y costo del flete")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Pedimos los datos del pedido
pais = input("País destino en MAYÚSCULAS y sin acento: ")
kilos = float(input("Peso del pedido en kg: "))
frecuente = input("¿Es cliente frecuente? (si/no): ")
urgente = input("¿El pedido es urgente? (si/no): ")

# Convertimos las respuestas en True o False
es_frecuente = frecuente == "si"
es_urgente = urgente == "si"

print()
print("===== COTIZACIÓN DEL FLETE =====")

# Elegir zona usando OR
if pais == "ESTADOS UNIDOS" or pais == "CANADA":
    zona = "NORTEAMERICA"
    tarifa = 2

elif pais == "GUATEMALA" or pais == "COLOMBIA" or pais == "CHILE" or pais == "BRASIL":
    zona = "LATINOAMERICA"
    tarifa = 3

elif pais == "ALEMANIA" or pais == "FRANCIA" or pais == "ITALIA":
    zona = "EUROPA"
    tarifa = 5

else:
    zona = "SIN RUTA"
    tarifa = 0

if zona == "SIN RUTA":
    print("❌ No tenemos ruta de envío a", pais)

else:
    flete = kilos * tarifa

    print("Zona:", zona)
    print("Flete: $", flete, sep="")

    # Cargo especial
    if es_urgente or kilos > 1000:
        cargo = 500
    else:
        cargo = 0

    print("Cargo especial: $", cargo, sep="")

    subtotal = flete + cargo

    # Descuento
    if es_frecuente or subtotal > 5000:
        descuento = subtotal * 0.10
    else:
        descuento = 0

    print("Descuento: $", descuento, sep="")

    total = subtotal - descuento

    print("Total a pagar: $", total, sep="")