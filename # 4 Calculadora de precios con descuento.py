"""
Programa: Calculadora de precios con descuento.
Calcula el precio final de un producto aplicando el descuento 
correspondiente según el precio original.
"""

# --- CONSTANTES ---
# Límites de precios
LIMITE_BAJO = 100.00
LIMITE_MEDIO = 200.00
LIMITE_ALTO = 500.00

# Porcentajes de descuento
DESC_CERO = 0.00
DESC_DIEZ = .10
DESC_VEINTE = .20
DESC_VEINTICINCO = .25

# --- ENTRADA DE DATOS --- 
print("--- Sistema de Cálculo de Descuentos ---")
precio_original = float(input("Ingresa el precio original del producto: $"))

# --- PROCESO ---
# Validación inicial: el precio debe ser mayor a cero
if precio_original <= 0:
    
    # --- SALIDA (Caso Error) ---
    print("\n❌ Error: El precio ingresado debe ser un número positivo mayor a cero.")

else:
    # Determinamos el descuento según los rangos establecidos
    if precio_original <= LIMITE_BAJO:
        porcentaje_desc = DESC_CERO
    elif precio_original <= LIMITE_MEDIO:
        porcentaje_desc = DESC_DIEZ
    elif precio_original <= LIMITE_ALTO:
        porcentaje_desc = DESC_VEINTE
    else:
        porcentaje_desc = DESC_VEINTICINCO

    # Cálculos finales
    monto_descuento = precio_original * porcentaje_desc
    precio_final = precio_original - monto_descuento

    # --- SALIDA (Caso Éxito) ---
    print("\n--- Resumen de Compra ---")
    print(f"Precio original: ${precio_original:,.2f}")
    print(f"Descuento aplicado: {porcentaje_desc * 100:.0f}% (-${monto_descuento:,.2f})")
    print(f"💰 Precio final a pagar: ${precio_final:,.2f}")