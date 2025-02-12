-- Total Sales per Product
SELECT product, SUM(quantity * price) AS total_sales 
FROM sales 
GROUP BY product;

-- Total Quantity Sold per Product
SELECT product, SUM(quantity) AS total_quantity 
FROM sales 
GROUP BY product;

-- Sales Trend Over Time
SELECT date, SUM(quantity * price) AS daily_revenue 
FROM sales 
GROUP BY date 
ORDER BY date ASC;
