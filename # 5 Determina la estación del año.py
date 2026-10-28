"""
Programa: Determinación de la Estación del Año
Determina la estación del año a partir de un número de mes ingresado.
"""

# --- CONSTANTES ---
MES_MINIMO = 1
MES_MAXIMO = 12

# --- ENTRADA DE DATOS ---
print("--- Estaciones del Año ---")
mes = int(input("Ingresa el número del mes (1-12): "))

# Usamos match-case para evaluar la variable 'mes'
match mes:
    # Primavera: marzo (3), abril (4), mayo (5)
    case 3 | 4 | 5:
        estacion = "Primavera"
        icono = "🌸"
    
    # Verano: junio (6), julio (7), agosto (8)
    case 6 | 7 | 8:
        estacion = "Verano"
        icono = "☀️"
    
    # Otoño: septiembre (9), octubre (10), noviembre (11)
    case 9 | 10 | 11:
        estacion = "Otoño"
        icono = "🍂"
    
    # Invierno: diciembre (12), enero (1), febrero (2)
    case 12 | 1 | 2:
        estacion = "Invierno"
        icono = "❄️"
    
    # El caso por defecto '_' atrapa cualquier número fuera de 1-12
    case _:
        estacion = "Invalido"

# --- SALIDA ---
if estacion == "Invalido":
    print(f"\n❌ Error: El número {mes} no corresponde a un mes válido. Debe ser entre {MES_MINIMO} y {MES_MAXIMO}.")
else:
    print(f"\n El mes {mes} corresponde a la estación: {estacion} {icono}")