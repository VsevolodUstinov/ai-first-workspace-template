# Financial Data Sources Reference Template
*[TEMPLATE EXAMPLE - This shows how to structure financial data sources and Google Sheets integration. Replace with your actual financial data sources.]*

---

**⚠️ TEMPLATE NOTICE:** This file contains an example financial data sources reference for "[COMPANY_NAME]" demonstrating how to organize and document financial data sources, including Google Sheets integration and data tracking methodology. Replace all content below with your actual financial data sources and links.

---

# Financial Data Sources Reference - [COMPANY_NAME]
*[EXAMPLE COMPANY - Replace with your company's financial data sources]*

## Primary Financial Model (Quarterly)

### Google Sheets URL
**URL:** https://docs.google.com/spreadsheets/d/[EXAMPLE_SPREADSHEET_ID]/

### Available Data in the Model

#### Key Metrics Tab
- **Quarterly ARR** (Annual Recurring Revenue)
- **MRR** (Monthly Recurring Revenue) 
- **Customer Count**
- **ARR per Customer**
- **Committed ARR** (signed contracts not yet recognized)
- **Quarterly Revenue** (recognized)
- **Quarterly Burn** (net spend)
- **YoY Growth rates**

#### Historical Data Available
- **Start Date:** Q[X] [YEAR]
- **Latest Actual Data:** Q[X] [YEAR] (as of last update)
- **Projections:** Through Q[X] [YEAR]

## Monthly Financial Report (P&L Detail)

### Google Sheets URL
**URL:** https://docs.google.com/spreadsheets/d/[EXAMPLE_SPREADSHEET_ID]/edit?gid=[SHEET_ID]#gid=[SHEET_ID]

### Sheet Name: "[P&L_SHEET_NAME]"

### Available Monthly Data ([START_DATE] - [END_DATE])
- **MRR** (Monthly Recurring Revenue)
- **ARR** (calculated from MRR)
- **Committed ARR**
- **Active Clients count**
- **New clients per month**
- **Detailed P&L breakdown:**
  - COGS with expenses breakdown
  - Sales & Marketing expenses (salaries, other S&M)
  - R&D expenses (salaries)
  - G&A expenses (salaries, other G&A)
- **Monthly Burn** ([CALCULATION_METHOD])

### Key Insights from Monthly Data
- More granular view of customer acquisition (monthly vs quarterly)
- Detailed expense categories for better cost analysis
- Month-over-month growth rates
- Actual monthly burn progression

## Cohort Analysis & Retention Data

### Google Sheets URL
**URL:** https://docs.google.com/spreadsheets/d/[EXAMPLE_COHORT_SPREADSHEET_ID]/edit?gid=0#gid=0

### Sheets Available:
- **"[COHORT_SHEET_NAME]"** - Cohort retention by month
- **"[LTV_SHEET_NAME]"** - LTV calculations

### Available Cohort Data ([START_YEAR]-[END_YEAR])
- **Monthly cohorts** from [START_MONTH] [START_YEAR] to [END_MONTH] [END_YEAR]
- **Customer type** ([CUSTOMER_CLASSIFICATION_1] vs [CUSTOMER_CLASSIFICATION_2] designation)
- **Industry vertical** for each cohort
- **Starting MRR** and monthly progression
- **Churn timing** and expansion patterns
- **Active/churned status**

### Key Insights from Cohort Data
- Clear distinction between [CUSTOMER_TYPE_1] and [CUSTOMER_TYPE_2] performance
- [CUSTOMER_TYPE_1] customers show [X]% NRR vs [Y]% for [CUSTOMER_TYPE_2]
- [YEAR]+ cohorts focused on [TARGET_SEGMENT] only
- [INDUSTRY_1], [INDUSTRY_2], and [INDUSTRY_3] verticals perform best

### How to Update Financial Numbers

1. **Access Google Sheets** using the URLs above
2. **Use [PRIMARY_MODEL]** for high-level metrics and projections
3. **Use [MONTHLY_REPORT]** for detailed P&L and recent month-by-month trends
4. **Update these key files:**
   - `/Financials/financial-summary.md` - Full financial details
   - `/executive-summary.md` - High-level metrics section

5. **Key Metrics to Update:**
   - Current MRR and ARR
   - Customer count and ARR/Customer
   - Burn rate (quarterly and monthly)
   - Revenue (quarterly)
   - YoY growth percentages
   - Committed ARR pipeline
   - CLV:CAC calculations (derive from burn and new customer additions)
   - Detailed expense breakdown (from monthly P&L)

### Important Calculations

#### CAC (Customer Acquisition Cost)
- Formula: Quarterly Burn ÷ Net New Customers Added
- Example: Q[X]'[YY] = $[X] burn ÷ [Y] new customers = $[Z] CAC
- **Note:** Monthly data allows for more precise CAC calculations

#### CLV (Customer Lifetime Value)
- Formula: ARPU × Expected Lifetime (months)
- Assumption: [X]-month average lifetime
- Example: $[X] annual ÷ 12 × [Y] months = $[Z]

#### CLV:CAC Ratio
- Formula: CLV ÷ CAC
- Target: Should be > [X]:1 for healthy unit economics
- Q[X]'[YY] Status: [X]:[Y] ([STATUS])

### Data Accuracy Tags to Use
- **[CONFIRMED]** - Directly from Google Sheets
- **[CALCULATED]** - Derived from confirmed data
- **[ESTIMATED]** - Reasonable estimates based on patterns
- **[PROJECTED]** - Future targets from model
- **[PLACEHOLDER]** - Data not available
- **[ASSUMPTION]** - Needs validation

### Notes on Data Quality
- Committed ARR typically runs [X]-[Y]% ahead of recognized ARR
- Customer additions can vary significantly by quarter
- Burn rate has been [TREND] in absolute terms
- Efficiency metrics (burn as multiple of revenue) have been [TREND]
- Monthly P&L provides more accurate expense allocation

### Other Potential Data Sources
- **Pitch Decks** - May contain updated metrics
- **Board Reports** - Quarterly updates
- **CRM Export** - For customer-level details
- **Financial Statements** - For audited numbers

---

## Template Customization Guide

### Replace All Financial Data Sources:
- **Google Sheets URLs**: Update with your actual spreadsheet links
- **Sheet Names**: Replace with your actual tab names
- **Date Ranges**: Update with your company's data timeline
- **Metrics Categories**: Adapt to your specific financial tracking
- **Calculation Methods**: Update formulas to match your business model

### Maintain Data Architecture:
- **Keep separation** between quarterly models and monthly details
- **Preserve cohort analysis** structure for customer lifetime tracking
- **Use consistent tags** ([CONFIRMED], [CALCULATED], etc.) for data quality
- **Document calculation methods** for key metrics like CAC and CLV

### Integration Best Practices:
- **Link to summary files** that pull from these data sources
- **Regular update schedule** for refreshing cached data
- **Version control** for historical data preservation
- **Access management** for sensitive financial information

### Financial Planning Framework:
- **Historical data** for trend analysis and benchmarking
- **Real-time metrics** for operational decision making
- **Projection models** for strategic planning and fundraising
- **Cohort tracking** for understanding customer behavior and retention

---

*Template Purpose: Financial data source organization and Google Sheets integration framework*
*Best For: Companies with complex financial models requiring multiple data sources*

[LAST UPDATED: [DATE] - TEMPLATE EXAMPLE] 