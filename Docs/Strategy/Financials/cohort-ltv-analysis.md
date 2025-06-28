# Cohort & LTV Analysis Template
*[TEMPLATE EXAMPLE - This shows how to structure cohort analysis and LTV calculations. Replace with your actual customer data.]*

---

**⚠️ TEMPLATE NOTICE:** This file contains an example cohort and LTV analysis for "[COMPANY_NAME]" demonstrating how to track customer cohorts, calculate lifetime value, and derive strategic insights from customer behavior data. Replace all content below with your actual customer cohort data and analysis.

---

# Cohort & LTV Analysis - [COMPANY_NAME] 
*[EXAMPLE COMPANY - Replace with your company's cohort analysis]*

## 📊 Raw Cohort Data ([START_YEAR]-[END_YEAR]) [CANONICAL - Document Overview]

### [START_YEAR]-[END_YEAR] [CUSTOMER_SEGMENT] Cohorts ([PRICING_TYPE] Highlighted)
| Start Date | Customer | Vertical | [SEGMENT] | Status | Month 1 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12+ |
|------------|----------|----------|-----|--------|---------|---------|---------|---------|---------|---------|---------|---------|---------|----------|----------|-----------|
| [YEAR]-[MO] | Client [X] | [INDUSTRY_A] | [SEGMENT] | + | $[X] | $[Y] | $[Y] | $[Z] | $[W] | $[W] | $[W] | $[W] | $[V] | $[W] | $[W] | $[W] |
| [YEAR]-[MO] | Client [X] | [INDUSTRY_B] | [SEGMENT] | + | $[X] | $[Y] | $[Y] | $[Y] | $[Z] | $[Z] | $[Z] | $[W] | $[W] | $[V] | $[V] | $[U] |
| [YEAR]-[MO] | Client [X] | [INDUSTRY_A] | [SEGMENT] | + | $[X] | $[X] | $[X] | $[X] | $[X] | $[X] | $[X] | $[X] | $[X] | $[X] | $[X] | $[X] |
| [YEAR]-[MO] | Client [X] | [INDUSTRY_C] | [SEGMENT] | - | $[X] | $[Y] | $[Z] | $[W] | $[W] | $[W] | $[W] | $[V] | $[V] | $[V] | $[V] | CHURNED |
| [YEAR]-[MO] | Client [X] | [INDUSTRY_D] | [SEGMENT] | - | $[X] | $[Y] | $[Y] | $[Y] | $[Z] | $[Z] | $[Z] | $[Z] | CHURNED | - | - | - |
| [YEAR]-[MO] | Client [X] | [INDUSTRY_B] | [SEGMENT] | ± | $[X] | $[Y] | $[Y] | $[Y] | $[Y] | $[Z] | $[Z] | $[Z] | $[Z] | DOWNGRADE | - | - |

**Status Legend:** [CANONICAL - Data Legend]
- **+** Active at full or expanding revenue
- **-** Churned completely
- **±** Downgraded significantly but still paying

### Churn Analysis Summary [CANONICAL - Calculated from Raw Cohort Data]
- **Total Cohorts:** [X]
- **Fully Active (+):** [Y] ([Z]%)
- **Churned (-):** [A] ([B]%)
- **Downgraded (±):** [C] ([D]%)
- **[SEGMENT_1] Churn Rate:** [X] out of [Y] [SEGMENT_1] clients ([Z]%)
- **[SEGMENT_2] Churn Rate:** [A] out of [B] [SEGMENT_2] clients ([C]%)

### Key Patterns from Raw Data [ANALYSIS - Derived from Raw Cohort Data]
1. **Discount Period:** Most [TARGET_SEGMENT] clients start with [X]-[Y]% discounts for [Z]-[W] months
2. **Full Price Range:** $[X]-$[Y]/month for established [TARGET_SEGMENT] clients
3. **Ramp Pattern:** Typical progression from [X]% → [Y]% → [Z]% of full price
4. **[NON_TARGET_SEGMENT] Performance:** Lower starting prices, minimal expansion, higher churn

### Churn Pattern Analysis [ANALYSIS - Derived from Raw Cohort Data]

**Churned Clients (-)**
1. **Client [X] ([INDUSTRY], [SEGMENT]):** Survived [X]+ months at ~$[Y]-$[Z]
2. **Client [X] ([INDUSTRY], [SEGMENT]):** Churned after [Y] months at ~$[Z]-$[W]
3. **Client [X] ([INDUSTRY], [SEGMENT]):** Churned after [Z] months at flat $[W]

**Downgraded Clients (±)**
1. **Client [X] ([INDUSTRY]):** Dropped from $[Y] to $[Z] ([X]% reduction) after [W] months
2. **Client [X] ([INDUSTRY]):** Dropped from $[Y] to $[Z] ([X]% reduction) after [W] months

**Success Patterns (+)**
- [INDUSTRY_A] clients show strongest retention ([X] of [Y] active)
- [INDUSTRY_B] clients ramp quickly and stay ([X] of [Y] active)
- [INDUSTRY_C] maintain high stable revenue ([X] of [Y] active)
- Higher starting prices correlate with better retention

**Risk Indicators**
- [INDUSTRY_D] vertical: [X] churned, [Y] active ([Z]% churn)
- [INDUSTRY_E] vertical: [X] churned, [Y] downgraded ([Z]% problematic)
- Clients starting below $[X] MRR have higher churn risk
- [NON_TARGET_SEGMENT] clients: [X]% churn rate vs [Y]% for [TARGET_SEGMENT]

## 💰 Updated LTV Calculation (No NPV Discounting) [CANONICAL - LTV Methodology & Result]

### Current Reality - Average [TARGET_SEGMENT] Customer [CANONICAL - LTV Model Inputs - Sourced from Cohort Data & P&L Analysis]
Based on actual cohort data patterns:

**Pricing Structure:**
- **Months 1-3:** Average $[X]/month (discounted period) [CANONICAL - Observed from Cohort Data]
- **Months 4+:** Average $[Y]/month (full price) [CANONICAL - Observed from Cohort Data] [REF: financial-summary.md#Full-Price-ARPU]
- **Gross Margin:** [Z]% [CANONICAL - Assumption for LTV Calc] [REF: financial-summary.md#Key-Metrics for COGS ratio]

**5-Year LTV Calculation:** [CANONICAL - LTV Calculation Steps]
```
Year 1: 
- Months 1-3: $[X] × 3 = $[Y]
- Months 4-9: $[Z] × 6 = $[W]
- Months 10-12: $[Z] × 3 × [RETENTION] = $[V] ([CHURN]% churn)
- Year 1 Total: $[TOTAL_1]

Years 2-5:
- Year 2: [RETENTION_2]% × $[Z] × 12 = $[TOTAL_2]
- Year 3: [RETENTION_3]% × $[Z] × 12 = $[TOTAL_3]
- Year 4: [RETENTION_4]% × $[Z] × 12 = $[TOTAL_4]
- Year 5: [RETENTION_5]% × $[Z] × 12 = $[TOTAL_5]
- Years 2-5 Total: $[TOTAL_2_5]

Total 5-Year Revenue: $[TOTAL_REV]
After [MARGIN]% Gross Margin: $[FINAL_LTV] [CANONICAL - Calculated 5-Year LTV]
```

### Target State - No Discounts [PROJECTED LTV Scenario]
If [IMPROVEMENT_INITIATIVE] eliminates [DISCOUNT_PERIOD]:

**5-Year LTV at Full Price:**
```
Year 1: $[X] × 9 + $[X] × 3 × [RETENTION] = $[Y]
Years 2-5: $[X] × ([RETENTION_FORMULA]) = $[Z]
Total Revenue: $[TOTAL]
After [MARGIN]% Gross Margin: $[FINAL_LTV] [PROJECTED - Calculated LTV without discounts]
```

### Is 5-Year LTV Reasonable for [COMPANY_NAME]? [ANALYSIS - Justification]
**Yes, for several reasons:**
1. **[BUSINESS_MODEL] standard** - [X]-[Y] year LTV is typical for [INDUSTRY_TYPE]
2. **Retention math** - [X]% of customers still active in year 5 (reasonable)
3. **Switching costs** - [STICKINESS_FACTOR] create stickiness
4. **Conservative approach** - Assumes no price increases beyond year 1

### Discount Impact Analysis [ANALYSIS - Calculated Impact]
- **Revenue lost to discounts:** $[X] in Year 1
- **Total LTV impact:** $[Y] ([Z]% of total LTV)
- **More realistic than previous [PREV_ESTIMATE]% estimate**

## 📊 Cohort Quality Analysis [CANONICAL - Analysis from Raw Data]

### Best Performing [TARGET_SEGMENT] Cohorts ([PRICING_TYPE] Examples) [CANONICAL - Examples from Raw Data]
1. **Client [X] ([INDUSTRY]):** Ramped from $[Y] to $[Z] - [MULTIPLE]x increase
2. **Client [X] ([INDUSTRY]):** Started at $[Y], quickly to $[Z]
3. **Client [X] ([INDUSTRY]):** Complex ramp but stabilized at $[Y]
4. **Client [X] ([INDUSTRY]):** Started directly at $[Y] (no discount)

### Discount Patterns by Vertical [CANONICAL - Analysis from Raw Data]
| Vertical | Avg Discount Period | Avg Discount % | Full Price Range |
|----------|-------------------|----------------|------------------|
| [INDUSTRY_A] | [X]-[Y] months | [Z]-[W]% | $[A]-$[B] |
| [INDUSTRY_B] | [X]-[Y] months | [Z]-[W]% | $[A]-$[B] |
| [INDUSTRY_C] | [X]-[Y] months | [Z]-[W]% | $[A]-$[B] |
| [INDUSTRY_D] | [X]-[Y] months | [Z]-[W]% | $[A]-$[B] |
| [INDUSTRY_E] | [X]-[Y] months | [Z]-[W]% | $[A]-$[B] |

## 🎯 Key Insights from Cohort Analysis [ANALYSIS - Conclusions]

### 1. Discount Reality Check
- Previous estimate of [X]% LTV loss was overstated
- Actual impact closer to [Y]% of total LTV
- Main issue is [ROOT_CAUSE], not discount depth

### 2. Pricing Opportunity
- Top [TARGET_SEGMENT] clients paying $[X]-$[Y]
- Current average of $[Z] has room to grow
- [X]-[Y]% pricing headroom for quality [TARGET_SEGMENT] customers

### 3. Vertical Performance
- [INDUSTRY_A] commands highest prices ($[X]-$[Y])
- [INDUSTRY_B] shows fastest ramp to full price
- [INDUSTRY_C] has shortest discount periods

### 4. [SUCCESS_FACTOR] Success Factors
- Clients starting at higher prices have smoother ramps
- [FACTOR_1] correlates with shorter discount periods
- [FACTOR_2] reach full price faster

## 🔍 Action Items from Analysis [PLAN - Derived from Cohort Analysis]

### Immediate (Q[X] [YEAR])
1. **Standardize pricing** at $[X]+ for new [TARGET_SEGMENT] customers
2. **Shorten discount period** to [X] month maximum
3. **Automate [PROCESS]** for [INDUSTRY_A] and [INDUSTRY_B] (fastest ramps)
4. **Stop all [NON_TARGET] sales** immediately

### Medium-term (H[X] [YEAR])
1. **Vertical pricing tiers:** [INDUSTRY_A] $[X], [INDUSTRY_B] $[Y], Others $[Z]
2. **Success-based pricing:** Tie discounts to [MILESTONE] milestones
3. **Expansion playbooks:** Systematic approach to [MULTIPLE]x initial contract
4. **Cohort health scores:** Predict based on initial engagement

---

## Template Customization Guide

### Replace All Customer Data:
- **Customer Names**: Replace with your actual customer identifiers or anonymized versions
- **Financial Numbers**: Update all dollar amounts with your actual revenue data
- **Industry Verticals**: Replace with your target market segments
- **Time Periods**: Update dates to match your business timeline
- **Customer Segments**: Replace [SEGMENT] classifications with your customer types

### Maintain Analysis Structure:
- **Keep cohort table format** for month-by-month revenue tracking
- **Preserve status legend** (+, -, ±) for customer health tracking
- **Use same analytical sections** (churn patterns, success factors, risk indicators)
- **Follow LTV calculation methodology** adapted to your business model

### Adapt to Your Business Model:
- **Pricing Structure**: Modify discount periods and pricing tiers to match your model
- **Retention Assumptions**: Update retention rates based on your customer behavior
- **Gross Margin**: Use your actual margin calculations
- **Success Metrics**: Define what constitutes customer success in your business

### Key Metrics to Track:
- **Customer Acquisition Cost (CAC)** from marketing and sales expenses
- **Customer Lifetime Value (LTV)** using cohort-based calculations
- **LTV:CAC Ratio** for unit economics validation
- **Churn patterns** by customer segment and industry vertical
- **Revenue expansion** within existing customer cohorts

---

*Template Purpose: Customer cohort analysis and lifetime value calculation framework*
*Best For: Subscription businesses with complex pricing and customer segmentation*

[LAST UPDATED: [DATE] - TEMPLATE EXAMPLE] 