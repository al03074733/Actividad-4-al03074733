print("Ejercicio 1: Liberación de embarque en aduana")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Preguntamos por los 4 documentos y revisiones de la aduana
factura = input("¿Tienes la factura comercial? (si/no): ")
pedimento = input("¿Tienes el pedimento de importación? (si/no): ")
impuestos = input("¿Ya pagaste los impuestos? (si/no): ")
coincide = input("¿La mercancía coincide con lo declarado? (si/no): ")
valor = float(input("Valor de la mercancía en dólares: "))

# Convertimos cada respuesta en True o False
tiene_factura = factura == "si"
tiene_pedimento = pedimento == "si"
impuestos_pagados = impuestos == "si"
mercancia_ok = coincide == "si"

print()
print("===== RESULTADO DE LA ADUANA =====")

# Los cuatro requisitos deben cumplirse
if tiene_factura and tiene_pedimento and impuestos_pagados and mercancia_ok:

    print("✅ Embarque liberado. Puede salir de la aduana.")

    # Si el valor es mayor a 100000, avisar al gerente
    if valor > 100000:
        print("📢 Embarque de alto valor: avisa al gerente de logística.")

else:

    print("🔴 Embarque detenido. Faltan estos requisitos:")

    faltantes = 0

    if not tiene_factura:
        print(" - Factura comercial")
        faltantes += 1

    if not tiene_pedimento:
        print(" - Pedimento de importación")
        faltantes += 1

    if not impuestos_pagados:
        print(" - Pago de impuestos")
        faltantes += 1

    if not mercancia_ok:
        print(" - La mercancía no coincide con lo declarado")
        faltantes += 1

    print("Total de requisitos pendientes:", faltantes)