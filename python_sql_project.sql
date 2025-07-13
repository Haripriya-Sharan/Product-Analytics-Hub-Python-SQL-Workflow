#To see the data structure
SELECT* FROM df_project;
DESCRIBE df_project;
SELECT COUNT(*) AS total_rows,
       COUNT(category) AS non_null_column_name
FROM df_project;

#Average, minimum and maximum actual and discount price in each categories
SELECT category,
   AVG(actual_price) AS avg_actual_price,
  MIN(actual_price) AS min_actual_price,
  MAX(actual_price) AS max_actual_price,
  AVG(discount_price) AS avg_discount_price,
  MIN(discount_price) AS min_discount_price,
  MAX(discount_price) AS max_discount_price
FROM df_project
GROUP BY category;

#Counting total number of headphnes and cameras
SELECT category, COUNT(*) AS product_count
FROM df_project
GROUP BY category
ORDER BY product_count DESC;

#Top 10 most expensive Cameras
SELECT category, name, actual_price
FROM df_project
WHERE category='Cameras'
ORDER BY actual_price DESC 
LIMIT 10;

#Top 10 most expensive Headphones
SELECT category, name, actual_price
FROM df_project
WHERE category='Headphones'
ORDER BY actual_price DESC 
LIMIT 10;

#Cameras with the highest discount percentage
SELECT name, discount_percentage, actual_price, discount_price
FROM df_project
WHERE category='Cameras'
ORDER BY discount_percentage DESC
LIMIT 10;

#Headphones with the highest discount percentage
SELECT name, discount_percentage, actual_price, discount_price
FROM df_project
WHERE category='Headphones'
ORDER BY discount_percentage DESC
LIMIT 10;

#Top-rated products by each category (with at least 100 reviews)
SELECT category, name, ratings, no_of_ratings
FROM (
    SELECT
        category,
        name,
        ratings,
        no_of_ratings,
        ROW_NUMBER() OVER (PARTITION BY category ORDER BY ratings DESC) AS rn
    FROM df_project
    WHERE no_of_ratings >= 100
) ranked
WHERE rn <= 10
ORDER BY category, ratings DESC;

#Count of products by rating bin:
SELECT rating_bin, COUNT(*) AS count
FROM df_project
GROUP BY rating_bin;

-- Selects the top 10 "High" rated Headphones priced below the average,
-- ordered by number of ratings (descending)
WITH avg_price_cte AS (
    SELECT AVG(actual_price) AS avg_price FROM df_project
)
SELECT *
FROM df_project, avg_price_cte
WHERE actual_price < avg_price_cte.avg_price and category='Headphones'
  AND rating_bin = 'High'
  ORDER BY no_of_ratings DESC
  LIMIT 10;
  
  -- Selects the top 10 "High" rated Cameras priced below the average,
-- ordered by number of ratings (descending)
WITH avg_price_cte AS (
    SELECT AVG(actual_price) AS avg_price FROM df_project
)
SELECT *
FROM df_project, avg_price_cte
WHERE actual_price < avg_price_cte.avg_price and category='Cameras'
  AND rating_bin = 'High'
  ORDER BY no_of_ratings DESC
  LIMIT 10;
  



