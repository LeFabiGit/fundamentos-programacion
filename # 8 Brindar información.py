"""
Programa: Buscador de Información
Permite buscar el nombre de un artistas, películas o videojuegos.
"""

# --- CONSTANTES ---
TEMA_1 = "league of legends"
TEMA_2 = "halo"
TEMA_3 = "cortis"
TEMA_4 = "starset"
TEMA_5 = "hope"

# --- ENTRADA DE DATOS ---
print("--- 🔍 Buscador de Información ---")
print("Temas disponibles: League of Legends | Halo | Cortis | Starset | Hope")
busqueda = input("Ingresa el nombre del tema que deseas consultar: ")

# --- PROCESO ---
tema = busqueda.strip().lower()

match tema:
    case "league of legends":
        informacion = (
            "📌 Tipo: Videojuego competitivo (MOBA) desarrollado por Riot Games.\n"
            "🎮 Lanzamiento: 2009.\n"
            "📝 Sinopsis: Dos equipos de 5 jugadores se enfrentan en la Grieta del Invocador "
            "con el objetivo de destruir el Nexo enemigo. Es el pilar fundamental de los esports globales."
        )
        valido = True

    case "halo":
        informacion = (
            "📌 Tipo: Saga de videojuegos de ciencia ficción y universo literario/televisivo.\n"
            "🛡️ Protagonista: El supersoldado Spartan John-117, mejor conocido como el 'Master Chief'.\n"
            "📝 Sinopsis: Narra la desesperada guerra espacial en el siglo XXVI entre la humanidad (UNSC) "
            "y una alianza alienígena fanática conocida como el Covenant, girando en torno a masivos mundos anillo."
        )
        valido = True

    case "cortis":
        informacion = (
            "📌 Tipo: Boy band musical surcoreana de K-pop bajo el sello BIGHIT MUSIC.\n"
            "🎤 Miembros: Martin, James, Juhoon, Seonghyeon y Keonho.\n"
            "📝 Detalles: Debutaron en agosto de 2025 con 'What You Want'. Su nombre proviene de la "
            "frase 'Color Outside the Lines', que simboliza pensar libremente y romper las normas."
        )
        valido = True

    case "starset":
        informacion = (
            "📌 Tipo: Banda estadounidense de rock alternativo y rock cinematográfico.\n"
            "🧑‍🎤 Líder: Dustin Bates.\n"
            "📝 Detalles: ¡Tu banda favorita! Es un grupo conceptual fundado con una narrativa "
            "de ciencia ficción profunda, donde sus canciones y conciertos forman parte de una historia "
            "difundida por la ficticia 'The Starset Society'."
        )
        valido = True

    case "hope":
        informacion = (
            "📌 Tipo: Película épica de ciencia ficción y suspenso (Corea del Sur).\n"
            "🎬 Director: Na Hong-jin | Estreno: 2026.\n"
            "📝 Sinopsis: Sigue los eventos en una remota aldea donde un jefe de policía y cazadores "
            "locales se enfrentan a una misteriosa y destructiva presencia, escalando en un conflicto "
            "de magnitudes cósmicas."
        )
        valido = True

    case _:
        valido = False

# --- SALIDA ---
if valido:
    print(f"\n✅ Información encontrada para '{busqueda}':")
    print("-" * 50)
    print(informacion)
    print("-" * 50)
else:
    print(f"\n❌ Lo siento, '{busqueda}' no se encuentra en la base de datos.")
    print("Asegúrate de escribir una opción válida: League of Legends, Halo, Cortis, Starset o Hope.")