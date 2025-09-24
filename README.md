# 📊 Sistema de Reportes de Métricas - Panera Bread

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-Active-success.svg)

**Generador Automatizado de Reportes Excel con Métricas de Rendimiento KPI**

*Transforma datos de rendimiento en reportes profesionales con formato condicional, gráficos y análisis automático*

</div>

---

## 🎯 **Descripción del Proyecto**

Este sistema automatiza la generación de reportes Excel profesionales para el análisis de métricas de rendimiento del equipo de atención al cliente de Panera Bread. El script procesa datos de performance diarios e individuales, aplicando formato condicional tipo semáforo, generando gráficos de tendencias y creando análisis comparativos del equipo.

### ✨ **Características Principales**

- 🔄 **Automatización Completa**: Genera reportes sin intervención manual
- 🚦 **Formato Condicional Inteligente**: Sistema de semáforo (Verde/Amarillo/Rojo) basado en metas
- 📈 **Gráficos Automáticos**: Tendencias por mes y rankings del equipo
- 📊 **Múltiples Hojas**: Datos diarios y análisis del equipo en pestañas separadas
- 💼 **Formato Profesional**: Tablas con estilos corporativos y fórmulas automáticas
- 🎨 **Visual y Intuitivo**: Interfaz clara con iconos y colores representativos

---

## 🚀 **Instalación y Configuración**

### **Requisitos del Sistema**
- 🐍 **Python 3.8+** (Recomendado: Python 3.10+)
- 💻 **Sistema Operativo**: Windows, macOS, o Linux
- 📦 **Gestor de Paquetes**: pip

### **Instalación Paso a Paso**

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/ByCulichi/Culichi-Metrics.git
   cd Culichi-Metrics
   ```

2. **Crear Entorno Virtual** (Recomendado)
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar Dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verificar Instalación**
   ```bash
   python to_excel.PY
   ```

### 📦 **Dependencias**

| Librería | Versión | Propósito |
|----------|---------|-----------|
| `pandas` | >=2.0.0 | Manipulación y análisis de datos |
| `xlsxwriter` | >=3.0.0 | Generación de archivos Excel con formato |
| `openpyxl` | >=3.0.0 | Soporte adicional para Excel |

---

## 📈 **Métricas y KPIs Incluidos**

### **📅 Datos Diarios por Mes**
- **HANDLED**: Número de llamadas atendidas
- **OIR (%)**: Offer and Information Rate - Tasa de oferta e información
- **AHT (seg)**: Average Handle Time - Tiempo promedio de atención
- **PS & Compliance (%)**: Professional Standards & Compliance
- **RTA (%)**: Real Time Adherence - Adherencia al horario

### **👥 Análisis Individual del Equipo**
- **OIR (%)**: Tasa de oferta e información por empleado
- **QA (%)**: Quality Assurance - Aseguramiento de calidad  
- **CCA (%)**: Customer Care Advocacy - Defensa del cuidado al cliente
- **CARE (%)**: Índice de cuidado al cliente
- **NICE TOUR (%)**: Métrica de evaluación de servicio
- **ACS Score (%)**: American Customer Satisfaction Score
- **RTA (%)**: Adherencia al horario en tiempo real
- **PS & Compliance (%)**: Estándares profesionales y cumplimiento

### 🎯 **Metas y Objetivos**

| Métrica | Objetivo | Tipo | Descripción |
|---------|----------|------|-------------|
| OIR (%) | ≥ 90% | Mayor es mejor | Eficiencia en ofertas e información |
| AHT (seg) | ≤ 630 seg | Menor es mejor | Tiempo óptimo por llamada |
| QA (%) | ≥ 85% | Mayor es mejor | Calidad del servicio |
| RTA (%) | ≥ 85% | Mayor es mejor | Puntualidad y adherencia |
| CARE (%) | ≤ 5% | Menor es mejor | Minimizar problemas de atención |

---

## 🎨 **Estructura del Reporte Generado**

### **📋 Hoja 1: "Daily_Data"**
```
📊 Datos Diarios Organizados por Mes
├── 📅 Abril 2025
│   ├── Tabla con formato profesional
│   ├── Fila de promedios automáticos
│   ├── 🚦 Formato condicional (semáforo)
│   └── 📈 Gráfico de tendencia OIR vs AHT
├── 📅 Mayo 2025
│   └── [Misma estructura...]
└── 📅 [Otros meses...]
```

### **👥 Hoja 2: "Team_August"**
```
📊 Análisis Individual del Equipo
├── 📋 Tabla de métricas por empleado
├── 🧮 Promedios del equipo
├── 🚦 Formato condicional por métrica
└── 📊 Gráfico de ranking por OIR (%)
```

---

## 🎯 **Cómo Usar el Sistema**

### **🔧 Ejecución Básica**
```bash
python to_excel.PY
```

### **📝 Personalización de Datos**

**1. Actualizar Datos Diarios:**
```python
# Buscar la sección: daily_data = [
# Agregar nuevos registros siguiendo el formato:
{
    'Mes': 'Octubre', 
    'Call Date': '2025-10-01', 
    'HANDLED': 45, 
    'OIR (%)': 95.0, 
    'AHT (seg)': 580.0,
    # ... otras métricas
}
```

**2. Actualizar Datos del Equipo:**
```python
# Buscar la sección: data_equipo = {
# Modificar listas correspondientes:
'Empleado': ['Nuevo Empleado', ...],
'OIR (%)': [92.5, ...],
# ... otras métricas
```

**3. Ajustar Metas:**
```python
# Buscar la sección: metas = {
# Modificar valores objetivo:
'OIR (%)': 95.0,  # Nueva meta
'AHT (seg)': 600.0,  # Nuevo objetivo
```

### **🎨 Personalizar Nombre del Archivo**
```python
# Línea ~282 en to_excel.PY
output_file = r'Mi_Reporte_Personalizado.xlsx'
```

---

## 🚦 **Sistema de Formato Condicional**

El sistema utiliza colores intuitivos para evaluar el rendimiento:

| Color | Significado | Criterio |
|-------|------------|----------|
| 🟢 **Verde Oscuro** | Excelente - Cumple objetivo | ≥ 100% de la meta |
| 🟢 **Verde Claro** | Bueno - Cerca del objetivo | ≥ 95% de la meta |
| 🟡 **Amarillo** | Aceptable - Necesita mejora | ≥ 90% de la meta |
| 🔴 **Rojo** | Crítico - Requiere atención | < 90% de la meta |

*Para métricas donde "menor es mejor" (AHT, CARE), los criterios se invierten*

---

## 🛠️ **Mantenimiento y Personalización**

### **📁 Estructura del Código**
```
to_excel.PY
├── 📦 Importaciones y configuración
├── 📊 Datos diarios (daily_data)
├── 👥 Datos del equipo (data_equipo)
├── 🎯 Metas y objetivos (metas)
├── 🔧 Funciones auxiliares
├── 🎨 Función principal (main)
└── 🚀 Punto de entrada
```

### **🔧 Funciones Principales**
- `parse_date()`: Convierte fechas para ordenamiento
- `excel_col_letter()`: Convierte índices a letras de columna Excel
- `add_traffic_light()`: Aplica formato condicional semáforo
- `main()`: Función principal de generación del reporte

### **🎨 Personalización de Estilos**
```python
# Modificar formatos de celda (línea ~315)
fmt_header = workbook.add_format({
    'bold': True, 
    'bg_color': '#TU_COLOR',  # Cambiar color
    'font_color': 'white',
    'align': 'center'
})
```

---

## 🐛 **Solución de Problemas**

### **❌ Errores Comunes**

**1. `ModuleNotFoundError: No module named 'pandas'`**
```bash
pip install -r requirements.txt
```

**2. `PermissionError: [Errno 13] Permission denied`**
- ✅ Cierra el archivo Excel si está abierto
- ✅ Verifica permisos de escritura en la carpeta
- ✅ Ejecuta como administrador si es necesario

**3. `FileNotFoundError` o problemas de ruta**
- ✅ Verifica que estés en el directorio correcto
- ✅ Usa rutas absolutas si hay problemas

**4. Datos no se muestran correctamente**
- ✅ Verifica formato de fechas (`YYYY-MM-DD`)
- ✅ Asegúrate que las claves de los diccionarios coincidan
- ✅ Revisa que los datos numéricos no estén como texto

### **🔍 Modo Debug**
Para ver más detalles en caso de errores, modifica:
```python
# Agregar al final de main():
import traceback
traceback.print_exc()
```

---

## 🤝 **Contribución**

### **💡 Cómo Contribuir**
1. 🍴 Fork el repositorio
2. 🌟 Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. 💻 Realiza tus cambios y añade documentación
4. ✅ Ejecuta las pruebas
5. 📝 Commit tus cambios (`git commit -m 'Añadir nueva funcionalidad'`)
6. 📤 Push a la rama (`git push origin feature/nueva-funcionalidad`)
7. 🔄 Abre un Pull Request

### **📋 Estándares de Código**
- 📝 **Documentación**: Todas las funciones deben tener docstrings
- 🐍 **PEP 8**: Seguir estándares de estilo de Python
- 💬 **Comentarios**: Código autoexplicativo con comentarios claros
- ✅ **Pruebas**: Verificar funcionamiento antes de contribuir

---

## 👥 **Equipo**

### **✨ Mantenedores**
- **Christian Velasco Navarro** - *Desarrollador Principal* - [@ByCulichi](https://github.com/ByCulichi)

### **🙏 Agradecimientos**
- Equipo de Panera Bread por los requerimientos
- Comunidad de Python por las librerías utilizadas
- Contribuidores que ayudan a mejorar el proyecto

---

## 📄 **Licencia**

Este proyecto está bajo la Licencia MIT - ve el archivo [LICENSE](LICENSE) para más detalles.

---

## 📞 **Contacto y Soporte**

### **📧 Contacto**
- **Email**: christian.velasco@panera.com
- **GitHub**: [@ByCulichi](https://github.com/ByCulichi)
- **LinkedIn**: [Christian Velasco](https://linkedin.com/in/christian-velasco)

### **🆘 Obtener Ayuda**
- 🐛 **Issues**: Reporta bugs en [GitHub Issues](https://github.com/ByCulichi/Culichi-Metrics/issues)
- 💬 **Discusiones**: Únete a [GitHub Discussions](https://github.com/ByCulichi/Culichi-Metrics/discussions)
- 📖 **Wiki**: Consulta la [Wiki del proyecto](https://github.com/ByCulichi/Culichi-Metrics/wiki)

---

<div align="center">

**📊 Hecho con ❤️ para el equipo de Panera Bread**

*Automatizando reportes, maximizando el rendimiento*

⭐ **¡No olvides dar una estrella si te ayudó este proyecto!** ⭐

</div>

---

## ⚡ **Inicio Rápido (Quick Start)**

### **🚀 Opción 1: Configuración Automática (Recomendada para nuevos usuarios)**
```bash
# 1. Clona el repositorio
git clone https://github.com/ByCulichi/Culichi-Metrics.git
cd Culichi-Metrics

# 2. Ejecuta la configuración automática
python setup.py

# 3. ¡Listo! El reporte se generará automáticamente
```

### **⚡ Opción 2: Configuración Manual**
```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Generar reporte
python to_excel.PY
```

### **📊 Resultado**
- ✅ Archivo Excel: `Reporte_Metricas_Christian_modified.xlsx`
- 📋 2 hojas: Datos diarios + Análisis del equipo  
- 🚦 Formato condicional automático
- 📈 Gráficos de tendencias y rankings
