# 🔧 Utility Scripts

Useful scripts for automating checks and calculations.

## 📊 check_range.py

Checks if numbers fall within specified ranges. Useful for health test analysis, financial metrics, and other numerical data.

### Usage:

```bash
python3 scripts/check_range.py [value] [min] [max] [value] [min] [max] ...
```

### Examples:

**Blood tests:**

```bash
# Cholesterol (normal 120-200), Sugar (normal 70-100), Blood pressure (normal 80-120)
python3 scripts/check_range.py 185 120 200 92 70 100 85 80 120
```

**Budget categories:**

```bash
# Food expenses (budget 500-700), Entertainment (budget 200-300)
python3 scripts/check_range.py 650 500 700 250 200 300
```

**Result:**

```
🔍 Range Check:
==================================================
   185.0 | [ 120.0 -  200.0] | ✅ In range
    92.0 | [  70.0 -  100.0] | ✅ In range
    85.0 | [  80.0 -  120.0] | ✅ In range
==================================================
```

### Why is this needed?

LLMs often make mistakes when comparing numbers. This script provides precise mathematical results that can be used in analysis.

## Ideas for other scripts:

* `calculate_bmi.py` - body mass index calculation
* `currency_convert.py` - currency conversion
* `compound_interest.py` - compound interest calculation
* `health_metrics.py` - healthy range calculations by age
