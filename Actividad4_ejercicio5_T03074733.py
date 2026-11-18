print("Ejercicio 5: Cálculo de impuestos con el T-MEC")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Pedimos los datos de la mercancía
pais = input("País de origen en MAYÚSCULAS y sin acento (MEXICO, ESTADOS UNIDOS, CANADA, CHINA...): ")
certificado = input("¿Tienes certificado de origen? (si/no): ")
valor = float(input("Valor de la mercancía en dólares: "))

# 1. Convierte la respuesta del certificado en True o False
tiene_certificado = certificado == "si"

print()
print("===== CÁLCULO DE IMPUESTOS DE IMPORTACIÓN =====")

# 2. Si el país es MEXICO, la mercancía es nacional y no se importa
if pais == "MEXICO":
    print("MX Es mercancía nacional. No paga impuestos de importación.")

else:

    # 3. Condición del T-MEC
    if (pais == "ESTADOS UNIDOS" or pais == "CANADA") and tiene_certificado:

        # 4. Arancel con T-MEC
        arancel = 0

        print("✅ Aplica el trato preferencial del T-MEC.")

    else:

        # 5. Arancel sin T-MEC
        arancel = 15

        print("🔴 No aplica el trato preferencial. Se cobra el arancel general.")

    # 6. Calcula el impuesto del arancel
    impuesto_arancel = valor * arancel / 100

    # 7. IVA = 16% de (valor + impuesto del arancel)
    iva = (valor + impuesto_arancel) * 0.16

    # 8. Total a pagar
    total = valor + impuesto_arancel + iva

    print("Arancel: ", arancel, "%", sep="")
    print("Impuesto del arancel: $", impuesto_arancel, sep="")
    print("IVA: $", iva, sep="")
    print("Total a pagar: $", total, sep="")

    # 9. Aviso de ahorro
    if (pais == "ESTADOS UNIDOS" or pais == "CANADA") and not tiene_certificado:
        ahorro = valor * 15 / 100
        print("💡 Con certificado de origen te habrías ahorrado en arancel: $", ahorro, sep="")