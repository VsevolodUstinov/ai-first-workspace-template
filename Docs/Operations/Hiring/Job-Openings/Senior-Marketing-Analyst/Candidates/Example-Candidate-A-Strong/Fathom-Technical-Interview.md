# Technical Interview Transcript
*[TEMPLATE EXAMPLE - This is a fictional technical interview transcript for demonstration purposes]*

**Candidate:** Sarah Johnson  
**Interviewers:** Robert Chen (Lead Data Engineer), Lisa Martinez (Senior Analyst)  
**Date:** June 15, 2024  
**Duration:** 50 minutes  
**Position:** Senior Marketing Analyst

---

## Technical Assessment: Advanced SQL Skills

**Robert Chen:** Hi Sarah, thanks for joining us today. We'll be testing your SQL skills with scenarios similar to our daily work. I'm sharing our test database - you can see companies, passengers, passenger_trips, and trips tables.

**Sarah Johnson:** Perfect, I can see the schema. This looks like a flight booking system with a many-to-many relationship between passengers and trips.

**Robert Chen:** Exactly right. Let's start with something moderately complex. Can you write a query to find passengers who have taken 3 or more flights with the same company?

**Sarah Johnson:** Sure, I'll need to join through the passenger_trips bridge table and aggregate by passenger and company.

```sql
SELECT p.passenger_name, c.company_name, COUNT(*) as flight_count
FROM passengers p
JOIN passenger_trips pt ON p.passenger_id = pt.passenger_id
JOIN trips t ON pt.trip_id = t.trip_id
JOIN companies c ON t.company_id = c.company_id
GROUP BY p.passenger_id, p.passenger_name, c.company_id, c.company_name
HAVING COUNT(*) >= 3
ORDER BY flight_count DESC, p.passenger_name;
```

**Lisa Martinez:** Great! You included the proper grouping and ordering. Now let's make it more challenging. Can you find the most popular aircraft type for each company, handling ties properly?

**Sarah Johnson:** I'll use window functions to handle ties with RANK() instead of ROW_NUMBER().

```sql
WITH aircraft_popularity AS (
  SELECT 
    c.company_name,
    t.aircraft_type,
    COUNT(*) as flight_count,
    RANK() OVER (PARTITION BY c.company_id ORDER BY COUNT(*) DESC) as popularity_rank
  FROM companies c
  JOIN trips t ON c.company_id = t.company_id
  GROUP BY c.company_id, c.company_name, t.aircraft_type
)
SELECT company_name, aircraft_type, flight_count
FROM aircraft_popularity
WHERE popularity_rank = 1
ORDER BY company_name, flight_count DESC;
```

**Robert Chen:** Excellent use of CTE and window functions! Now let's test optimization knowledge. This query might be slow with millions of records. How would you optimize it?

**Sarah Johnson:** Several approaches:
1. **Indexes:** Composite index on (company_id, aircraft_type) and potentially (company_id, trip_id)
2. **Partitioning:** If we partition trips by date ranges, we could limit the scan
3. **Materialized views:** Pre-aggregate aircraft counts by company if this query runs frequently
4. **Query rewrite:** Depending on data distribution, we might use EXISTS instead of joins

**Lisa Martinez:** Perfect answer! Let's move to attribution scenarios. You'll work with this daily.

## Marketing Attribution Logic

**Lisa Martinez:** We have Google Analytics sessions and order data. Build a last-click attribution query, but override with influencer codes when present.

**Sarah Johnson:** I'll handle this step by step with CTEs for clarity:

```sql
WITH order_sessions AS (
  -- Get the last session before each order
  SELECT 
    o.order_id,
    o.user_id,
    o.order_time,
    o.promo_code,
    s.session_id,
    s.source,
    s.medium,
    s.campaign,
    ROW_NUMBER() OVER (
      PARTITION BY o.order_id 
      ORDER BY s.session_time DESC
    ) as session_rank
  FROM orders o
  LEFT JOIN sessions s ON o.user_id = s.user_id 
                      AND s.session_time < o.order_time
                      AND s.session_time >= o.order_time - INTERVAL '30 days'
),
last_click_attribution AS (
  SELECT 
    order_id,
    user_id,
    CASE 
      WHEN promo_code IS NOT NULL AND promo_code LIKE 'INFLUENCER_%' 
      THEN 'influencer'
      WHEN session_rank = 1 THEN source
      ELSE 'direct'
    END as attribution_source,
    CASE 
      WHEN promo_code IS NOT NULL AND promo_code LIKE 'INFLUENCER_%' 
      THEN promo_code
      WHEN session_rank = 1 THEN campaign
      ELSE NULL
    END as attribution_campaign
  FROM order_sessions
  WHERE session_rank = 1 OR session_rank IS NULL
)
SELECT * FROM last_click_attribution;
```

**Robert Chen:** Excellent! You handled edge cases like missing sessions and added the 30-day lookback window. What about performance considerations for this query?

**Sarah Johnson:** Key optimizations:
1. **Partitioned indexes** on sessions(user_id, session_time) 
2. **Date partitioning** on sessions table by month
3. **Consider incremental processing** - only recompute attribution for recent orders
4. **Materialized table** for historical attribution that doesn't change

## Complex Analytics Scenarios

**Lisa Martinez:** Here's a real scenario: Conversion rates dropped 40% yesterday but traffic stayed flat. Walk me through your debugging approach.

**Sarah Johnson:** I'd follow this systematic approach:

**1. Data Quality Checks:**
```sql
-- Compare daily metrics
SELECT 
  DATE(event_time) as date,
  COUNT(*) as total_events,
  COUNT(DISTINCT user_id) as unique_users,
  COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) as conversions,
  ROUND(100.0 * COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) / COUNT(*), 2) as conversion_rate
FROM events 
WHERE event_time >= CURRENT_DATE - 7
GROUP BY DATE(event_time)
ORDER BY date;

-- Check for data completeness
SELECT 
  COUNT(*) as total_records,
  COUNT(user_id) as non_null_users,
  COUNT(session_id) as non_null_sessions,
  COUNT(CASE WHEN event_type IS NULL THEN 1 END) as null_event_types
FROM events 
WHERE DATE(event_time) = CURRENT_DATE - 1;
```

**2. Technical Investigation:**
- Check ETL pipeline logs for failures
- Verify tracking code deployment times
- Look for bot traffic or data collection issues
- Examine conversion funnel step-by-step

**3. Business Context:**
- Site performance issues or downtime
- Payment processor problems
- UI/UX changes affecting checkout flow
- External factors (holidays, news events)

**Robert Chen:** Excellent systematic approach. What if the data looks clean but conversions are genuinely down?

**Sarah Johnson:** Then I'd investigate business factors:

```sql
-- Analyze conversion funnel breakdown
WITH funnel_analysis AS (
  SELECT 
    DATE(event_time) as date,
    COUNT(DISTINCT CASE WHEN event_type = 'page_view' THEN user_id END) as visitors,
    COUNT(DISTINCT CASE WHEN event_type = 'add_to_cart' THEN user_id END) as cart_adds,
    COUNT(DISTINCT CASE WHEN event_type = 'checkout_start' THEN user_id END) as checkout_starts,
    COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) as purchases
  FROM events 
  WHERE event_time >= CURRENT_DATE - 7
  GROUP BY DATE(event_time)
)
SELECT 
  date,
  visitors,
  ROUND(100.0 * cart_adds / visitors, 2) as cart_rate,
  ROUND(100.0 * checkout_starts / cart_adds, 2) as checkout_rate,
  ROUND(100.0 * purchases / checkout_starts, 2) as purchase_rate
FROM funnel_analysis
ORDER BY date;
```

This would help identify exactly where users are dropping off.

## Advanced Performance Optimization

**Robert Chen:** Last challenge. We have 100M records in our sessions table. This attribution query takes 45 minutes. How do you optimize it?

**Sarah Johnson:** Multi-pronged approach:

**1. Table Design:**
```sql
-- Partition sessions by month
CREATE TABLE sessions_partitioned (
  session_id BIGINT,
  user_id BIGINT,
  session_time TIMESTAMP,
  source VARCHAR(100)
) PARTITION BY RANGE (session_time);

-- Create monthly partitions with indexes
CREATE INDEX idx_sessions_user_time ON sessions_partitioned (user_id, session_time DESC);
```

**2. Query Optimization:**
```sql
-- Use EXISTS instead of joins for better performance
WITH recent_orders AS (
  SELECT order_id, user_id, order_time, promo_code
  FROM orders 
  WHERE order_time >= CURRENT_DATE - 1
),
order_attribution AS (
  SELECT 
    o.order_id,
    o.promo_code,
    (
      SELECT s.source 
      FROM sessions s 
      WHERE s.user_id = o.user_id 
        AND s.session_time < o.order_time
        AND s.session_time >= o.order_time - INTERVAL '30 days'
      ORDER BY s.session_time DESC 
      LIMIT 1
    ) as last_click_source
  FROM recent_orders o
)
SELECT * FROM order_attribution;
```

**3. Incremental Processing:**
- Only process new orders daily
- Store historical attribution in a separate table
- Use change data capture (CDC) for real-time updates

**Lisa Martinez:** Outstanding! Your performance optimization approach shows deep understanding of both query tuning and system architecture.

## Wrap-up & Assessment

**Robert Chen:** Sarah, this has been impressive. Your SQL skills are clearly advanced, and your systematic problem-solving approach is exactly what we need.

**Sarah Johnson:** Thank you! I really enjoyed working through these scenarios. They're much more complex than my current role, which is exactly what I'm looking for.

**Lisa Martinez:** Any questions about our tech stack or daily responsibilities?

**Sarah Johnson:** Yes, a couple:
1. Do you use DBT or similar tools for transformation pipelines?
2. What's your approach to data quality monitoring?
3. How do you handle real-time vs. batch processing decisions?

**Robert Chen:** Great questions - those show you're thinking about the broader data architecture. We use DBT extensively, have automated data quality checks, and carefully balance real-time vs. batch based on business requirements.

We'll discuss internally and get back to you soon. Thanks for a great technical session!

---

## Technical Interview Assessment

**SQL Proficiency:** 5/5 - Advanced skills, optimal query structure  
**Performance Optimization:** 5/5 - Deep understanding of indexing, partitioning  
**Attribution Logic:** 5/5 - Complex scenarios handled correctly  
**Problem-Solving:** 5/5 - Systematic, comprehensive approach  
**Window Functions:** 5/5 - Proper use of RANK vs ROW_NUMBER  
**Data Architecture:** 5/5 - Understands broader system implications  
**Communication:** 5/5 - Clear explanations of complex concepts  

**Overall Technical Fit:** Excellent - exceeds requirements, ready for immediate productivity

---

*Template Note: This interview demonstrates a strong candidate who exceeds technical requirements and shows advanced problem-solving capabilities. Use this to calibrate expectations for senior-level hires.* 

