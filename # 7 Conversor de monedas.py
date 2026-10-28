"""
Programa: Conversor de Monedas
Convierte una cantidad de pesos mexicanos a diferentes monedas.
"""

# --- CONSTANTES ---
# Moneda (Equivalente de 1 MXN en cada divisa)
M_USD = 0.050    # 1. Dólar (USD)
M_EUR = 0.047    # 2. Euro (EUR)
M_THB = 1.680    # 3. Baht (THB)
M_JPY = 7.650    # 4. Yen (JPY)
M_KRW = 69.50    # 5. Won (KRW)
M_AUD = 0.076    # 6. Dólar Australiano (AUD)
M_PEN = 0.185    # 7. Sol (PEN)
M_CAD = 0.069    # 8. Dólar Canadiense (CAD)
M_VES = 1.830    # 9. Bolívar (VES)
M_ARS = 49.30    # 10. Peso Argentino (ARS)

# Límites de opciones
OPCION_MINIMA = 1
OPCION_MAXIMA = 10

# --- ENTRADA DE DATOS ---
print("--- Conversor de Monedas (Desde MXN) ---")
pesos_mxn = float(input("Ingresa la cantidad en pesos mexicanos (MXN): $"))

# Menú de opciones de conversión para el usuario
print("\nSelecciona la moneda a la que deseas convertir:")
print("1. Dólar (USD)")
print("2. Euro (EUR)")
print("3. Baht (THB)")
print("4. Yen (JPY)")
print("5. Won (KRW)")
print("6. Dólar Australiano (AUD)")
print("7. Sol (PEN)")
print("8. Dólar Canadiense (CAD)")
print("9. Bolívar (VES)")
print("10. Peso Argentino (ARS)")
opcion = int(input(f"Ingresa el número de tu opción \
    ({OPCION_MINIMA}-{OPCION_MAXIMA}): "))

if pesos_mxn <= 0:
    valido = False
    error_msg = "La cantidad a convertir debe ser mayor a cero."
else:
    match opcion:
        case 1:
            resultado = pesos_mxn * M_USD
            moneda = "USD (Dólares)"
            valido = True
        case 2:
            resultado = pesos_mxn * M_EUR
            moneda = "EUR (Euros)"
            valido = True
        case 3:
            resultado = pesos_mxn * M_THB
            moneda = "THB (Bahts)"
            valido = True
        case 4:
            resultado = pesos_mxn * M_JPY
            moneda = "JPY (Yenes)"
            valido = True
        case 5:
            resultado = pesos_mxn * M_KRW
            moneda = "KRW (Wons)"
            valido = True
        case 6:
            resultado = pesos_mxn * M_AUD
            moneda = "AUD (Dólares Australianos)"
            valido = True
        case 7:
            resultado = pesos_mxn * M_PEN
            moneda = "PEN (Soles)"
            valido = True
        case 8:
            resultado = pesos_mxn * M_CAD
            moneda = "CAD (Dólares Canadienses)"
            valido = True
        case 9:
            resultado = pesos_mxn * M_VES
            moneda = "VES (Bolívares)"
            valido = True
        case 10:
            resultado = pesos_mxn * M_ARS
            moneda = "ARS (Pesos Argentinos)"
            valido = True
        case _:
            valido = False
            error_msg = f"La opción '{opcion}' no es válida. \
                Debes elegir un número del {OPCION_MINIMA} al {OPCION_MAXIMA}."

# --- SALIDA ---
if valido:
    print("\n--- Transacción Exitosa ---")
    print(f"Monto original: ${pesos_mxn:,.2f} MXN")
    print(f"Equivalente: {resultado:,.2f} {moneda}")
else:
    print(f"\n❌ Error: {error_msg}")