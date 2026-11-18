print("Ejercicio 11: Revisión de pedido y reporte de ventas")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Listas de la empresa
catalogo = ["CAFE", "TEQUILA", "MIEL", "AGUACATE", "CHOCOLATE"]
restringidos = ["MERCURIO", "PIROTECNIA", "ACIDO SULFURICO"]
paises_tmec = ["MEXICO", "ESTADOS UNIDOS", "CANADA"]

# Ventas del cliente de enero a junio
ventas = [135, 110, 145, 170, 125, 190]

# Pedimos los datos del pedido
producto = input("Producto en MAYÚSCULAS y sin acento: ")
pais = input("País destino en MAYÚSCULAS y sin acento: ")
meses = int(input("¿Cuántos meses quieres en el reporte? (1 a 6): "))

print()
print("===== REVISIÓN DEL PEDIDO =====")

# not in: valida catálogo
if producto not in catalogo:
    print("❌", producto, "no está en nuestro catálogo.")
else:
    # in: valida restringidos
    if producto in restringidos:
        print("🛑", producto, "requiere permiso especial.")
    else:
        print("✅", producto, "se puede exportar.")

    # in: valida T-MEC
    if pais in paises_tmec:
        print("🌎", pais, "pertenece al T-MEC. Arancel 0%.")
    else:
        print("📄", pais, "no pertenece al T-MEC.")

print()
print("===== REPORTE DE VENTAS =====")

# or: validar rango
if meses < 1 or meses > 6:
    print("❌ Captura un número entre 1 y 6.")
else:
    print("Primeros", meses, "meses:", ventas[:meses])
    print("Últimos", meses, "meses:", ventas[-meses:])
    print("Primer trimestre:", ventas[0:3])
    print("Segundo trimestre:", ventas[3:6])