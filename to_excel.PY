# to_excel_
# Ejecuta dentro de tu venv en Windows:
#   .\venv\Scripts\Activate.ps1


import pandas as pd
import math
from xlsxwriter.utility import xl_col_to_name

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
    {'Mes': 'Abril', 'Call Date': '2025-04-21', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 572.3, 'PS & Compliance (%)': 100.0, 'RTA (%)': 91.7, 'Availability (%)': 99.7},
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
    {'Mes': 'Mayo', 'Call Date': '2025-05-08', 'HANDLED': 30, 'OIR (%)': 100.0, 'AHT (seg)': 490.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 79.0, 'Availability (%)': 99.9},
    {'Mes': 'Mayo', 'Call Date': '2025-05-09', 'HANDLED': 34, 'OIR (%)': 100.0, 'AHT (seg)': 515.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 81.0, 'Availability (%)': 99.7},
    {'Mes': 'Mayo', 'Call Date': '2025-05-10', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 505.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 84.0, 'Availability (%)': 99.8},
    {'Mes': 'Mayo', 'Call Date': '2025-05-11', 'HANDLED': 37, 'OIR (%)': 100.0, 'AHT (seg)': 525.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 87.0, 'Availability (%)': 99.6},
    {'Mes': 'Mayo', 'Call Date': '2025-05-12', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 495.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 80.0, 'Availability (%)': 99.9},
    {'Mes': 'Mayo', 'Call Date': '2025-05-06', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 527.3, 'PS & Compliance (%)': 100.0, 'RTA (%)': 80.1, 'Availability (%)': 99.8},
    {'Mes': 'Mayo', 'Call Date': '2025-05-07', 'HANDLED': 10, 'OIR (%)': 100.0, 'AHT (seg)': 414.2, 'PS & Compliance (%)': 100.0, 'RTA (%)': 50.6, 'Availability (%)': 99.8},
    {'Mes': 'Mayo', 'Call Date': '2025-05-13', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 353.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 70.4, 'Availability (%)': 99.9},
    {'Mes': 'Mayo', 'Call Date': '2025-05-14', 'HANDLED': 44, 'OIR (%)': 100.0, 'AHT (seg)': 361.1, 'PS & Compliance (%)': 100.0, 'RTA (%)': 75.8, 'Availability (%)': 99.8},
    {'Mes': 'Mayo', 'Call Date': '2025-05-15', 'HANDLED': 30, 'OIR (%)': 100.0, 'AHT (seg)': 427.8, 'PS & Compliance (%)': 100.0, 'RTA (%)': 89.6, 'Availability (%)': 100.0},
    {'Mes': 'Mayo', 'Call Date': '2025-05-16', 'HANDLED': 37, 'OIR (%)': 100.0, 'AHT (seg)': 600.9, 'PS & Compliance (%)': 100.0, 'RTA (%)': 80.4, 'Availability (%)': 99.9},

    # Junio
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
    {'Mes': 'Junio', 'Call Date': '2025-06-21', 'HANDLED': 42, 'OIR (%)': 100.0, 'AHT (seg)': 550.5, 'PS & Compliance (%)': 87.5, 'RTA (%)': 92.1, 'Availability (%)': 99.8},
    {'Mes': 'Junio', 'Call Date': '2025-06-22', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 426.5, 'PS & Compliance (%)': 100.0, 'RTA (%)': 89.2, 'Availability (%)': 99.8},
    {'Mes': 'Junio', 'Call Date': '2025-06-23', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 784.6, 'PS & Compliance (%)': 100.0, 'RTA (%)': 82.7, 'Availability (%)': 99.4},
    {'Mes': 'Junio', 'Call Date': '2025-06-24', 'HANDLED': 24, 'OIR (%)': 100.0, 'AHT (seg)': 684.6, 'PS & Compliance (%)': 100.0, 'RTA (%)': 73.5, 'Availability (%)': 99.0},
    {'Mes': 'Junio', 'Call Date': '2025-06-25', 'HANDLED': 30, 'OIR (%)': 100.0, 'AHT (seg)': 706.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 92.8, 'Availability (%)': 99.0},
    {'Mes': 'Junio', 'Call Date': '2025-06-26', 'HANDLED': 35, 'OIR (%)': 100.0, 'AHT (seg)': 461.3, 'PS & Compliance (%)': 100.0, 'RTA (%)': 85.3, 'Availability (%)': 99.0},
    {'Mes': 'Junio', 'Call Date': '2025-06-28', 'HANDLED': 40, 'OIR (%)': 100.0, 'AHT (seg)': 529.1, 'PS & Compliance (%)': 100.0, 'RTA (%)': 94.9, 'Availability (%)': 99.9},

    # Julio
    {'Mes': 'Junio', 'Call Date': '2025-06-01', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 540.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 90.0, 'Availability (%)': 99.7},
    {'Mes': 'Junio', 'Call Date': '2025-06-02', 'HANDLED': 32, 'OIR (%)': 100.0, 'AHT (seg)': 530.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 88.0, 'Availability (%)': 99.8},
    {'Mes': 'Junio', 'Call Date': '2025-06-03', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 560.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 85.0, 'Availability (%)': 99.6},
    {'Mes': 'Junio', 'Call Date': '2025-06-04', 'HANDLED': 30, 'OIR (%)': 100.0, 'AHT (seg)': 520.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 91.0, 'Availability (%)': 99.9},
    {'Mes': 'Junio', 'Call Date': '2025-06-05', 'HANDLED': 35, 'OIR (%)': 100.0, 'AHT (seg)': 550.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 93.0, 'Availability (%)': 99.7},
    {'Mes': 'Junio', 'Call Date': '2025-06-06', 'HANDLED': 34, 'OIR (%)': 100.0, 'AHT (seg)': 535.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 87.0, 'Availability (%)': 99.8},
    {'Mes': 'Junio', 'Call Date': '2025-06-07', 'HANDLED': 37, 'OIR (%)': 100.0, 'AHT (seg)': 545.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 89.0, 'Availability (%)': 99.6},
    {'Mes': 'Junio', 'Call Date': '2025-06-08', 'HANDLED': 33, 'OIR (%)': 100.0, 'AHT (seg)': 525.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 92.0, 'Availability (%)': 99.9},
    {'Mes': 'Junio', 'Call Date': '2025-06-09', 'HANDLED': 36, 'OIR (%)': 100.0, 'AHT (seg)': 570.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 86.0, 'Availability (%)': 99.7},
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
    {'Mes': 'Agosto', 'Call Date': '2025-08-04', 'HANDLED': 30, 'OIR (%)': 96.0, 'AHT (seg)': 580.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 91.0, 'Availability (%)':99.6}, 
    {'Mes': 'Agosto', 'Call Date': '2025-08-05', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 630.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 93.0,'Availability (%)': 99.7},
    {'Mes': 'Agosto', 'Call Date': '2025-08-07', 'HANDLED': 37, 'OIR (%)': 100.0, 'AHT (seg)': 615.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 88.0, 'Availability (%)': 99.6},
    {'Mes': 'Agosto', 'Call Date': '2025-08-08', 'HANDLED':35, 'OIR (%)': 99.0, 'AHT (seg)': 595.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 90.0, 'Availability (%)': 100.0},
    {'Mes': 'Agosto', 'Call Date': '2025-08-09', 'HANDLED': 31, 'OIR (%)': 100.0, 'AHT (seg)': 605.0, 'PS & Compliance (%)': 75.0, 'RTA (%)': 84.0, 'Availability (%)': 99.7},
    {'Mes': 'Agosto', 'Call Date': '2025-08-10', 'HANDLED': 34, 'OIR (%)': 98.0, 'AHT (seg)': 585.0, 'PS & Compliance (%)': 100.0, 'RTA (%)': 92.0, 'Availability (%)': 99.8},
    {'Mes': 'Agosto', 'Call Date': '2025-08-23', 'HANDLED': 38, 'OIR (%)': 100.0, 'AHT (seg)': 620.1, 'PS & Compliance (%)': 0.0, 'RTA (%)': 92.8, 'Availability (%)': 99.7},
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
    {'Mes': 'Septiembre', 'Call Date': '2025-09-22', 'HANDLED': 32, 'OIR (%)': 100.0, 'AHT (seg)': 794.7, 'PS & Compliance (%)': 87.5, 'RTA (%)': 72.5, 'Availability (%)': 94.4},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-23', 'HANDLED': 15, 'OIR (%)': 100.0, 'AHT (seg)': 981.1, 'PS & Compliance (%)': 25.0, 'RTA (%)': 92.3, 'Availability (%)': 94.8},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-25', 'HANDLED': 18, 'OIR (%)': 100.0, 'AHT (seg)': 845.4, 'PS & Compliance (%)': 0.0, 'RTA (%)': 80.4, 'Availability (%)': 98.1},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-26', 'HANDLED': 35, 'OIR (%)': 100.0, 'AHT (seg)': 524.6, 'PS & Compliance (%)': 50.0, 'RTA (%)': 79.7, 'Availability (%)': 97.9},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-27', 'HANDLED': 44, 'OIR (%)': 90.0, 'AHT (seg)': 445.0, 'PS & Compliance (%)': 70.0, 'RTA (%)': 84.0, 'Availability (%)': 0.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-28', 'HANDLED': 40, 'OIR (%)': 95.0, 'AHT (seg)': 754.0, 'PS & Compliance (%)': 74.0, 'RTA (%)': 84.0, 'Availability (%)': 4.0},
    {'Mes': 'Septiembre', 'Call Date': '2025-09-30', 'HANDLED': 40, 'OIR (%)': 92.0, 'AHT (seg)': 475.0, 'PS & Compliance (%)': 74.0, 'RTA (%)': 84.0, 'Availability (%)': 4.0}
]

df_daily = pd.DataFrame(daily_data)

# Datos mensuales

data_monthly = {
    'Mes': ['Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre'],
    'HANDLED': [320, 310, 300, 290, 280, 270],
    'OIR (%)': [94.67, 96.15, 86.67, 96.15, 96.75, 92.0],
    'AHT (seg)': [567.1, 459.0, 459.0, 498.9, 629.0, 650.0],
    'QA (%)': [81.0, 80.0, 83.0, 73.0, 81.1, 87.5],
    'PS & Compliance (%)': [79.0, 74.14, 87.57, 91.3, 74.1, 75.0],
    'RTA (%)': [89.9, 99.81, 99.87, 98.3, 99.1, 95.0]
}

df_monthly = pd.DataFrame(data_monthly)

# Datos equipo - removed 'CS (%)'
data_equipo = {
    'Empleado': [
        'Christian Velasco Navarro', 'Teresa Cervantes', 'Carlos Miguel', 'Torre Roberto', 'De La Cruz Paola',
        'Ramiro Partida', 'Villela Stefania', 'Izaguirre Itzel', 'Silva Bernal', 'Delgado Rafael',
        'Velasco Estrada', 'Gabriel Araceli', 'Soriano Madriz', 'Alvarez Danila'
    ],
    'OIR (%)': [95.12, 94.76, 93.53, 93.90, 93.65, 92.49, 98.31, 81.98, 70.0, 100.0, 100.0, 93.85, 92.81, 83.33],
    'Silence Percentage (%)': [38.4, 47.6, 42.6, 45.5, 38.98, 34.0, 41.7, 38.47, 45.0, 45.02, 48.0, 49.0, 46.32, 51.18],
    'CCA (%)': [75.2, 98.0, 100.0, 100.0, 80.77, 85.33, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
    'CARE (%)': [7.36, 0.0, 8.58, 10.0, 6.36, 7.32, 10.0, 5.77, 4.67, 1.0, 0.0, 3.87, 0.7, 0.0],
    'NICE TOUR (%)': [70.5, 75.0, 84.33, 71.38, 82.14, 63.30, 50.0, 85.0, 95.83, 75.0, 73.44, 95.10, 90.0, 90.0],
    'QA (%)': [85.0, 90.0, 90.5, 70.52, 52.0, 67.0, 100.0, 87.22, 100.0, 100.0, 100.0, 92.5, 95.0, 70.0],
    'ACS Score (%)': [89.0, 90.0, 94.4, 97.3, 70.5, 100.0, 100.0, 84.8, 0.0, 100.0, 90.7, 92.3, 85.33, 83.33],
    'Availability (%)': [96.51, 99.49, 99.79, 99.28, 95.96, 99.96, 98.31, 98.79, 99.74, 95.29, 99.83, 99.78, 83.35, 93.0],
    'RTA (%)': [82.94, 93.3, 88.42, 84.33, 83.06, 65.96, 82.31, 70.72, 80.96, 100.0, 73.1, 70.0, 75.0, 66.0],
    'PS & Compliance (%)': [86.16, 88.4, 93.28, 84.55, 83.27, 90.16, 86.33, 44.95, 98.57, 91.67, 100.0, 82.79, 85.7, 82.67],
    'AHT': [633, 655.7, 637.8, 922.8, 606.3, 890, 772.5, 609.9, 506.6, 486, 450, 440, 384, 381]
}

df_daily = pd.DataFrame(daily_data)

# Datos mensuales

data_monthly = {
    'Mes': ['Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre'],
    'HANDLED': [320, 310, 300, 290, 280, 270],
    'OIR (%)': [94.67, 96.15, 86.67, 96.15, 96.75, 92.0],
    'AHT (seg)': [567.1, 459.0, 459.0, 498.9, 629.0, 650.0],
    'QA (%)': [81.0, 80.0, 83.0, 73.0, 81.1, 87.5],
    'PS & Compliance (%)': [79.0, 74.14, 87.57, 91.3, 74.1, 75.0],
    'RTA (%)': [89.9, 99.81, 99.87, 98.3, 99.1, 95.0]
}

df_monthly = pd.DataFrame(data_monthly)

# Datos equipo - removed 'CS (%)'
data_equipo = {
    'Empleado': [
        'Christian Velasco Navarro', 'Teresa Cervantes', 'Carlos Miguel', 'Torre Roberto', 'De La Cruz Paola',
        'Ramiro Partida', 'Villela Stefania', 'Izaguirre Itzel', 'Silva Bernal', 'Delgado Rafael',
        'Velasco Estrada', 'Gabriel Araceli', 'Soriano Madriz', 'Alvarez Danila'
    ],
    'OIR (%)': [95.12, 94.76, 93.53, 93.90, 93.65, 92.49, 98.31, 81.98, 70.0, 100.0, 100.0, 93.85, 92.81, 83.33],
    'Silence Percentage (%)': [38.4, 47.6, 42.6, 45.5, 38.98, 34.0, 41.7, 38.47, 45.0, 45.02, 48.0, 49.0, 46.32, 51.18],
    'CCA (%)': [75.2, 98.0, 100.0, 100.0, 80.77, 85.33, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
    'CARE (%)': [7.36, 0.0, 8.58, 10.0, 6.36, 7.32, 10.0, 5.77, 4.67, 1.0, 0.0, 3.87, 0.7, 0.0],
    'NICE TOUR (%)': [70.5, 75.0, 84.33, 71.38, 82.14, 63.30, 50.0, 85.0, 95.83, 75.0, 73.44, 95.10, 90.0, 90.0],
    'QA (%)': [85.0, 90.0, 90.5, 70.52, 52.0, 67.0, 100.0, 87.22, 100.0, 100.0, 100.0, 92.5, 95.0, 70.0],
    'ACS Score (%)': [89.0, 90.0, 94.4, 97.3, 70.5, 100.0, 100.0, 84.8, 0.0, 100.0, 90.7, 92.3, 85.33, 83.33],
    'Availability (%)': [96.51, 99.49, 99.79, 99.28, 95.96, 99.96, 98.31, 98.79, 99.74, 95.29, 99.83, 99.78, 83.35, 93.0],
    'RTA (%)': [82.94, 93.3, 88.42, 84.33, 83.06, 65.96, 82.31, 70.72, 80.96, 100.0, 73.1, 70.0, 75.0, 66.0],
    'PS & Compliance (%)': [86.16, 88.4, 93.28, 84.55, 83.27, 90.16, 86.33, 44.95, 98.57, 91.67, 100.0, 82.79, 85.7, 82.67],
    'AHT': [633, 655.7, 637.8, 922.8, 606.3, 890, 772.5, 609.9, 506.6, 486, 450, 440, 384, 381]
}

df_equipo = pd.DataFrame(data_equipo)


# --------------------------- METAS y formatos ---------------------------
metas = {
    'OIR (%)': 92.0,
    'AHT (seg)': 640.0,
    'QA (%)': 85.0,
    'ACS (%)': 70.0,
    'PS & Compliance (%)': 75.0,
    'RTA (%)': 90.0,
    'CCA (%)': 90.0,
    'CARE (%)': 5.0,
    'NICE TOUR (%)': 80.0,
    'ACS Score (%)': 85.0,
    'Lates (%)': 0.0,
    'Abs (%)': 50.0,
    'Availability (%)': 90.0,  # Assumed target, high good
    'Silence Percentage (%)': 40.0  # Assumed target, low good
}

# ----------------------------------------------------------------------
# Función auxiliar para obtener letra de columna Excel desde índice 0-based
def excel_col_letter(col_idx):
    return xl_col_to_name(col_idx)

# Guardar en Excel con xlsxwriter
output_file = r'C:\Users\GAMER\Documents\Reporte_Metricas_Christian.xlsx'
try:
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        workbook = writer.book

        # Formatos generales with larger font
        fmt_header = workbook.add_format({'bold': True, 'bg_color': '#4F81BD', 'font_color': 'white', 'align': 'center', 'font_size': 14})
        fmt_bold = workbook.add_format({'bold': True, 'font_size': 12})
        fmt_pct = workbook.add_format({'num_format': '0.00', 'font_size': 12})
        fmt_int = workbook.add_format({'num_format': '0', 'font_size': 12})

        # ------------------ Formato condicional (semáforo) ------------------
        # Define formats with larger font
        fmt_dark_green = workbook.add_format({'bg_color': '#008000', 'font_size': 12})
        fmt_light_green = workbook.add_format({'bg_color': '#90EE90', 'font_size': 12})
        fmt_yellow = workbook.add_format({'bg_color': '#FFFF00', 'font_size': 12})
        fmt_red = workbook.add_format({'bg_color': '#FF0000', 'font_size': 12})

        def add_traffic_light(ws, col_idx, target, menor_mejor=False, first_row=1, last_row=None):
            if last_row is None:
                last_row = ws.dim_rowmax
            col_letter = excel_col_letter(col_idx)
            rng = f'{col_letter}{first_row+1}:{col_letter}{last_row+1}'
            # For xlsxwriter conditional formats, we add 4 rules to implement the bands described
            if menor_mejor:
                # dark green <= target
                ws.conditional_format(rng, {'type':'cell', 'criteria':'<=', 'value': target, 'format': fmt_dark_green})
                # light green <= target*1.05 (close)
                ws.conditional_format(rng, {'type':'cell', 'criteria':'<=', 'value': target*1.05, 'format': fmt_light_green})
                # yellow <= target*1.15
                ws.conditional_format(rng, {'type':'cell', 'criteria':'<=', 'value': target*1.15, 'format': fmt_yellow})
                # else red (>= target*1.15) - implemented by >= rule
                ws.conditional_format(rng, {'type':'cell', 'criteria':'>', 'value': target*1.15, 'format': fmt_red})
            else:
                # dark green >= target
                ws.conditional_format(rng, {'type':'cell', 'criteria':'>=', 'value': target, 'format': fmt_dark_green})
                # light green >= 0.95*target
                ws.conditional_format(rng, {'type':'cell', 'criteria':'>=', 'value': target*0.95, 'format': fmt_light_green})
                # yellow >= 0.9*target
                ws.conditional_format(rng, {'type':'cell', 'criteria':'>=', 'value': target*0.9, 'format': fmt_yellow})
                # else red < 0.9*target
                ws.conditional_format(rng, {'type':'cell', 'criteria':'<', 'value': target*0.9, 'format': fmt_red})

        # 1) Hoja: Datos Diarios (como tablas separadas por mes)
        sheet_daily = 'Daily_Data'
        ws = workbook.add_worksheet(sheet_daily)
        writer.sheets[sheet_daily] = ws
        grouped = df_daily.groupby('Mes')
        current_row = 0
        styles = ['Table Style Medium 9', 'Table Style Medium 2', 'Table Style Medium 3', 'Table Style Medium 4', 'Table Style Medium 5', 'Table Style Medium 6', 'Table Style Medium 7']
        i = 0
        for mes, df_group in grouped:
            # Write month header
            ws.write(current_row, 0, f'Mes: {mes}', fmt_header)
            current_row += 1
            # Write data
            df_group.to_excel(writer, sheet_name=sheet_daily, index=False, startrow=current_row, header=True)
            rows_group = len(df_group)
            cols = len(df_group.columns)
            last_col = cols - 1
            table_range = f'A{current_row+1}:{excel_col_letter(last_col)}{current_row + rows_group +1}'
            columns = [{'header': c} for c in df_group.columns]
            ws.add_table(table_range, {'columns': columns, 'style': styles[i % len(styles)]})
            # Add averages row
            avg_row = current_row + rows_group + 2
            ws.write(avg_row-1, 0, 'Average', fmt_bold)
            for cidx, col in enumerate(df_group.columns):
                if pd.api.types.is_numeric_dtype(df_group[col]):
                    col_letter = excel_col_letter(cidx)
                    start = current_row + 2
                    end = current_row + rows_group +1
                    formula = f'=AVERAGE({col_letter}{start}:{col_letter}{end})'
                    ws.write_formula(avg_row-1, cidx, formula)
            # Ajustar anchos (larger for visibility)
            for j, col in enumerate(df_group.columns):
                max_len = max(df_group[col].astype(str).map(len).max(), len(col)) + 5
                ws.set_column(j, j, max_len)
            # Apply semáforo to this group
            daily_col_map_group = {c: j for j, c in enumerate(df_group.columns)}
            for metric in ['OIR (%)', 'AHT (seg)', 'PS & Compliance (%)', 'RTA (%)', 'Availability (%)']:
                if metric in metas and metric in daily_col_map_group:
                    menor = True if metric in ['AHT (seg)'] else False
                    add_traffic_light(ws, daily_col_map_group[metric], metas[metric], menor_mejor=menor, first_row=current_row, last_row=current_row + rows_group)
            current_row = avg_row + 2  # space between months
            i += 1

        # 2) Hoja: Monthly Summary
        
        sheet_month = 'Monthly_Summary'
        df_monthly.to_excel(writer, sheet_name=sheet_month, index=False, startrow=0)
        ws_m = writer.sheets[sheet_month]
        r_m, c_m = df_monthly.shape
        last_col_m = c_m - 1
        # Add table
        table_range_m = f'A1:{excel_col_letter(last_col_m)}{r_m+1}'
        columns_m = [{'header': c} for c in df_monthly.columns]
        ws_m.add_table(table_range_m, {'columns': columns_m, 'style':'Table Style Medium 9'})
        # Average row
        avg_row_m = r_m + 2
        ws_m.write(avg_row_m-1, 0, 'Average 6 Months', fmt_bold)
        for cidx, col in enumerate(df_monthly.columns):
            if pd.api.types.is_numeric_dtype(df_monthly[col]):
                col_letter = excel_col_letter(cidx)
                formula = f'=AVERAGE({col_letter}2:{col_letter}{r_m+1})'
                ws_m.write_formula(avg_row_m-1, cidx, formula)
        for i, col in enumerate(df_monthly.columns):
            max_len = max(df_monthly[col].astype(str).map(len).max(), len(col)) + 5
            ws_m.set_column(i, i, max_len)


        # 3) Hoja: Team (Equipo)
        
        sheet_team = 'Team_August'
        df_equipo.to_excel(writer, sheet_name=sheet_team, index=False, startrow=0)
        ws_t = writer.sheets[sheet_team]
        r_t, c_t = df_equipo.shape
        last_col_t = c_t -1
        table_range_t = f'A1:{excel_col_letter(last_col_t)}{r_t+1}'
        columns_t = [{'header': c} for c in df_equipo.columns]
        ws_t.add_table(table_range_t, {'columns': columns_t, 'style':'Table Style Medium 9'})
        # Average row
        avg_row_t = r_t + 2
        ws_t.write(avg_row_t-1, 0, 'Average', fmt_bold)
        for cidx, col in enumerate(df_equipo.columns):
            if pd.api.types.is_numeric_dtype(df_equipo[col]):
                col_letter = excel_col_letter(cidx)
                formula = f'=AVERAGE({col_letter}2:{col_letter}{r_t+1})'
                ws_t.write_formula(avg_row_t-1, cidx, formula)
        for i, col in enumerate(df_equipo.columns):
            max_len = max(df_equipo[col].astype(str).map(len).max(), len(col)) + 5
            ws_t.set_column(i, i, max_len)


        # Apply semáforo en Monthly (columns indices: OIR=1, AHT=2, QA=3, ACS=4, PS=5, RTA=6)
        col_map_monthly = { 'OIR (%)': 1, 'AHT (seg)': 2, 'QA (%)': 3, 'ACS (%)': 4, 'PS & Compliance (%)': 5, 'RTA (%)': 6 }
        for k, idx in col_map_monthly.items():
            if k in metas:
                menor = True if k in ['AHT (seg)'] else False
                add_traffic_light(ws_m, idx, metas[k], menor_mejor=menor, first_row=1, last_row=r_m)


        # Apply semáforo en Team (selección de métricas, adjusted for removed CS)
        team_col_map = {
            'OIR (%)': 1, 'Silence Percentage (%)': 2, 'CCA (%)': 3, 'CARE (%)': 4,
            'NICE TOUR (%)': 5, 'QA (%)': 6, 'ACS Score (%)': 7,
            'Availability (%)': 8, 'RTA (%)': 9, 'PS & Compliance (%)': 10, 'AHT': 11
        }
        for k, idx in team_col_map.items():
            if k in metas:
                menor = True if k in ['AHT', 'Silence Percentage (%)', 'CARE (%)'] else False
                add_traffic_light(ws_t, idx, metas[k], menor_mejor=menor, first_row=1, last_row=r_t)


        # Daily semáforo applied per group above


        # ------------------ Gráficos con XlsxWriter ------------------
        # Monthly trend: OIR (line), QA (line) and AHT (line secondary axis)
        chart_month = workbook.add_chart({'type': 'line'})  
        # series: data is in sheet_month starting at row 1 (headers row 0)
        # OIR column col 1
        chart_month.add_series({'name': 'OIR (%)', 'categories': [sheet_month, 1, 0, r_m, 0], 'values': [sheet_month, 1, 1, r_m, 1]})
        chart_month.add_series({'name': 'QA (%)', 'categories': [sheet_month, 1, 0, r_m, 0], 'values': [sheet_month, 1, 3, r_m, 3]})
        chart_month.add_series({'name': 'AHT (seg)', 'categories': [sheet_month, 1, 0, r_m, 0], 'values': [sheet_month, 1, 2, r_m, 2], 'y2_axis': True})
        chart_month.set_title({'name': 'Trend Monthly: OIR / QA / AHT'})
        chart_month.set_y_axis({'name': 'Percent (%)'})
        chart_month.set_y2_axis({'name': 'AHT (seg)'})
        chart_month.set_size({'width': 720, 'height': 360})
        ws_m.insert_chart('J2', chart_month)

        # Team ranking - OIR horizontal bar
        chart_team = workbook.add_chart({'type':'bar', 'subtype':'stacked'})
        # Categories: Empleado rows 1..r_t
        chart_team.add_series({'name':'OIR (%)', 'categories': [sheet_team, 1, 0, r_t, 0], 'values': [sheet_team, 1, 1, r_t, 1]})
        chart_team.set_title({'name': 'Team Ranking by OIR (%)'})
        chart_team.set_x_axis({'name': 'OIR (%)'})
        chart_team.set_size({'width': 720, 'height': 400})
        ws_t.insert_chart('P2', chart_team)

        # Daily chart removed as data is split

    print(f'Archivo Excel generado: {output_file}')
except PermissionError as e:
    print(f"Error: No se puede escribir en el archivo '{output_file}' debido a un problema de permisos.")
    print("Por favor, asegúrate de que:")
    print("1. El archivo no esté abierto en otra aplicación (como Excel).")
    print("2. Tienes permisos de escritura en la carpeta 'C:\\Users\\GAMER\\Documents'.")
    print("3. Intenta ejecutar el comando como administrador o cambiar la ruta de salida.")
    print(f"Detalles del error: {e}")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")