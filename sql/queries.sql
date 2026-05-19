/* =========================================================
   FOOD DELIVERY ANALYTICS - BUSINESS SQL QUERIES
   ========================================================= */


/* =========================================================
   1. DELIVERY PERFORMANCE BY HOUR
   ========================================================= */
SELECT 
    EXTRACT(HOUR FROM order_time) AS hour,
    COUNT(*) AS total_orders,
    AVG(TIMESTAMPDIFF(MINUTE, order_time, delivery_time)) AS avg_delivery_time,
    MIN(TIMESTAMPDIFF(MINUTE, order_time, delivery_time)) AS min_delivery_time,
    MAX(TIMESTAMPDIFF(MINUTE, order_time, delivery_time)) AS max_delivery_time
FROM orders
GROUP BY hour
ORDER BY hour;


/* =========================================================
   2. PEAK VS NON-PEAK ANALYSIS
   ========================================================= */
SELECT 
    CASE 
        WHEN EXTRACT(HOUR FROM order_time) BETWEEN 19 AND 22 THEN 'Peak'
        ELSE 'Non-Peak'
    END AS time_bucket,
    COUNT(*) AS total_orders,
    AVG(TIMESTAMPDIFF(MINUTE, order_time, delivery_time)) AS avg_delivery_time
FROM orders
GROUP BY time_bucket;


/* =========================================================
   3. DEMAND DISTRIBUTION (PERCENTAGE SHARE)
   ========================================================= */
SELECT 
    EXTRACT(HOUR FROM order_time) AS hour,
    COUNT(*) AS total_orders,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 
        2
    ) AS percentage_of_total_orders
FROM orders
GROUP BY hour
ORDER BY total_orders DESC;


/* =========================================================
   4. DISTANCE VS DELIVERY TIME (SEGMENTED)
   ========================================================= */
SELECT 
    CASE 
        WHEN distance_km < 3 THEN 'Short Distance'
        WHEN distance_km BETWEEN 3 AND 6 THEN 'Medium Distance'
        ELSE 'Long Distance'
    END AS distance_bucket,
    COUNT(*) AS total_orders,
    AVG(TIMESTAMPDIFF(MINUTE, order_time, delivery_time)) AS avg_delivery_time
FROM orders
GROUP BY distance_bucket;


/* =========================================================
   5. SLA BREACH ANALYSIS (CRITICAL KPI)
   ========================================================= */
SELECT 
    COUNT(*) AS total_orders,
    SUM(CASE 
        WHEN TIMESTAMPDIFF(MINUTE, order_time, delivery_time) > 45 
        THEN 1 ELSE 0 
    END) AS delayed_orders,
    ROUND(
        SUM(CASE 
            WHEN TIMESTAMPDIFF(MINUTE, order_time, delivery_time) > 45 
            THEN 1 ELSE 0 
        END) * 100.0 / COUNT(*), 
        2
    ) AS delay_percentage
FROM orders;


/* =========================================================
   6. CITY-LEVEL PERFORMANCE
   ========================================================= */
SELECT 
    city,
    COUNT(*) AS total_orders,
    AVG(TIMESTAMPDIFF(MINUTE, order_time, delivery_time)) AS avg_delivery_time
FROM orders
GROUP BY city
ORDER BY avg_delivery_time DESC;


/* =========================================================
   7. HIGH DEMAND VS DELAY (ROOT CAUSE)
   ========================================================= */
SELECT 
    EXTRACT(HOUR FROM order_time) AS hour,
    COUNT(*) AS total_orders,
    AVG(TIMESTAMPDIFF(MINUTE, order_time, delivery_time)) AS avg_delivery_time
FROM orders
GROUP BY hour
HAVING COUNT(*) > 50
ORDER BY total_orders DESC;


/* =========================================================
   8. EXPERIMENT ANALYSIS (A/B STYLE)
   ========================================================= */
SELECT 
    CASE 
        WHEN EXTRACT(HOUR FROM order_time) BETWEEN 19 AND 22 
        THEN 'Test_Group'
        ELSE 'Control_Group'
    END AS group_type,
    COUNT(*) AS total_orders,
    AVG(TIMESTAMPDIFF(MINUTE, order_time, delivery_time)) AS avg_delivery_time
FROM orders
GROUP BY group_type;