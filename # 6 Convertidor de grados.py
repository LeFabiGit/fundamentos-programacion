"""
Programa: Convertidor de Grados
Convierte una temperatura en grados Celsius a Fahrenheit o Kelvin.
"""

# --- CONSTANTES ---
FACTOR_FAHRENHEIT = 9 / 5
AJUSTE_FAHRENHEIT = 32
AJUSTE_KELVIN = 273.15

# Opciones del menú
OPCION_FAHRENHEIT = 1
OPCION_KELVIN = 2

# --- ENTRADA DE DATOS ---
print("--- Convertidor de Temperatura ---")
celsius = float(input("Ingresa la temperatura en grados Celsius (°C): "))

print("\n¿A qué unidad deseas convertir?")
print(f"{OPCION_FAHRENHEIT}. Fahrenheit (°F)")
print(f"{OPCION_KELVIN}. Kelvin (K)")
opcion = int(input("Selecciona una opción (1 o 2): "))

match opcion:
    case 1:  # Conversión a Fahrenheit
        resultado = (celsius * FACTOR_FAHRENHEIT) + AJUSTE_FAHRENHEIT
        unidad = "°F"
        valido = True
        
    case 2:  # Conversión a Kelvin
        resultado = celsius + AJUSTE_KELVIN
        unidad = "K"
        valido = True
        
    case _:  # Opción inválida
        valido = False

# --- SALIDA ---
if valido:
    print(f"\n✅ {celsius:.2f} °C equivalen a: {resultado:.2f} {unidad}")
else:
    print(f"\n❌ Error: La opción '{opcion}' no es válida. \
        Debes elegir {OPCION_FAHRENHEIT} o {OPCION_KELVIN}.")