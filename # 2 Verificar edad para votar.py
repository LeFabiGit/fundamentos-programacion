"""
Programa: Verificación de edad para votar.
Determina si una persona es elegible para votar basándose en su edad
validando que el dato ingresado sea un valor lógico y real.
"""
    
# --- CONSTANTES ---
EDAD_MINIMA_VOTAR = 18
EDAD_MINIMA_LOGICA = 0
EDAD_MAXIMA_LOGICA = 120
    
# --- ENTRADA DE DATOR ---
print ("--- Sistema de verificación de elegibilidad de voto---")
edad = int (input("Por favor, ingrese su edad"))
    
# --- PROCESO ---
# Validamos que la edad sea un número real y lógico
if edad < EDAD_MINIMA_LOGICA or edad > EDAD_MAXIMA_LOGICA:
        
    # --- SALIDA (Caso: Edad irreal o negativa) ---
    print(f"\n❌ Error: La edad ingresada ({edad}) no es válida. Debe estar entre {EDAD_MINIMA_LOGICA} y {EDAD_MAXIMA_LOGICA} años.")
        
else:
    # Si la edad es válida, procedemos a revisar si puede votar o no
    if edad >= EDAD_MINIMA_VOTAR:
        
        # --- SALIDA (Caso: Elegible para votar) ---
        print(f"\n✅ Tienes {edad} años. ¡Eres elegible para votar!")
        
    else:
        
        # --- SALIDA (Caso: Menor de edad) ---
        print(f"\n❌ Tienes {edad} años. No eres elegible para votar. Te faltan {EDAD_MINIMA_VOTAR - edad} años.")