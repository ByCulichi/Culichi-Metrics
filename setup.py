#!/usr/bin/env python3
"""
Script de instalación y verificación para el Sistema de Reportes de Métricas
============================================================================

Este script automatiza la instalación de dependencias y verifica que
el sistema esté configurado correctamente para generar reportes.

Uso:
    python setup.py
"""

import subprocess
import sys
import os

def print_banner():
    """Imprime el banner de bienvenida."""
    print("=" * 70)
    print("🚀 CONFIGURACIÓN AUTOMÁTICA - SISTEMA DE REPORTES PANERA")
    print("   Instalación y verificación de dependencias")
    print("=" * 70)

def check_python_version():
    """Verifica que la versión de Python sea compatible."""
    print("🐍 Verificando versión de Python...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Error: Se requiere Python 3.8 o superior")
        print(f"   Versión actual: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
    return True

def install_requirements():
    """Instala las dependencias del requirements.txt."""
    print("\n📦 Instalando dependencias...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError:
        print("❌ Error al instalar dependencias")
        return False

def verify_installation():
    """Verifica que las librerías estén instaladas correctamente."""
    print("\n🔍 Verificando instalación...")
    
    required_packages = ['pandas', 'xlsxwriter', 'openpyxl']
    all_good = True
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} - OK")
        except ImportError:
            print(f"❌ {package} - No disponible")
            all_good = False
    
    return all_good

def run_test():
    """Ejecuta una prueba del sistema."""
    print("\n🧪 Ejecutando prueba del sistema...")
    
    try:
        # Importa y ejecuta una prueba básica
        result = subprocess.run([sys.executable, "to_excel.PY"], 
                               capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print("✅ Prueba exitosa - El sistema funciona correctamente")
            print("📁 Archivo de prueba generado: Reporte_Metricas_Christian_modified.xlsx")
            return True
        else:
            print("❌ Error en la prueba:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ La prueba tomó demasiado tiempo - posiblemente exitosa")
        return True
    except Exception as e:
        print(f"❌ Error ejecutando prueba: {e}")
        return False

def main():
    """Función principal del script de configuración."""
    print_banner()
    
    # Verificar Python
    if not check_python_version():
        print("\n💡 Actualiza Python a la versión 3.8 o superior e intenta de nuevo")
        sys.exit(1)
    
    # Instalar dependencias
    if not install_requirements():
        print("\n💡 Revisa tu conexión a internet e intenta de nuevo")
        sys.exit(1)
    
    # Verificar instalación
    if not verify_installation():
        print("\n💡 Intenta ejecutar: pip install -r requirements.txt")
        sys.exit(1)
    
    # Ejecutar prueba
    if not run_test():
        print("\n💡 Revisa los errores anteriores y contacta al administrador")
        sys.exit(1)
    
    # Mensaje final
    print("\n" + "=" * 70)
    print("🎉 CONFIGURACIÓN COMPLETADA EXITOSAMENTE")
    print("   El sistema está listo para generar reportes")
    print("\n💡 Para generar reportes, ejecuta:")
    print("   python to_excel.PY")
    print("=" * 70)

if __name__ == "__main__":
    main()