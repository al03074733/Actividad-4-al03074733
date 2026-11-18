print("Ejercicio 14: Ranking de vendedores del mes")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Cada vendedor tiene su venta en la MISMA posición (miles de pesos)
vendedores = ["Sara", "Mario", "Mariana", "Josue", "Lili"]
ventas = [76, 134, 67, 54, 23]
total_vendedores = len(ventas)

print("Ventas como vienen en el reporte:", ventas)

# 1. for de afuera: ¿cuántas vueltas se dan como máximo?
for vuelta in range(total_vendedores - 1):

    # 2. for de adentro: cada vuelta compara una vez menos
    for lugar in range(total_vendedores - 1 - vuelta):

        venta_izquierda = ventas[lugar]
        venta_derecha = ventas[lugar + 1]

        # 3. Queremos de MAYOR a MENOR: ¿cuándo están al revés?
        if venta_izquierda < venta_derecha:

            # Cambiamos de lugar las ventas
            ventas[lugar] = venta_derecha
            ventas[lugar + 1] = venta_izquierda

            # 4. Cambiamos también a los vendedores,
            # para que cada uno siga con su venta
            vendedor_izquierda = vendedores[lugar]
            vendedor_derecha = vendedores[lugar + 1]

            vendedores[lugar] = vendedor_derecha
            vendedores[lugar + 1] = vendedor_izquierda

    print("Después de la vuelta", vuelta + 1, "las ventas quedan:", ventas)

print()
print("===== RANKING DEL MES =====")
for lugar in range(total_vendedores):

    # 5. Solo los 3 primeros lugares ganan bono
    if lugar < 3:
        print(lugar + 1, vendedores[lugar], ventas[lugar], "mil 🏆 Gana bono")
    else:
        print(lugar + 1, vendedores[lugar], ventas[lugar], "mil")