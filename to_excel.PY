#!/usr/bin/env python3
"""
Sistema de Reportes de Métricas - Panera Bread
==============================================

Este script genera reportes automatizados de Excel con métricas de rendimiento (KPIs)
para el equipo de atención al cliente. Incluye tablas dinámicas, formatos condicionales 
tipo semáforo, gráficos de tendencias y análisis por empleado.

Autor: Christian Velasco Navarro
Empresa: Culichi Metrics - Panera Bread
Fecha: 2025
"""

# =============================================================================
# IMPORTACIONES DE LIBRERÍAS NECESARIAS
# =============================================================================

import pandas as pd
from datetime import datetime
from xlsxwriter.utility import xl_col_to_name

# =============================================================================
# 1. CONFIGURACIÓN INICIAL Y CONSTANTES
# =============================================================================

# Datos diarios de métricas por fecha y mes
daily_data = [
    # Abril
    {'Mes': 'Abril', 'Call Date': '2025-04-01', 'HANDLED': 35, 'OIR (%)': 100.0, 'AHT (seg)': 560.2, 'PS & Compliance (%)': 100.0, 'RTA (%)': 90.0, 'Availability (%)': 99.6},
    {'Mes': 'Abril', 'Call Date': '2025-04-02', 'HANDLED': 32, 'OIR (%)': 100.0, 'AHT (seg)': 575.1, 'PS & Compliance (%)': 100.0, 'RTA (%)': 85.0, 'Availability (%)': 99.7},
    {'Mes': 'Abril', 'Call Date': '2025-04-03', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 590.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 88.0, 'Availability (%)': 99.5},
    {'Mes': 'Abril', 'Call Date': '2025-04-04', 'HANDLED': 30, 'OIR (%)': 100.0, 'AHT (seg)': 545.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 92.0, 'Availability (%)': 99.8},
    {'Mes': 'Abril', 'Call Date': '2025-04-05', 'HANDLED': 40, 'OIR (%)': 100.0, 'AHT (seg)': 600.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 95.0, 'Availability (%)': 99.6},
    {'Mes': 'Abril', 'Call Date': '2025-04-06', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 570.0, 'PS & Compliance (%)': 50.0, 'RTA (%)': 87.0, 'Availability (%)': 99.7},
    {'Mes': 'Abril', 'Call Date': '2025-04-07', 'HANDLED': 37, 'OIR (%)': 100.0, 'AHT (seg)': 585.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 89.0, 'Availability (%)': 99.6},
    {'Mes': 'Abril', 'Call Date': '2025-04-08', 'HANDLED': 34, 'OIR (%)': 100.0, 'AHT (seg)': 550.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 93.0, 'Availability (%)': 99.8},
    {'Mes': 'Abril', 'Call Date': '2025-04-09', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 595.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 86.0, 'Availability (%)': 99.5},
    {'Mes': 'Abril', 'Call Date': '2025-04-10', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 565.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 91.0, 'Availability (%)': 99.7},
    {'Mes': 'Abril', 'Call Date': '2025-04-11', 'HANDLED': None, 'OIR (%)': None, 'AHT (seg)': None, 'PS & Compliance (%)': None, 'RTA (%)': None, 'Availability (%)': None},
    {'Mes': 'Abril', 'Call Date': '2025-04-12', 'HANDLED': 40, 'OIR (%)': 100.0, 'AHT (seg)': 540.3, 'PS & Compliance (%)': 100.0, 'RTA (%)': 94.1, 'Availability (%)': 99.1},
    {'Mes': 'Abril', 'Call Date': '2025-04-14', 'HANDLED': 39, 'OIR (%)': 100.0, 'AHT (seg)': 675.7, 'PS & Compliance (%)': 100.0, 'RTA (%)': 96.3, 'Availability (%)': 100.0},
    {'Mes': 'Abril', 'Call Date': '2025-04-15', 'HANDLED': 32, 'OIR (%)': 100.0, 'AHT (seg)': 586.3, 'PS & Compliance (%)': 100.0, 'RTA (%)': 81.2, 'Availability (%)': 99.9},
    {'Mes': 'Abril', 'Call Date': '2025-04-16', 'HANDLED': 40, 'OIR (%)': 100.0, 'AHT (seg)': 540.2, 'PS & Compliance (%)': 57.5, 'RTA (%)': 98.2, 'Availability (%)': 99.8},
    {'Mes': 'Abril', 'Call Date': '2025-04-17', 'HANDLED': 45, 'OIR (%)': 100.0, 'AHT (seg)': 449.3, 'PS & Compliance (%)': 87.5, 'RTA (%)': 93.6, 'Availability (%)': 99.9},
    {'Mes': 'Abril', 'Call Date': '2025-04-19', 'HANDLED': 42, 'OIR (%)': 100.0, 'AHT (seg)': 478.8, 'PS & Compliance (%)': 100.0, 'RTA (%)': 94.6, 'Availability (%)': 99.5},
    {'Mes': 'Abril', 'Call Date': '2025-04-21', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 572.3, 'PS & Compliance (%)': 100.0, 'RTA (%)': 91.7, 'Availability (%)': 99.7},
    {'Mes': 'Abril', 'Call Date': '2025-04-21', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 670.2, 'PS & Compliance (%)': 100.0, 'RTA (%)': 91.9, 'Availability (%)': 99.9},
    {'Mes': 'Abril', 'Call Date': '2025-04-22', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 577.4, 'PS & Compliance (%)': 100.0, 'RTA (%)': 76.7, 'Availability (%)': 99.7},
    {'Mes': 'Abril', 'Call Date': '2025-04-23', 'HANDLED': 29, 'OIR (%)': 100.0, 'AHT (seg)': 550.9, 'PS & Compliance (%)': 50.0, 'RTA (%)': 75.1, 'Availability (%)': 99.8},
    {'Mes': 'Abril', 'Call Date': '2025-04-24', 'HANDLED': 39, 'OIR (%)': 100.0, 'AHT (seg)': 581.9, 'PS & Compliance (%)': 100.0, 'RTA (%)': 98.7, 'Availability (%)': 99.8},
    {'Mes': 'Abril', 'Call Date': '2025-04-26', 'HANDLED': 43, 'OIR (%)': 100.0, 'AHT (seg)': 452.4, 'PS & Compliance (%)': 100.0, 'RTA (%)': 96.9, 'Availability (%)': 99.1},
    {'Mes': 'Abril', 'Call Date': '2025-04-27', 'HANDLED': 16, 'OIR (%)': 100.0, 'AHT (seg)': 242.6, 'PS & Compliance (%)': 100.0, 'RTA (%)': 60.9, 'Availability (%)': 99.1},
    {'Mes': 'Abril', 'Call Date': '2025-04-28', 'HANDLED': 41, 'OIR (%)': 100.0, 'AHT (seg)': 529.1, 'PS & Compliance (%)': 100.0, 'RTA (%)': 94.1, 'Availability (%)': 99.0},

    # Mayo
    {'Mes': 'Mayo', 'Call Date': '2025-05-01', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 500.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 82.0, 'Availability (%)': 99.8},
    {'Mes': 'Mayo', 'Call Date': '2025-05-02', 'HANDLED': 29, 'OIR (%)': 100.0, 'AHT (seg)': 480.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 78.0, 'Availability (%)': 99.9},
    {'Mes': 'Mayo', 'Call Date': '2025-05-03', 'HANDLED': 35, 'OIR (%)': 100.0, 'AHT (seg)': 520.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 85.0, 'Availability (%)': 99.7},
    {'Mes': 'Mayo', 'Call Date': '2025-05-04', 'HANDLED': 32, 'OIR (%)': 100.0, 'AHT (seg)': 510.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 80.0, 'Availability (%)': 99.8},
    {'Mes': 'Mayo', 'Call Date': '2025-05-05', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 530.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 83.0, 'Availability (%)': 99.6},
    {'Mes': 'Mayo', 'Call Date': '2025-05-06', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 527.3, 'PS & Compliance (%)': 100.0, 'RTA (%)': 80.1, 'Availability (%)': 99.8},
    {'Mes': 'Mayo', 'Call Date': '2025-05-07', 'HANDLED': 10, 'OIR (%)': 100.0, 'AHT (seg)': 414.2, 'PS & Compliance (%)': 100.0, 'RTA (%)': 50.6, 'Availability (%)': 99.8},
    {'Mes': 'Mayo', 'Call Date': '2025-05-08', 'HANDLED': 30, 'OIR (%)': 100.0, 'AHT (seg)': 490.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 79.0, 'Availability (%)': 99.9},
    {'Mes': 'Mayo', 'Call Date': '2025-05-09', 'HANDLED': 34, 'OIR (%)': 100.0, 'AHT (seg)': 515.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 81.0, 'Availability (%)': 99.7},
    {'Mes': 'Mayo', 'Call Date': '2025-05-10', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 505.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 84.0, 'Availability (%)': 99.8},
    {'Mes': 'Mayo', 'Call Date': '2025-05-11', 'HANDLED': 37, 'OIR (%)': 100.0, 'AHT (seg)': 525.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 87.0, 'Availability (%)': 99.6},
    {'Mes': 'Mayo', 'Call Date': '2025-05-12', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 495.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 80.0, 'Availability (%)': 99.9},
    {'Mes': 'Mayo', 'Call Date': '2025-05-13', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 353.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 70.4, 'Availability (%)': 99.9},
    {'Mes': 'Mayo', 'Call Date': '2025-05-14', 'HANDLED': 44, 'OIR (%)': 100.0, 'AHT (seg)': 361.1, 'PS & Compliance (%)': 100.0, 'RTA (%)': 75.8, 'Availability (%)': 99.8},
    {'Mes': 'Mayo', 'Call Date': '2025-05-15', 'HANDLED': 30, 'OIR (%)': 100.0, 'AHT (seg)': 427.8, 'PS & Compliance (%)': 100.0, 'RTA (%)': 89.6, 'Availability (%)': 100.0},
    {'Mes': 'Mayo', 'Call Date': '2025-05-16', 'HANDLED': 37, 'OIR (%)': 100.0, 'AHT (seg)': 600.9, 'PS & Compliance (%)': 100.0, 'RTA (%)': 80.4, 'Availability (%)': 99.9},
    {'Mes': 'Mayo', 'Call Date': '2025-05-22', 'HANDLED': 40, 'OIR (%)': 75.0, 'AHT (seg)': 505.7, 'PS & Compliance (%)': 100.0, 'RTA (%)': 64.2, 'Availability (%)': 99.9},
    {'Mes': 'Mayo', 'Call Date': '2025-05-23', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 600.7, 'PS & Compliance (%)': 87.5, 'RTA (%)': 80.4, 'Availability (%)': 99.4},
    {'Mes': 'Mayo', 'Call Date': '2025-05-24', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 620.1, 'PS & Compliance (%)': 89.2, 'RTA (%)': 0.0, 'Availability (%)': 99.7},
    {'Mes': 'Mayo', 'Call Date': '2025-05-26', 'HANDLED': 15, 'OIR (%)': 100.0, 'AHT (seg)': 280.1, 'PS & Compliance (%)': 0.0, 'RTA (%)': 50.8, 'Availability (%)': 99.8},
    {'Mes': 'Mayo', 'Call Date': '2025-05-27', 'HANDLED': 40, 'OIR (%)': 100.0, 'AHT (seg)': 660.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 70.4, 'Availability (%)': 99.7},
    {'Mes': 'Mayo', 'Call Date': '2025-05-28', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 731.2, 'PS & Compliance (%)': None, 'RTA (%)': 75.7, 'Availability (%)': 99.0},
    {'Mes': 'Mayo', 'Call Date': '2025-05-29', 'HANDLED': 28, 'OIR (%)': 100.0, 'AHT (seg)': 767.8, 'PS & Compliance (%)': None, 'RTA (%)': 89.5, 'Availability (%)': 99.0},
    {'Mes': 'Mayo', 'Call Date': '2025-05-30', 'HANDLED': None, 'OIR (%)': None, 'AHT (seg)': None, 'PS & Compliance (%)': None, 'RTA (%)': None, 'Availability (%)': None},
    {'Mes': 'Mayo', 'Call Date': '2025-05-31', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 600.9, 'PS & Compliance (%)': 87.5, 'RTA (%)': 80.4, 'Availability (%)': 99.4},

    # Junio
    {'Mes': 'Junio', 'Call Date': '2025-06-01', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 540.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 90.0, 'Availability (%)': 99.7},
    {'Mes': 'Junio', 'Call Date': '2025-06-02', 'HANDLED': 32, 'OIR (%)': 100.0, 'AHT (seg)': 530.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 88.0, 'Availability (%)': 99.8},
    {'Mes': 'Junio', 'Call Date': '2025-06-03', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 560.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 85.0, 'Availability (%)': 99.6},
    {'Mes': 'Junio', 'Call Date': '2025-06-04', 'HANDLED': 30, 'OIR (%)': 100.0, 'AHT (seg)': 520.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 91.0, 'Availability (%)': 99.9},
    {'Mes': 'Junio', 'Call Date': '2025-06-05', 'HANDLED': 35, 'OIR (%)': 100.0, 'AHT (seg)': 550.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 93.0, 'Availability (%)': 99.7},
    {'Mes': 'Junio', 'Call Date': '2025-06-06', 'HANDLED': 34, 'OIR (%)': 100.0, 'AHT (seg)': 535.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 87.0, 'Availability (%)': 99.8},
    {'Mes': 'Junio', 'Call Date': '2025-06-07', 'HANDLED': 37, 'OIR (%)': 100.0, 'AHT (seg)': 545.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 89.0, 'Availability (%)': 99.6},
    {'Mes': 'Junio', 'Call Date': '2025-06-08', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 525.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 92.0, 'Availability (%)': 99.9},
    {'Mes': 'Junio', 'Call Date': '2025-06-09', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 570.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 86.0, 'Availability (%)': 99.7},
    {'Mes': 'Junio', 'Call Date': '2025-06-11', 'HANDLED': 29, 'OIR (%)': 100.0, 'AHT (seg)': 604.4, 'PS & Compliance (%)': None, 'RTA (%)': 73.1, 'Availability (%)': 99.5},
    {'Mes': 'Junio', 'Call Date': '2025-06-12', 'HANDLED': 30, 'OIR (%)': 100.0, 'AHT (seg)': 693.3, 'PS & Compliance (%)': None, 'RTA (%)': 89.7, 'Availability (%)': 99.7},
    {'Mes': 'Junio', 'Call Date': '2025-06-13', 'HANDLED': None, 'OIR (%)': None, 'AHT (seg)': None, 'PS & Compliance (%)': None, 'RTA (%)': None, 'Availability (%)': None},
    {'Mes': 'Junio', 'Call Date': '2025-06-14', 'HANDLED': 44, 'OIR (%)': 100.0, 'AHT (seg)': 572.5, 'PS & Compliance (%)': None, 'RTA (%)': 87.1, 'Availability (%)': 99.7},
    {'Mes': 'Junio', 'Call Date': '2025-06-16', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 647.2, 'PS & Compliance (%)': None, 'RTA (%)': 93.7, 'Availability (%)': 99.8},
    {'Mes': 'Junio', 'Call Date': '2025-06-17', 'HANDLED': 43, 'OIR (%)': 100.0, 'AHT (seg)': 548.3, 'PS & Compliance (%)': None, 'RTA (%)': 97.3, 'Availability (%)': 99.5},
    {'Mes': 'Junio', 'Call Date': '2025-06-18', 'HANDLED': 42, 'OIR (%)': 100.0, 'AHT (seg)': 555.7, 'PS & Compliance (%)': None, 'RTA (%)': 81.7, 'Availability (%)': 98.9},
    {'Mes': 'Junio', 'Call Date': '2025-06-19', 'HANDLED': 28, 'OIR (%)': 100.0, 'AHT (seg)': 743.8, 'PS & Compliance (%)': None, 'RTA (%)': 95.8, 'Availability (%)': 99.7},
    {'Mes': 'Junio', 'Call Date': '2025-06-21', 'HANDLED': 42, 'OIR (%)': 100.0, 'AHT (seg)': 550.5, 'PS & Compliance (%)': 87.5, 'RTA (%)': 92.1, 'Availability (%)': 99.8},
    {'Mes': 'Junio', 'Call Date': '2025-06-22', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 426.5, 'PS & Compliance (%)': 100.0, 'RTA (%)': 89.2, 'Availability (%)': 99.8},
    {'Mes': 'Junio', 'Call Date': '2025-06-23', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 784.6, 'PS & Compliance (%)': 100.0, 'RTA (%)': 82.7, 'Availability (%)': 99.4},
    {'Mes': 'Junio', 'Call Date': '2025-06-24', 'HANDLED': 24, 'OIR (%)': 100.0, 'AHT (seg)': 684.6, 'PS & Compliance (%)': 100.0, 'RTA (%)': 73.5, 'Availability (%)': 99.0},
    {'Mes': 'Junio', 'Call Date': '2025-06-25', 'HANDLED': 30, 'OIR (%)': 100.0, 'AHT (seg)': 706.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 92.8, 'Availability (%)': 99.0},
    {'Mes': 'Junio', 'Call Date': '2025-06-26', 'HANDLED': 35, 'OIR (%)': 100.0, 'AHT (seg)': 461.3, 'PS & Compliance (%)': 100.0, 'RTA (%)': 85.3, 'Availability (%)': 99.0},
    {'Mes': 'Junio', 'Call Date': '2025-06-28', 'HANDLED': 40, 'OIR (%)': 100.0, 'AHT (seg)': 529.1, 'PS & Compliance (%)': 100.0, 'RTA (%)': 94.9, 'Availability (%)': 99.9},

    # Julio
    {'Mes': 'Julio', 'Call Date': '2025-07-01', 'HANDLED': 35, 'OIR (%)': 100.0, 'AHT (seg)': 580.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 84.0, 'Availability (%)': 98.0},
    {'Mes': 'Julio', 'Call Date': '2025-07-02', 'HANDLED': 32, 'OIR (%)': 100.0, 'AHT (seg)': 560.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 80.0, 'Availability (%)': 97.5},
    {'Mes': 'Julio', 'Call Date': '2025-07-03', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 590.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 82.0, 'Availability (%)': 98.2},
    {'Mes': 'Julio', 'Call Date': '2025-07-04', 'HANDLED': 30, 'OIR (%)': 100.0, 'AHT (seg)': 540.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 85.0, 'Availability (%)': 97.8},
    {'Mes': 'Julio', 'Call Date': '2025-07-05', 'HANDLED': 34, 'OIR (%)': 100.0, 'AHT (seg)': 570.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 87.0, 'Availability (%)': 98.5},
    {'Mes': 'Julio', 'Call Date': '2025-07-06', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 550.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 83.0, 'Availability (%)': 98.0},
    {'Mes': 'Julio', 'Call Date': '2025-07-07', 'HANDLED': 37, 'OIR (%)': 100.0, 'AHT (seg)': 585.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 81.0, 'Availability (%)': 97.7},
    {'Mes': 'Julio', 'Call Date': '2025-07-08', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 565.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 86.0, 'Availability (%)': 98.3},
    {'Mes': 'Julio', 'Call Date': '2025-07-09', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 575.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 84.0, 'Availability (%)': 98.1},
    {'Mes': 'Julio', 'Call Date': '2025-07-10', 'HANDLED': 35, 'OIR (%)': 100.0, 'AHT (seg)': 560.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 88.0, 'Availability (%)': 97.9},
    {'Mes': 'Julio', 'Call Date': '2025-07-12', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 572.4, 'PS & Compliance (%)': 100.0, 'RTA (%)': 83.5, 'Availability (%)': 97.7},
    {'Mes': 'Julio', 'Call Date': '2025-07-13', 'HANDLED': 10, 'OIR (%)': 100.0, 'AHT (seg)': 414.2, 'PS & Compliance (%)': 100.0, 'RTA (%)': 80.9, 'Availability (%)': 95.3},
    {'Mes': 'Julio', 'Call Date': '2025-07-14', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 530.1, 'PS & Compliance (%)': 100.0, 'RTA (%)': 79.3, 'Availability (%)': 95.8},
    {'Mes': 'Julio', 'Call Date': '2025-07-15', 'HANDLED': 34, 'OIR (%)': 100.0, 'AHT (seg)': 361.1, 'PS & Compliance (%)': 86.3, 'RTA (%)': 91.7, 'Availability (%)': 97.6},
    {'Mes': 'Julio', 'Call Date': '2025-07-16', 'HANDLED': 30, 'OIR (%)': 100.0, 'AHT (seg)': 427.7, 'PS & Compliance (%)': 91.7, 'RTA (%)': 82.5, 'Availability (%)': 98.9},
    {'Mes': 'Julio', 'Call Date': '2025-07-17', 'HANDLED': 37, 'OIR (%)': 100.0, 'AHT (seg)': 529.2, 'PS & Compliance (%)': 82.5, 'RTA (%)': 76.9, 'Availability (%)': 99.0},
    {'Mes': 'Julio', 'Call Date': '2025-07-19', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 345.4, 'PS & Compliance (%)': 76.9, 'RTA (%)': 76.6, 'Availability (%)': 98.4},
    {'Mes': 'Julio', 'Call Date': '2025-07-20', 'HANDLED': 32, 'OIR (%)': 100.0, 'AHT (seg)': 501.6, 'PS & Compliance (%)': 74.6, 'RTA (%)': 80.4, 'Availability (%)': 98.3},
    {'Mes': 'Julio', 'Call Date': '2025-07-21', 'HANDLED': 40, 'OIR (%)': 100.0, 'AHT (seg)': 770.0, 'PS & Compliance (%)': 4.0, 'RTA (%)': 90.5, 'Availability (%)': 0.0},

    # Agosto
    {'Mes': 'Agosto', 'Call Date': '2025-08-01', 'HANDLED': 34, 'OIR (%)': 100.0, 'AHT (seg)': 610.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 89.0, 'Availability (%)': 99.8},
    {'Mes': 'Agosto', 'Call Date': '2025-08-02', 'HANDLED': 32, 'OIR (%)': 98.0, 'AHT (seg)': 590.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 87.0, 'Availability (%)': 99.7},
    {'Mes': 'Agosto', 'Call Date': '2025-08-03', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 620.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 85.0, 'Availability (%)': 99.6},
    {'Mes': 'Agosto', 'Call Date': '2025-08-04', 'HANDLED': 30, 'OIR (%)': 96.0, 'AHT (seg)': 580.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 91.0, 'Availability (%)': 99.6},
    {'Mes': 'Agosto', 'Call Date': '2025-08-05', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 630.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 93.0, 'Availability (%)': 99.7},
    {'Mes': 'Agosto', 'Call Date': '2025-08-07', 'HANDLED': 37, 'OIR (%)': 100.0, 'AHT (seg)': 615.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 88.0, 'Availability (%)': 99.6},
    {'Mes': 'Agosto', 'Call Date': '2025-08-08', 'HANDLED': 35, 'OIR (%)': 99.0, 'AHT (seg)': 595.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 90.0, 'Availability (%)': 100.0},
    {'Mes': 'Agosto', 'Call Date': '2025-08-09', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 605.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 84.0, 'Availability (%)': 99.7},
    {'Mes': 'Agosto', 'Call Date': '2025-08-10', 'HANDLED': 34, 'OIR (%)': 98.0, 'AHT (seg)': 585.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 92.0, 'Availability (%)': 99.8},
    {'Mes': 'Agosto', 'Call Date': '2025-08-13', 'HANDLED': 9, 'OIR (%)': None, 'AHT (seg)': 826.6, 'PS & Compliance (%)': None, 'RTA (%)': 73.3, 'Availability (%)': 99.1},
    {'Mes': 'Agosto', 'Call Date': '2025-08-15', 'HANDLED': None, 'OIR (%)': None, 'AHT (seg)': None, 'PS & Compliance (%)': None, 'RTA (%)': None, 'Availability (%)': None},
    {'Mes': 'Agosto', 'Call Date': '2025-08-16', 'HANDLED': 94, 'OIR (%)': None, 'AHT (seg)': 95.6, 'PS & Compliance (%)': 100.0, 'RTA (%)': 87.2, 'Availability (%)': 98.8},
    {'Mes': 'Agosto', 'Call Date': '2025-08-18', 'HANDLED': 48, 'OIR (%)': 100.0, 'AHT (seg)': 297.9, 'PS & Compliance (%)': 100.0, 'RTA (%)': 89.7, 'Availability (%)': 98.5},
    {'Mes': 'Agosto', 'Call Date': '2025-08-19', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 620.1, 'PS & Compliance (%)': 87.5, 'RTA (%)': 86.2, 'Availability (%)': 99.7},
    {'Mes': 'Agosto', 'Call Date': '2025-08-20', 'HANDLED': 26, 'OIR (%)': 100.0, 'AHT (seg)': 653.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 84.2, 'Availability (%)': 99.0},
    {'Mes': 'Agosto', 'Call Date': '2025-08-22', 'HANDLED': 24, 'OIR (%)': 100.0, 'AHT (seg)': 527.3, 'PS & Compliance (%)': 87.5, 'RTA (%)': 77.8, 'Availability (%)': 97.3},
    {'Mes': 'Agosto', 'Call Date': '2025-08-23', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 620.1, 'PS & Compliance (%)': 0.0, 'RTA (%)': 92.8, 'Availability (%)': 99.7},
    {'Mes': 'Agosto', 'Call Date': '2025-08-23', 'HANDLED': None, 'OIR (%)': None, 'AHT (seg)': None, 'PS & Compliance (%)': None, 'RTA (%)': None, 'Availability (%)': None},
    {'Mes': 'Agosto', 'Call Date': '2025-08-24', 'HANDLED': 15, 'OIR (%)': 100.0, 'AHT (seg)': 280.1, 'PS & Compliance (%)': 100.0, 'RTA (%)': 50.8, 'Availability (%)': 99.8},
    {'Mes': 'Agosto', 'Call Date': '2025-08-26', 'HANDLED': 40, 'OIR (%)': 100.0, 'AHT (seg)': 660.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 70.4, 'Availability (%)': 99.7},
    {'Mes': 'Agosto', 'Call Date': '2025-08-27', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 731.2, 'PS & Compliance (%)': 100.0, 'RTA (%)': 75.7, 'Availability (%)': 99.9},
    {'Mes': 'Agosto', 'Call Date': '2025-08-28', 'HANDLED': 28, 'OIR (%)': 100.0, 'AHT (seg)': 767.8, 'PS & Compliance (%)': 0.0, 'RTA (%)': 89.5, 'Availability (%)': 99.9},
    {'Mes': 'Agosto', 'Call Date': '2025-08-29', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 600.9, 'PS & Compliance (%)': 87.5, 'RTA (%)': 80.4, 'Availability (%)': 99.4},
    {'Mes': 'Agosto', 'Call Date': '2025-08-30', 'HANDLED': 5, 'OIR (%)': 95.0, 'AHT (seg)': 550.0, 'PS & Compliance (%)': 0.0, 'RTA (%)': 5.0, 'Availability (%)': 5.0},
    {'Mes': 'Agosto', 'Call Date': '2025-08-31', 'HANDLED': 50, 'OIR (%)': 93.0, 'AHT (seg)': 550.0, 'PS & Compliance (%)': 0.0, 'RTA (%)': 0.0, 'Availability (%)': 0.0},

    # Septiembre
    {'Mes': 'Septiembre', 'Call Date': '2025-09-01', 'HANDLED': 33, 'OIR (%)': 91.0, 'AHT (seg)': 640.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 75.0, 'Availability (%)': 95.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-02', 'HANDLED': 30, 'OIR (%)': 94.0, 'AHT (seg)': 620.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 78.0, 'Availability (%)': 96.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-03', 'HANDLED': 36, 'OIR (%)': 93.0, 'AHT (seg)': 650.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 80.0, 'Availability (%)': 94.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-04', 'HANDLED': 32, 'OIR (%)': 95.0, 'AHT (seg)': 630.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 82.0, 'Availability (%)': 97.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-05', 'HANDLED': 38, 'OIR (%)': 90.0, 'AHT (seg)': 660.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 77.0, 'Availability (%)': 95.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-06', 'HANDLED': 34, 'OIR (%)': 96.0, 'AHT (seg)': 640.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 79.0, 'Availability (%)': 96.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-07', 'HANDLED': 31, 'OIR (%)': 92.0, 'AHT (seg)': 670.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 81.0, 'Availability (%)': 94.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-08', 'HANDLED': 35, 'OIR (%)': 94.0, 'AHT (seg)': 625.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 83.0, 'Availability (%)': 97.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-09', 'HANDLED': 37, 'OIR (%)': 93.0, 'AHT (seg)': 655.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 76.0, 'Availability (%)': 95.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-10', 'HANDLED': 33, 'OIR (%)': 95.0, 'AHT (seg)': 645.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 80.0, 'Availability (%)': 96.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-10', 'HANDLED': 34, 'OIR (%)': 100.0, 'AHT (seg)': 609.2, 'PS & Compliance (%)': 33.3, 'RTA (%)': 89.6, 'Availability (%)': 99.9},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-11', 'HANDLED': 25, 'OIR (%)': 100.0, 'AHT (seg)': 572.4, 'PS & Compliance (%)': 100.0, 'RTA (%)': 25.6, 'Availability (%)': 96.9},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-13', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 713.6, 'PS & Compliance (%)': 50.0, 'RTA (%)': 94.3, 'Availability (%)': 99.7},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-14', 'HANDLED': 19, 'OIR (%)': None, 'AHT (seg)': 306.2, 'PS & Compliance (%)': None, 'RTA (%)': 85.0, 'Availability (%)': 100.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-15', 'HANDLED': None, 'OIR (%)': None, 'AHT (seg)': None, 'PS & Compliance (%)': None, 'RTA (%)': None, 'Availability (%)': None},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-16', 'HANDLED': 23, 'OIR (%)': 100.0, 'AHT (seg)': 904.2, 'PS & Compliance (%)': 50.0, 'RTA (%)': 87.5, 'Availability (%)': 99.2},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-17', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 598.4, 'PS & Compliance (%)': None, 'RTA (%)': 89.5, 'Availability (%)': 99.8},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-22', 'HANDLED': 32, 'OIR (%)': 100.0, 'AHT (seg)': 794.7, 'PS & Compliance (%)': 87.5, 'RTA (%)': 72.5, 'Availability (%)': 94.4},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-09', 'HANDLED': 27, 'OIR (%)': 100.0, 'AHT (seg)': 740.4, 'PS & Compliance (%)': None, 'RTA (%)': 85.2, 'Availability (%)': 100.0},
]

# =============================================================================
# 2. ORDENAMIENTO DE DATOS POR FECHA
# =============================================================================

def parse_date(row):
    """
    Convierte la fecha de string a objeto datetime para ordenamiento.
    
    Args:
        row (dict): Diccionario con datos de una fila que contiene 'Call Date'
        
    Returns:
        datetime: Objeto datetime de la fecha o datetime.min si hay error
    """
    try:
        return datetime.strptime(row['Call Date'], "%Y-%m-%d")
    except Exception:
        return datetime.min

# Ordena los datos diarios por mes y fecha (útil cuando se agregan datos nuevos)
daily_data = sorted(daily_data, key=lambda x: (x['Mes'], parse_date(x)))

# =============================================================================
# 3. CONFIGURACIÓN DE DATOS DEL EQUIPO (MÉTRICAS POR EMPLEADO)
# =============================================================================
# Datos del equipo con métricas de rendimiento individual
# Cada métrica se mide como porcentaje (%) excepto AHT que está en segundos
data_equipo = {
    'Empleado': [
        'Christian Velasco Navarro', 'Teresa Cervantes', 'Carlos Miguel', 'Torre Roberto', 'De La Cruz Paola',
        'Ramiro Partida', 'Villela Stefania', 'Izaguirre Itzel', 'Silva Bernal', 'Delgado Rafael',
        'Velasco Estrada', 'Gabriel Araceli', 'Soriano Madriz', 'Alvarez Danila'
    ],
    # OIR: Offer and Information Rate (%)
    'OIR (%)': [95.12, 94.76, 93.53, 93.90, 93.65, 92.49, 98.31, 81.98, 70.0, 100.0, 100.0, 93.85, 92.81, 83.33],
    # Porcentaje de tiempo en silencio durante llamadas
    'Silence Percentage (%)': [38.4, 47.6, 42.6, 45.5, 38.98, 34.0, 41.7, 38.47, 45.0, 45.02, 48.0, 49.0, 46.32, 51.18],
    # CCA: Customer Care Advocacy (%)
    'CCA (%)': [75.2, 98.0, 100.0, 100.0, 80.77, 85.33, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
    # CARE: Índice de cuidado al cliente (%)
    'CARE (%)': [7.36, 0.0, 8.58, 10.0, 6.36, 7.32, 10.0, 5.77, 4.67, 1.0, 0.0, 3.87, 0.7, 0.0],
    # NICE TOUR: Métrica de evaluación de servicio (%)
    'NICE TOUR (%)': [70.5, 75.0, 84.33, 71.38, 82.14, 63.30, 50.0, 85.0, 95.83, 75.0, 73.44, 95.10, 90.0, 90.0],
    # QA: Quality Assurance (%)
    'QA (%)': [85.0, 90.0, 90.5, 70.52, 52.0, 67.0, 100.0, 87.22, 100.0, 100.0, 100.0, 92.5, 95.0, 70.0],
    # ACS Score: American Customer Satisfaction Score (%)
    'ACS Score (%)': [89.0, 90.0, 94.4, 97.3, 70.5, 100.0, 100.0, 84.8, 0.0, 100.0, 90.7, 92.3, 85.33, 83.33],
    # Disponibilidad del agente (%)
    'Availability (%)': [96.51, 99.49, 99.79, 99.28, 95.96, 99.96, 98.31, 98.79, 99.74, 95.29, 99.83, 99.78, 83.35, 93.0],
    # RTA: Real Time Adherence - Adherencia al horario (%)
    'RTA (%)': [82.94, 93.3, 88.42, 84.33, 83.06, 65.96, 82.31, 70.72, 80.96, 100.0, 73.1, 70.0, 75.0, 66.0],
    # PS & Compliance: Professional Standards & Compliance (%)
    'PS & Compliance (%)': [86.16, 88.4, 93.28, 84.55, 83.27, 90.16, 86.33, 44.95, 98.57, 91.67, 100.0, 82.79, 85.7, 82.67],
    # AHT: Average Handle Time (segundos)
    'AHT': [633, 655.7, 637.8, 922.8, 606.3, 890, 772.5, 609.9, 506.6, 486, 450, 440, 384, 381]
}

# Convierte los datos del equipo a DataFrame de pandas para manipulación
df_equipo = pd.DataFrame(data_equipo)

# =============================================================================
# 4. DEFINICIÓN DE METAS Y OBJETIVOS POR MÉTRICA
# =============================================================================
# Valores objetivo para cada métrica - utilizados para formato condicional tipo semáforo
# Verde: Cumple objetivo, Amarillo: Cerca del objetivo, Rojo: Lejos del objetivo
metas = {
    'OIR (%)': 90.0,                    # Objetivo: >= 90%
    'AHT (seg)': 630.0,                 # Objetivo: <= 630 segundos (menor es mejor)
    'QA (%)': 85.0,                     # Objetivo: >= 85%
    'ACS (%)': 70.0,                    # Objetivo: >= 70%
    'PS & Compliance (%)': 80.0,        # Objetivo: >= 80%
    'RTA (%)': 85.0,                    # Objetivo: >= 85%
    'CCA (%)': 90.0,                    # Objetivo: >= 90%
    'CARE (%)': 5.0,                    # Objetivo: <= 5% (menor es mejor)
    'NICE TOUR (%)': 80.0,              # Objetivo: >= 80%
    'ACS Score (%)': 85.0,              # Objetivo: >= 85%
    'Silence Percentage (%)': 40.0      # Objetivo: <= 40% (menor es mejor)
}

# =============================================================================
# 5. FUNCIONES AUXILIARES Y UTILIDADES
# =============================================================================
def excel_col_letter(col_idx):
    """
    Convierte un índice de columna numérico a su letra correspondiente en Excel.
    
    Args:
        col_idx (int): Índice de columna (0=A, 1=B, 2=C, etc.)
        
    Returns:
        str: Letra de columna de Excel (A, B, C, ..., Z, AA, AB, etc.)
        
    Ejemplos:
        excel_col_letter(0) -> 'A'
        excel_col_letter(25) -> 'Z'
        excel_col_letter(26) -> 'AA'
    """
    return xl_col_to_name(col_idx)

# =============================================================================
# 6. CONFIGURACIÓN DEL ARCHIVO DE SALIDA
# =============================================================================
# Nombre del archivo Excel que se generará
output_file = r'Reporte_Metricas_Christian_modified.xlsx'

# =============================================================================
# 7. PROCESO PRINCIPAL: GENERACIÓN DEL REPORTE EXCEL
# =============================================================================

def main():
    """
    Función principal que genera el reporte de métricas en Excel.
    
    Crea un archivo Excel con dos hojas:
    1. Daily_Data: Métricas diarias organizadas por mes
    2. Team_August: Métricas del equipo con rankings y análisis
    
    Incluye:
    - Formateo condicional tipo semáforo
    - Tablas con estilos profesionales
    - Gráficos de tendencias y rankings
    - Cálculos automáticos de promedios
    """
    print("🚀 Iniciando generación del reporte de métricas...")
    
    try:
        with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
            workbook = writer.book

            # =================================================================
            # CONFIGURACIÓN DE FORMATOS DE CELDA
            # =================================================================
            print("📊 Configurando formatos de celda...")
            
            # Formato para encabezados de tabla
            fmt_header = workbook.add_format({
                'bold': True, 'bg_color': '#4F81BD', 'font_color': 'white',
                'align': 'center', 'font_size': 12, 'border': 1
            })
            
            # Formato para texto en negrita
            fmt_bold = workbook.add_format({'bold': True, 'font_size': 11})
            
            # Formato para números enteros
            fmt_int = workbook.add_format({'num_format': '0', 'font_size': 11})
            fmt_round0 = workbook.add_format({'num_format': '0', 'font_size': 11})

            # Formatos para semáforo (formato condicional)
            fmt_dark_green = workbook.add_format({'bg_color': '#008000', 'font_size': 11, 'font_color': 'white'})
            fmt_light_green = workbook.add_format({'bg_color': '#90EE90', 'font_size': 11})
            fmt_yellow = workbook.add_format({'bg_color': '#FFFF00', 'font_size': 11})
            fmt_red = workbook.add_format({'bg_color': '#FF0000', 'font_size': 11, 'font_color': 'white'})

            def add_traffic_light(ws, col_idx, target, menor_mejor=False, first_row=1, last_row=None):
                """
                Aplica formato condicional tipo semáforo a una columna de Excel.
                
                Args:
                    ws: Hoja de trabajo (worksheet) de Excel
                    col_idx (int): Índice de la columna (0, 1, 2, ...)
                    target (float): Valor objetivo/meta para la métrica
                    menor_mejor (bool): True si valores menores son mejores (ej: AHT, CARE)
                    first_row (int): Primera fila para aplicar formato
                    last_row (int): Última fila para aplicar formato
                    
                Colores:
                    - Verde oscuro: Cumple completamente el objetivo
                    - Verde claro: Cerca del objetivo (95% o 105% según sea mayor/menor mejor)
                    - Amarillo: Moderadamente alejado (90% o 115% según sea mayor/menor mejor)
                    - Rojo: Muy alejado del objetivo
                """
                if last_row is None:
                    last_row = ws.dim_rowmax
                    
                col_letter = excel_col_letter(col_idx)
                rng = f'{col_letter}{first_row+1}:{col_letter}{last_row+1}'
                
                if menor_mejor:
                    # Para métricas donde menor es mejor (ej: AHT, CARE)
                    ws.conditional_format(rng, {
                        'type': 'cell', 'criteria': '<=', 'value': target, 
                        'format': fmt_dark_green
                    })
                    ws.conditional_format(rng, {
                        'type': 'cell', 'criteria': '<=', 'value': target*1.05, 
                        'format': fmt_light_green
                    })
                    ws.conditional_format(rng, {
                        'type': 'cell', 'criteria': '<=', 'value': target*1.15, 
                        'format': fmt_yellow
                    })
                    ws.conditional_format(rng, {
                        'type': 'cell', 'criteria': '>', 'value': target*1.15, 
                        'format': fmt_red
                    })
                else:
                    # Para métricas donde mayor es mejor (ej: OIR, QA, RTA)
                    ws.conditional_format(rng, {
                        'type': 'cell', 'criteria': '>=', 'value': target, 
                        'format': fmt_dark_green
                    })
                    ws.conditional_format(rng, {
                        'type': 'cell', 'criteria': '>=', 'value': target*0.95, 
                        'format': fmt_light_green
                    })
                    ws.conditional_format(rng, {
                        'type': 'cell', 'criteria': '>=', 'value': target*0.9, 
                        'format': fmt_yellow
                    })
                    ws.conditional_format(rng, {
                        'type': 'cell', 'criteria': '<', 'value': target*0.9, 
                        'format': fmt_red
                    })

            # =================================================================
            # HOJA 1: DATOS DIARIOS (DAILY_DATA)
            # =================================================================
            print("📅 Generando hoja de datos diarios...")
            
            sheet_daily = 'Daily_Data'
            ws = workbook.add_worksheet(sheet_daily)
            writer.sheets[sheet_daily] = ws

            # Convierte datos diarios a DataFrame y agrupa por mes
            df_daily = pd.DataFrame(daily_data)
            grouped = df_daily.groupby('Mes')
            current_row = 0
            
            # Estilos de tabla para alternar entre meses
            styles = [
                'Table Style Medium 9', 'Table Style Medium 2', 
                'Table Style Medium 3', 'Table Style Medium 4'
            ]
            i = 0

            for mes, df_group in grouped:
                print(f"  📊 Procesando mes: {mes}")
                
                # Remueve la columna 'Availability (%)' de la vista diaria
                df_group2 = df_group.drop(columns=['Availability (%)'], errors='ignore').copy()

                # Escribe encabezado del mes
                ws.write(current_row, 0, f'Mes: {mes}', fmt_header)
                current_row += 1

                # Escribe los datos del grupo en la hoja
                df_group2.to_excel(writer, sheet_name=sheet_daily, index=False, 
                                 startrow=current_row, header=True)

                rows_group = len(df_group2)
                cols = len(df_group2.columns)
                last_col = cols - 1

                # Crea tabla Excel con formato profesional
                table_range = f'A{current_row+1}:{excel_col_letter(last_col)}{current_row + rows_group +1}'
                columns = [{'header': c} for c in df_group2.columns]
                ws.add_table(table_range, {
                    'columns': columns, 
                    'style': styles[i % len(styles)]
                })

                # Agrega fila de promedio (redondeado a entero)
                avg_row = current_row + rows_group + 2
                ws.write(avg_row-1, 0, 'Average', fmt_bold)
                
                for cidx, col in enumerate(df_group2.columns):
                    if pd.api.types.is_numeric_dtype(df_group2[col]):
                        col_letter = excel_col_letter(cidx)
                        start = current_row + 2
                        end = current_row + rows_group + 1
                        formula = f'=ROUND(AVERAGE({col_letter}{start}:{col_letter}{end}),0)'
                        ws.write_formula(avg_row-1, cidx, formula)

                # Ajusta ancho de columnas automáticamente
                for j, col in enumerate(df_group2.columns):
                    max_len = max(df_group2[col].astype(str).map(len).max(), len(col)) + 4
                    ws.set_column(j, j, max_len)

                # Aplica formato condicional semáforo a métricas clave
                daily_col_map_group = {c: j for j, c in enumerate(df_group2.columns)}
                semaforo_metrics = [
                    ('OIR (%)', False),           # Mayor es mejor
                    ('AHT (seg)', True),          # Menor es mejor  
                    ('PS & Compliance (%)', False), # Mayor es mejor
                    ('RTA (%)', False)            # Mayor es mejor
                ]
                
                for metric, menor_mejor in semaforo_metrics:
                    if metric in metas and metric in daily_col_map_group:
                        add_traffic_light(
                            ws, daily_col_map_group[metric], metas[metric], 
                            menor_mejor=menor_mejor, first_row=current_row, 
                            last_row=current_row + rows_group
                        )

                # Agrega mini-gráfico de tendencia OIR vs AHT para cada mes
                if all(col in df_group2.columns for col in ['OIR (%)', 'AHT (seg)', 'Call Date']):
                    print(f"  📈 Creando gráfico de tendencias para {mes}")
                    
                    idx_date = df_group2.columns.get_loc('Call Date')
                    idx_oir = df_group2.columns.get_loc('OIR (%)')
                    idx_aht = df_group2.columns.get_loc('AHT (seg)')
                    
                    chart = workbook.add_chart({'type': 'line'})
                    chart.add_series({
                        'name': 'OIR (%)',
                        'categories': [sheet_daily, current_row+1, idx_date, current_row+rows_group, idx_date],
                        'values': [sheet_daily, current_row+1, idx_oir, current_row+rows_group, idx_oir],
                    })
                    chart.add_series({
                        'name': 'AHT (seg)',
                        'categories': [sheet_daily, current_row+1, idx_date, current_row+rows_group, idx_date],
                        'values': [sheet_daily, current_row+1, idx_aht, current_row+rows_group, idx_aht],
                        'y2_axis': True  # Segundo eje Y para AHT
                    })
                    
                    chart.set_title({'name': f'{mes}: Tendencia OIR vs AHT'})
                    chart.set_x_axis({'name': 'Fecha'})
                    chart.set_y_axis({'name': 'OIR (%)'})
                    chart.set_y2_axis({'name': 'AHT (segundos)'})
                    chart.set_size({'width': 480, 'height': 300})
                    
                    # Inserta gráfico a la derecha de los datos
                    insert_col = last_col + 2
                    insert_cell = f'{excel_col_letter(insert_col)}{current_row+1}'
                    ws.insert_chart(insert_cell, chart)

                # Espacio antes del siguiente mes
                current_row = avg_row + 2
                i += 1

            # =================================================================
            # HOJA 2: ANÁLISIS DEL EQUIPO (TEAM_AUGUST)
            # =================================================================
            print("👥 Generando hoja de análisis del equipo...")
            
            sheet_team = 'Team_August'
            # Remueve métricas específicas para enfocarse en las más relevantes
            df_team2 = df_equipo.drop(
                columns=['Availability (%)', 'AHT', 'Silence Percentage (%)'], 
                errors='ignore'
            ).copy()
            
            df_team2.to_excel(writer, sheet_name=sheet_team, index=False, startrow=0)
            ws_t = writer.sheets[sheet_team]
            r_t, c_t = df_team2.shape
            last_col_t = c_t - 1

            # Crea tabla principal del equipo
            table_range_t = f'A1:{excel_col_letter(last_col_t)}{r_t+1}'
            columns_t = [{'header': c} for c in df_team2.columns]
            ws_t.add_table(table_range_t, {
                'columns': columns_t, 
                'style': 'Table Style Medium 9'
            })

            # Agrega fila de promedio del equipo
            avg_row_t = r_t + 2
            ws_t.write(avg_row_t-1, 0, 'Team Average', fmt_bold)
            
            for cidx, col in enumerate(df_team2.columns):
                if pd.api.types.is_numeric_dtype(df_team2[col]):
                    col_letter = excel_col_letter(cidx)
                    formula = f'=ROUND(AVERAGE({col_letter}2:{col_letter}{r_t+1}),1)'
                    ws_t.write_formula(avg_row_t-1, cidx, formula)

            # Ajusta ancho de columnas automáticamente
            for i_col, col in enumerate(df_team2.columns):
                max_len = max(df_team2[col].astype(str).map(len).max(), len(col)) + 4
                ws_t.set_column(i_col, i_col, max_len)

            # Aplica formato condicional semáforo a todas las métricas del equipo
            print("  🚦 Aplicando formato condicional semáforo...")
            
            for cidx, col in enumerate(df_team2.columns):
                if col in metas:
                    # Determina si menor es mejor para esta métrica
                    menor_mejor = col in ['CARE (%)']
                    add_traffic_light(
                        ws_t, cidx, metas[col], 
                        menor_mejor=menor_mejor, first_row=1, last_row=r_t
                    )

            # Crea gráfico de ranking por OIR
            if 'OIR (%)' in df_team2.columns:
                print("  📊 Creando gráfico de ranking OIR...")
                
                chart_team = workbook.add_chart({'type': 'bar'})
                chart_team.add_series({
                    'name': 'OIR (%)',
                    'categories': [sheet_team, 1, 0, r_t, 0],  # Nombres de empleados
                    'values': [sheet_team, 1, df_team2.columns.get_loc('OIR (%)'), 
                              r_t, df_team2.columns.get_loc('OIR (%)')]
                })
                
                chart_team.set_title({'name': 'Ranking del Equipo por OIR (%)'})
                chart_team.set_x_axis({'name': 'OIR (%)', 'min': 0, 'max': 100})
                chart_team.set_y_axis({'name': 'Empleados'})
                chart_team.set_size({'width': 720, 'height': 400})
                
                # Posiciona el gráfico a la derecha de los datos
                ws_t.insert_chart('P2', chart_team)

        print(f"✅ Archivo Excel generado exitosamente: {output_file}")
        print(f"📂 Ubicación: {output_file}")
        print("🎉 ¡Proceso completado!")

    except PermissionError as e:
        print("❌ ERROR DE PERMISOS:")
        print(f"   No se puede escribir en el archivo '{output_file}'")
        print("💡 SOLUCIONES:")
        print("   1. Cierra el archivo Excel si está abierto")
        print("   2. Verifica que tengas permisos de escritura en la carpeta")
        print("   3. Cambia la variable 'output_file' a otra ubicación")
        print(f"   📋 Detalles técnicos: {e}")
        return False

    except Exception as e:
        print("❌ ERROR INESPERADO:")
        print(f"   {str(e)}")
        print("💡 SUGERENCIAS:")
        print("   - Verifica que todas las librerías estén instaladas")
        print("   - Revisa que los datos estén en el formato correcto")
        print("   - Contacta al administrador del sistema si persiste")
        return False
    
    return True

# =============================================================================
# 8. EJECUCIÓN DEL PROGRAMA PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    
    Ejecuta la función main() y maneja el resultado de la operación.
    """
    print("=" * 60)
    print("📊 SISTEMA DE REPORTES DE MÉTRICAS - PANERA BREAD")
    print("   Generador Automatizado de Reportes Excel")
    print("=" * 60)
    
    success = main()
    
    if success:
        print("\n" + "=" * 60)
        print("🎊 REPORTE GENERADO CORRECTAMENTE")
        print("   El archivo Excel está listo para su uso")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("💥 ERROR EN LA GENERACIÓN DEL REPORTE")
        print("   Revisa los mensajes anteriores para más detalles")
        print("=" * 60)

# =============================================================================
# FIN DEL SCRIPT
# =============================================================================