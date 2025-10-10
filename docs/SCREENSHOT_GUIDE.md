# Screenshot Guide for Culichi-Metrics Documentation

This guide provides step-by-step instructions for creating screenshots to complete the documentation.

## Prerequisites

1. **Python environment set up** with all dependencies installed
2. **Excel or LibreOffice Calc** to open `.xlsx` files
3. **Screenshot tool** available on your system

## Step-by-Step Process

### Step 1: Generate the Report

```bash
cd /path/to/Culichi-Metrics
python to_excel.PY
```

This will create: `Reporte_Metricas_Christian_modified.xlsx`

### Step 2: Open the Excel File

Open the generated Excel file in your preferred spreadsheet application:
- **Windows**: Microsoft Excel
- **macOS**: Microsoft Excel or Numbers
- **Linux**: LibreOffice Calc

### Step 3: Take the Required Screenshots

#### Screenshot 1: `daily_metrics_preview.png`
**What to capture:**
- Open the "Daily_Data" sheet
- Zoom to fit about 1-2 months of data on screen
- Capture the entire visible area including:
  - Column headers
  - At least one full month of data
  - The averages row
  - Part of a trend chart if visible

**Recommended settings:**
- Resolution: 800x600 pixels or similar
- Format: PNG
- Make sure conditional formatting colors are visible

#### Screenshot 2: `team_performance_preview.png`
**What to capture:**
- Switch to the "Team_August" (or similar team sheet)
- Zoom to fit the employee table and ranking chart
- Capture:
  - Employee names column
  - Several metric columns with color formatting
  - The horizontal bar chart on the right
  - Team averages row at the bottom

**Recommended settings:**
- Resolution: 800x600 pixels
- Format: PNG

#### Screenshot 3: `daily_data_example.png`
**What to capture:**
- Focus on the "Daily_Data" sheet
- Zoom in to show detail of ONE complete month
- Make sure to capture:
  - All column headers clearly visible
  - All rows for one month
  - Color coding is clearly visible
  - The averages row
  - The trend chart below or beside the data

**Recommended settings:**
- Resolution: 1200x800 pixels (larger for detail)
- Format: PNG

#### Screenshot 4: `team_analysis_example.png`
**What to capture:**
- Full view of the "Team_August" sheet
- Show all employees and all metrics
- Include the ranking chart
- Show the team averages row

**Recommended settings:**
- Resolution: 1200x800 pixels
- Format: PNG

#### Screenshot 5: `conditional_formatting_demo.png`
**What to capture:**
- Close-up of a few cells showing different colors
- You can capture this from either sheet
- Should clearly show:
  - Dark green cells (excellent performance)
  - Light green cells (good performance)
  - Yellow cells (acceptable performance)
  - Red cells (critical performance)
- Optionally, add text annotations explaining each color

**Recommended settings:**
- Resolution: 600x400 pixels
- Format: PNG
- Consider using an image editor to add labels/arrows

#### Screenshot 6: `chart_example.png`
**What to capture:**
- Close-up of one of the trend charts
- Show the full chart including:
  - Chart title
  - Legend
  - X-axis (dates)
  - Y-axis (values)
  - The actual data lines/bars

**Recommended settings:**
- Resolution: 800x500 pixels
- Format: PNG

## Screenshot Tools by Operating System

### Windows
1. **Snipping Tool** (Windows 10)
   - Press `Windows + Shift + S`
   - Select area to capture
   - Save as PNG

2. **Snip & Sketch** (Windows 11)
   - Press `Windows + Shift + S`
   - Select rectangular snip
   - Save to `docs/images/`

### macOS
1. **Screenshot Utility**
   - Press `Cmd + Shift + 4`
   - Drag to select area
   - File saved to Desktop (move to `docs/images/`)

2. **Screenshot App**
   - Press `Cmd + Shift + 5`
   - Choose selection type
   - Save to chosen location

### Linux
1. **GNOME Screenshot**
   ```bash
   gnome-screenshot -a
   ```

2. **Spectacle** (KDE)
   - Launch Spectacle
   - Select "Rectangular Region"
   - Save to `docs/images/`

3. **Flameshot**
   ```bash
   flameshot gui
   ```

## After Taking Screenshots

1. **Verify image quality:**
   - Text is readable
   - Colors are accurate
   - No personal/sensitive information visible

2. **Optimize file size:**
   ```bash
   # Using ImageMagick (optional)
   convert screenshot.png -quality 85 -resize 1200x optimized.png
   ```

3. **Move to correct location:**
   ```bash
   mv screenshot.png docs/images/daily_metrics_preview.png
   ```

4. **Update git:**
   ```bash
   git add docs/images/*.png
   git commit -m "Add documentation screenshots"
   git push
   ```

## Tips for Better Screenshots

1. **Clean workspace**: Close unnecessary windows/tabs before capturing
2. **Proper zoom level**: Make text readable but show enough content
3. **Natural colors**: Ensure your display isn't in night mode
4. **No sensitive data**: Check that no real employee data is visible if using modified examples
5. **Consistent style**: Use the same zoom level for similar screenshots

## Troubleshooting

**Problem**: Screenshots are too large (>500KB)
- **Solution**: Reduce resolution or use PNG optimization tools

**Problem**: Colors don't show well
- **Solution**: Check Excel zoom level and screen color settings

**Problem**: Text is blurry
- **Solution**: Increase screenshot resolution or take screenshot at 100% zoom

## Alternative: Using Sample Data

If you prefer not to use the default data, you can:

1. Modify the data in `to_excel.PY` to use placeholder names
2. Regenerate the report
3. Take screenshots of the sanitized data

## Questions?

If you have questions about the screenshots:
- Open an issue on GitHub
- Check the [VISUAL_GUIDE.md](images/VISUAL_GUIDE.md) for ASCII representations
- Review examples from similar projects

---

**Once all screenshots are added, remove this file or mark it as complete.**
