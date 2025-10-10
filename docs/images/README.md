# Image Placeholders for Documentation

This directory contains placeholder images for the documentation. In a real implementation, these would be actual screenshots of the Excel reports.

## Required Images

### 1. `daily_metrics_preview.png`
**Description**: Screenshot of the Daily Data sheet showing:
- Monthly grouped data tables
- Color-coded conditional formatting (green, yellow, red cells)
- Average rows at the bottom of each month section
- Professional table styling with alternating colors

**Recommended size**: 800x600 pixels

---

### 2. `team_performance_preview.png`
**Description**: Screenshot of the Team Analysis sheet showing:
- Employee names in the first column
- Multiple metric columns (OIR, QA, CCA, CARE, etc.)
- Conditional formatting applied to metric values
- Horizontal bar chart on the right side showing team ranking

**Recommended size**: 800x600 pixels

---

### 3. `daily_data_example.png`
**Description**: Detailed screenshot of the Daily Data sheet featuring:
- One complete month of data (e.g., April 2025)
- All columns visible: Call Date, HANDLED, OIR (%), AHT (sec), PS & Compliance (%), RTA (%)
- Traffic light conditional formatting clearly visible
- Line chart showing OIR vs AHT trends

**Recommended size**: 1200x800 pixels

---

### 4. `team_analysis_example.png`
**Description**: Detailed screenshot of the Team Analysis sheet showing:
- Complete employee list with all metrics
- Team averages row at the bottom
- Color-coded cells based on performance targets
- OIR ranking chart positioned to the right of the data table

**Recommended size**: 1200x800 pixels

---

### 5. `conditional_formatting_demo.png`
**Description**: Close-up showing the traffic light system:
- Examples of cells with dark green (≥100% of target)
- Examples of cells with light green (≥95% of target)
- Examples of cells with yellow (≥90% of target)
- Examples of cells with red (<90% of target)
- Labels or annotations explaining each color

**Recommended size**: 600x400 pixels

---

### 6. `chart_example.png`
**Description**: Close-up of a trend chart showing:
- Line chart with two series (OIR and AHT)
- X-axis with dates
- Y-axis with percentage/time values
- Legend identifying the lines
- Professional chart styling

**Recommended size**: 800x500 pixels

---

## How to Generate These Images

1. Run the script: `python to_excel.PY`
2. Open the generated Excel file: `Reporte_Metricas_Christian_modified.xlsx`
3. Take screenshots of:
   - Full sheet views
   - Specific sections with formatting
   - Charts and visualizations
4. Save screenshots in this directory with the names listed above
5. Optimize images for web (PNG format, reasonable file size)

---

## Note

To create actual images, you can use:
- Windows Snipping Tool / Snip & Sketch
- macOS Screenshot (Cmd + Shift + 4)
- Linux Screenshot tools (gnome-screenshot, Spectacle, etc.)
- Or any screenshot utility of your choice

Make sure to capture the images at a good resolution that shows the details clearly while keeping file sizes reasonable for the repository.
