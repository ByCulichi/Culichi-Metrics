# Visual Guide - ASCII Representation

This file provides a text-based visual representation of what the Excel reports look like.

## Daily Data Sheet Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          DAILY DATA - APRIL 2025                            │
├───────────┬──────────┬───────────┬───────────┬──────────────────┬──────────┤
│ Call Date │ HANDLED  │  OIR (%)  │ AHT (sec) │ PS & Compliance  │  RTA (%) │
├───────────┼──────────┼───────────┼───────────┼──────────────────┼──────────┤
│ 2025-04-01│    45    │   92.5 🟢 │   620 🟢  │      95.0 🟢     │  88.0 🟡 │
│ 2025-04-02│    52    │   88.3 🟡 │   645 🟡  │      92.5 🟢     │  90.5 🟢 │
│ 2025-04-03│    48    │   95.2 🟢 │   598 🟢  │      96.8 🟢     │  92.3 🟢 │
│ 2025-04-04│    51    │   85.6 🟡 │   670 🔴  │      89.2 🟡     │  87.8 🟡 │
│    ...    │   ...    │    ...    │    ...    │       ...        │   ...    │
├───────────┼──────────┼───────────┼───────────┼──────────────────┼──────────┤
│  AVERAGE  │   49.0   │   90.4 🟢 │   633 🟡  │      93.4 🟢     │  89.7 🟡 │
└───────────┴──────────┴───────────┴───────────┴──────────────────┴──────────┘

                           [TREND CHART]
                      OIR vs AHT Over Time
  100% ┤                    ╭─╮
       │                 ╭──╯ ╰──╮
   90% ┤           ╭─────╯       ╰───╮
       │        ╭──╯                  ╰─╮
   80% ┼────────╯                       ╰──
       └────────────────────────────────────
         Apr 1  Apr 5  Apr 10  Apr 15  Apr 20
             🟢 OIR (%)    🔵 AHT (sec)
```

## Team Analysis Sheet Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        TEAM PERFORMANCE - AUGUST                            │
├──────────────────┬──────────┬──────────┬──────────┬──────────┬────────────┤
│    Employee      │ OIR (%)  │  QA (%)  │ CCA (%)  │ CARE (%) │   RTA (%)  │
├──────────────────┼──────────┼──────────┼──────────┼──────────┼────────────┤
│ John Smith       │  95.2 🟢 │  88.5 🟢 │  92.3 🟢 │  3.2 🟢  │   91.0 🟢  │
│ Maria Garcia     │  92.8 🟢 │  91.2 🟢 │  89.5 🟡 │  4.1 🟢  │   89.5 🟡  │
│ David Johnson    │  88.6 🟡 │  85.3 🟢 │  90.8 🟢 │  5.5 🟡  │   87.2 🟡  │
│ Sarah Williams   │  93.5 🟢 │  89.8 🟢 │  94.1 🟢 │  2.8 🟢  │   92.3 🟢  │
│ Robert Brown     │  87.2 🟡 │  82.5 🟡 │  86.7 🟡 │  6.2 🔴  │   85.8 🟢  │
│       ...        │   ...    │   ...    │   ...    │   ...    │    ...     │
├──────────────────┼──────────┼──────────┼──────────┼──────────┼────────────┤
│  TEAM AVERAGE    │  91.5 🟢 │  87.5 🟢 │  90.7 🟢 │  4.4 🟢  │   89.2 🟡  │
└──────────────────┴──────────┴──────────┴──────────┴──────────┴────────────┘

                      [RANKING CHART - OIR %]
    Sarah Williams    ████████████████████████████ 93.5%
    John Smith        ████████████████████████████ 95.2%
    Maria Garcia      ██████████████████████████   92.8%
    David Johnson     █████████████████████        88.6%
    Robert Brown      ████████████████████         87.2%
                      0%        50%        100%
```

## Color Legend

The traffic light system uses these colors:

```
🟢 DARK GREEN  - Excellent (≥100% of target)
   Example: OIR at 95% when target is 90%

🟢 LIGHT GREEN - Good (≥95% of target)
   Example: OIR at 88.5% when target is 90%

🟡 YELLOW      - Acceptable (≥90% of target)
   Example: OIR at 82% when target is 90%

🔴 RED         - Critical (<90% of target)
   Example: OIR at 75% when target is 90%
```

## Metrics Explanation

### Daily Metrics:
- **HANDLED**: Total number of calls handled that day
- **OIR (%)**: Offer and Information Rate - percentage of calls where offers/info were provided
- **AHT (sec)**: Average Handle Time - average duration of calls in seconds
- **PS & Compliance (%)**: Professional Standards & Compliance score
- **RTA (%)**: Real Time Adherence - how well agents stick to their schedules

### Team Metrics:
- **OIR (%)**: Individual offer and information rate
- **QA (%)**: Quality Assurance score from call reviews
- **CCA (%)**: Customer Care Advocacy score
- **CARE (%)**: Customer care issue rate (lower is better)
- **RTA (%)**: Individual schedule adherence

## Chart Types

### 1. Line Chart (Daily Data)
Shows trends over time for key metrics like OIR and AHT across all days in a month.

### 2. Horizontal Bar Chart (Team Analysis)
Displays team member rankings based on OIR percentage, making it easy to see top performers.

---

## How the Conditional Formatting Works

The script automatically applies colors based on performance relative to targets:

```python
For "Higher is Better" metrics (OIR, QA, RTA, etc.):
    if value >= target:                    # 100% or more
        color = DARK_GREEN
    elif value >= target * 0.95:           # 95% to 99.9%
        color = LIGHT_GREEN
    elif value >= target * 0.90:           # 90% to 94.9%
        color = YELLOW
    else:                                  # Less than 90%
        color = RED

For "Lower is Better" metrics (AHT, CARE):
    The logic is inverted - lower values get better colors
```

This makes it immediately obvious which areas need attention and which are performing well.

---

## Sample Data Flow

```
Input (Python dictionaries):
{
    'Call Date': '2025-04-01',
    'HANDLED': 45,
    'OIR (%)': 92.5,
    'AHT (seg)': 620,
    ...
}
        ↓
Processing (pandas + xlsxwriter):
- Convert to DataFrame
- Group by month
- Calculate averages
- Apply formatting rules
        ↓
Output (Excel with formatting):
┌───────────┬──────────┬───────────┐
│ 2025-04-01│    45    │   92.5 🟢 │
└───────────┴──────────┴───────────┘
```

---

*This ASCII representation helps visualize the report structure. For actual images, see the main README instructions on generating screenshots.*
