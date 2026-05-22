# ============================================================
# Universidad Nacional Abierta y a Distancia - UNAD
# Curso: Fundamentos de Programación - Código: 213022
# Fase 5 - Evaluación Final POA
# Problema 5: Horas trabajadas por equipo (Sobretiempo)
# ============================================================

# --- MATRIZ DE DATOS ---
# Formato: [Nombre del Recurso, Lunes, Martes, Miércoles, Jueves, Viernes]
equipo = [
    ["Ana García",    8, 9, 10, 8, 9],
    ["Luis Pérez",    7, 8,  8, 7, 8],
    ["María Torres",  9, 10, 9, 9, 10],
    ["Carlos Ruiz",   6, 7,  8, 6, 7]
]

# --- CONSTANTE ---
UMBRAL_HORAS = 40  # Horas estándar semanales


# ============================================================
# MÓDULO (FUNCIÓN): Calcula el total de horas y clasifica
# la jornada de un recurso.
# Parámetros:
#   recurso -> lista con [nombre, lun, mar, mie, jue, vie]
# Retorna:
#   total_horas (int), clasificacion (str)
# ============================================================
def calcular_jornada(recurso):
    total_horas = sum(recurso[1:])
    if total_horas > UMBRAL_HORAS:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
    return total_horas, clasificacion


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================
def main():
    print("=" * 55)
    print("   INFORME DE HORAS TRABAJADAS - SEMANA LABORAL")
    print("=" * 55)
    print(f"{'Nombre':<18} {'Total Horas':>12} {'Clasificación':>18}")
    print("-" * 55)

    for recurso in equipo:
        total, clasificacion = calcular_jornada(recurso)
        print(f"{recurso[0]:<18} {total:>12} {clasificacion:>18}")

    print("=" * 55)
    print(f"  Umbral de horas estándar: {UMBRAL_HORAS} horas semanales")
    print("=" * 55)


# --- LLAMADO AL PROGRAMA PRINCIPAL ---
if __name__ == '__main__':
    main()
