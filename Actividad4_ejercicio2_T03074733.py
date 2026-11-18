print("Ejercicio 2: ¿Quién paga el flete y el seguro?")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Pedimos los datos del contrato
incoterm = input("Escribe el Incoterm en MAYÚSCULAS (EXW, FOB, CIF, CIP, DAP): ")
valor = float(input("Valor de la mercancía en dólares: "))
transporte = input("Transporte en MAYÚSCULAS (MARITIMO, AEREO, TERRESTRE): ")
fragil = input("¿La mercancía es frágil? (si/no): ")

# Convertimos la respuesta en True o False
es_fragil = fragil == "si"

print()
print("===== RESUMEN DEL CONTRATO =====")

# Verificamos que el Incoterm sea válido
if not (incoterm == "EXW" or incoterm == "FOB" or incoterm == "CIF" or incoterm == "CIP" or incoterm == "DAP"):
    print("❌ Incoterm no válido. Revisa que esté en MAYÚSCULAS.")

else:

    # Determinar quién paga el flete
    if incoterm == "EXW" or incoterm == "FOB":
        print("🚚 Flete internacional: lo paga el COMPRADOR.")
    else:
        print("🚚 Flete internacional: lo paga el VENDEDOR.")

    # Determinar quién contrata el seguro
    if incoterm == "CIF" or incoterm == "CIP":

        if es_fragil or transporte == "MARITIMO":
            porcentaje = 2
        else:
            porcentaje = 1

        seguro = valor * porcentaje / 100

        print("✅ Seguro: lo contrata el VENDEDOR.")
        print("Porcentaje del seguro: ", porcentaje, "%", sep="")
        print("Costo estimado del seguro: $", seguro, sep="")

    else:
        print("📦 Seguro: NO lo contrata el vendedor. Lo decide el COMPRADOR.")