"""
Programa: Calculadora de Calificaciones Finales

Calcula el promedio final de un estudiante aplicando porcentajes 
específicos a sus parciales, proyecto y examen, validando 
que las notas estén en el rango de 0 a 100.

"""

# --- CONSTANTES ---
PORCENTAJE_PARCIALES = 0.40
PORCENTAJE_PROYECTO = 0.30
PORCENTAJE_EXAMEN = 0.30
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 100.0

# --- ENTRADA DE DATOS ---
print("--- Calculadora de Calificaciones Finales ---")

# Solicitar las calificaciones al usuario
parciales = float(input("Ingresa la calificación de los Parciales (0-100): "))
proyecto = float(input("Ingresa la calificación del Proyecto (0-100): "))
examen_final = float(input("Ingresa la calificación del Examen Final (0-100): "))

# Validar que todas las calificaciones estén en el rango correcto (0 a 100)
if (NOTA_MINIMA <= parciales <= NOTA_MAXIMA and
    NOTA_MINIMA <= proyecto <= NOTA_MAXIMA and
    NOTA_MINIMA <= examen_final <= NOTA_MAXIMA):
    
    # Cálculo utilizando las constantes definidas al inicio
    nota_final = (parciales * PORCENTAJE_PARCIALES
                 + proyecto * PORCENTAJE_PROYECTO
                 + examen_final * PORCENTAJE_EXAMEN)
    
    # Imprimir el promedio final con dos decimales
    print("\n✅ Validación exitosa.")
    print(f"El promedio final del estudiante es: {nota_final:.2f}")

else:
    # Mensaje de error si alguna calificación está fuera de rango
    print("\n❌ Error: Todas las calificaciones deben estar en el rango de 0 a 100.")