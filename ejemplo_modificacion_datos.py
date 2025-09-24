#!/usr/bin/env python3
"""
Ejemplo de cómo modificar datos para nuevos usuarios
====================================================

Este archivo muestra cómo añadir nuevos datos al sistema de reportes.
Copia estos ejemplos al archivo to_excel.PY en las secciones correspondientes.

Para más información, consulta el README.md
"""

# =============================================================================
# EJEMPLO 1: AÑADIR NUEVOS DATOS DIARIOS
# =============================================================================

# Busca en to_excel.PY la sección que comienza con:
# daily_data = [

# Añade nuevos registros siguiendo este formato:
ejemplo_datos_diarios = [
    {
        'Mes': 'Octubre',                    # Nombre del mes
        'Call Date': '2025-10-01',           # Fecha en formato YYYY-MM-DD
        'HANDLED': 42,                       # Llamadas atendidas (número)
        'OIR (%)': 95.5,                     # Offer and Information Rate
        'AHT (seg)': 620.3,                  # Average Handle Time en segundos
        'PS & Compliance (%)': 88.0,         # Professional Standards
        'RTA (%)': 92.0,                     # Real Time Adherence
        'Availability (%)': 99.2             # Disponibilidad del agente
    },
    # Añade más registros siguiendo el mismo formato...
]

# =============================================================================
# EJEMPLO 2: AÑADIR NUEVO EMPLEADO AL EQUIPO
# =============================================================================

# Busca en to_excel.PY la sección que comienza con:
# data_equipo = {

# Para añadir un nuevo empleado, debes añadir su nombre y todas sus métricas:
ejemplo_nuevo_empleado = {
    # 1. Añadir nombre a la lista de empleados:
    'Empleado': [
        # ... empleados existentes ...
        'Nuevo Empleado Ejemplo'          # ← Añadir aquí
    ],
    
    # 2. Añadir sus métricas (¡IMPORTANTE: debe coincidir el número de elementos!)
    'OIR (%)': [
        # ... valores existentes ...
        94.5                              # ← Añadir aquí
    ],
    
    'Silence Percentage (%)': [
        # ... valores existentes ...
        35.2                              # ← Añadir aquí
    ],
    
    'CCA (%)': [
        # ... valores existentes ...
        92.0                              # ← Añadir aquí
    ],
    
    # Continuar para TODAS las métricas:
    # 'CARE (%)', 'NICE TOUR (%)', 'QA (%)', 'ACS Score (%)',
    # 'Availability (%)', 'RTA (%)', 'PS & Compliance (%)', 'AHT'
}

# =============================================================================
# EJEMPLO 3: MODIFICAR METAS/OBJETIVOS
# =============================================================================

# Busca en to_excel.PY la sección que comienza con:
# metas = {

# Modifica los valores objetivo según tus necesidades:
ejemplo_nuevas_metas = {
    'OIR (%)': 92.0,                     # Nueva meta: 92% (era 90%)
    'AHT (seg)': 600.0,                  # Nueva meta: 600 seg (era 630)
    'QA (%)': 88.0,                      # Nueva meta: 88% (era 85%)
    'ACS (%)': 75.0,                     # Nueva meta: 75% (era 70%)
    'PS & Compliance (%)': 85.0,         # Nueva meta: 85% (era 80%)
    'RTA (%)': 90.0,                     # Nueva meta: 90% (era 85%)
    'CCA (%)': 95.0,                     # Nueva meta: 95% (era 90%)
    'CARE (%)': 3.0,                     # Nueva meta: 3% (era 5%)
    'NICE TOUR (%)': 85.0,               # Nueva meta: 85% (era 80%)
    'ACS Score (%)': 88.0,               # Nueva meta: 88% (era 85%)
    'Silence Percentage (%)': 35.0       # Nueva meta: 35% (era 40%)
}

# =============================================================================
# EJEMPLO 4: PERSONALIZAR NOMBRE DEL ARCHIVO
# =============================================================================

# Busca en to_excel.PY la línea que comienza con:
# output_file = r'Reporte_Metricas_Christian_modified.xlsx'

# Cambiala por:
ejemplo_nombre_archivo = r'Mi_Reporte_Personalizado_2025.xlsx'
# O con fecha automática:
from datetime import datetime
ejemplo_con_fecha = f'Reporte_Metricas_{datetime.now().strftime("%Y-%m-%d")}.xlsx'

# =============================================================================
# CONSEJOS IMPORTANTES
# =============================================================================

"""
⚠️  CONSEJOS PARA EVITAR ERRORES:

1. FORMATO DE FECHAS:
   ✅ Correcto: '2025-10-01' 
   ❌ Incorrecto: '01/10/2025', '01-10-25'

2. CONSISTENCIA EN LISTAS:
   ✅ Todas las listas del data_equipo deben tener el mismo número de elementos
   ❌ Si tienes 14 empleados, TODAS las métricas deben tener 14 valores

3. TIPOS DE DATOS:
   ✅ Números: 95.5, 620, 42
   ❌ Texto para números: '95.5', 'alto', 'bueno'

4. VALORES NULOS:
   ✅ Usar None para datos faltantes
   ❌ Dejar espacios vacíos o usar texto como 'N/A'

5. NOMBRES DE MESES:
   ✅ Usar nombres consistentes: 'Enero', 'Febrero'
   ❌ Mezclar: 'Enero', 'Feb', '02'

🔧 PARA PROBAR TUS CAMBIOS:
   1. Guarda el archivo to_excel.PY
   2. Ejecuta: python to_excel.PY
   3. Verifica que no hay errores
   4. Abre el archivo Excel generado
"""

print("""
📚 GUÍA RÁPIDA DE MODIFICACIÓN DE DATOS

Este archivo contiene ejemplos de cómo modificar los datos del sistema.
Para implementar cambios:

1. 📝 Estudia los ejemplos en este archivo
2. 🔧 Modifica to_excel.PY siguiendo los patrones
3. 🧪 Ejecuta python to_excel.PY para probar
4. 📊 Revisa el archivo Excel generado

Para más detalles, consulta README.md
""")