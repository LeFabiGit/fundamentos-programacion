"""
Programa: Evaluación de Calificaciones con Letras
Transforma una calificación numérica (0-100) a su equivalente
en letra (A, B, C, D, F) utilizando una estructura if-elif-else.
"""

# --- CONSTANTES ---
LIMITE_A = 90
LIMITE_B = 80
LIMITE_C = 70
LIMITE_D = 60
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 100.0

# --- ENTRADA DE DATOS ---
print("--- Convertidor de Calificación Numérica a Letra ---")
calificacion = float(input("Ingresa la calificación numérica (0-100): "))

# Validar  que la calificación esté dentro del rango real permitido
if calificacion < NOTA_MINIMA or calificacion > NOTA_MAXIMA:
    
    # --- SALIDA (Caso Error) ---
    print(f"\n❌ Error: La calificación {calificacion} está fuera del rango permitido ({NOTA_MINIMA:.0f} - {NOTA_MAXIMA:.0f}).")

else:
    # Evaluamos de la más alta a la más baja usando if-elif-else
    if calificacion >= LIMITE_A:
        letra = "A"
    elif calificacion >= LIMITE_B:
        letra = "B"
    elif calificacion >= LIMITE_C:
        letra = "C"
    elif calificacion >= LIMITE_D:
        letra = "D"
    else:
        letra = "F"
        
    # --- SALIDA (Caso Éxito) ---
    print(f"\n✅ Tu calificación final es: {letra}")