-- count of customer_preference
SELECT COUNT(DISTINCT customer_name) AS total_customers,
       COUNT(DISTINCT CASE WHEN customer_preference = 'App' THEN customer_name END) AS app_users,
       COUNT(DISTINCT CASE WHEN customer_preference = 'Website' THEN customer_name END) AS Website_users
FROM customer_details;

-- preferred communication mode
SELECT communication_method, COUNT(*) AS total_customers
FROM customer_details
GROUP BY communication_method
ORDER BY total_customers DESC;

-- active and inactive customers
SELECT COUNT(DISTINCT customer_id CASE WHEN transaction_activity >= 1000 THEN customer_id) AS Active_customers,
       COUNT(DISTINCT customer_id CASE WHEN transaction_activity <= 100 THEN customer_id) AS Inactive_customers
FROM customer_details;


-- most active customer
SELECT customer_id AS customer, email AS email, MAX(transaction_activity) AS most_active
FROM customer_details;

-- group customers in the same vicinity
SELECT address, COUNT(customer_id) AS total_customers
FROM customer_details
GROUP BY address
ORDER BY total_customers DESC;

--select the communication mode of 10 active customers
SELECT customer_id, name, communication_method, transaction_activity as number_of_transactions
FROM customer_details
WHERE transaction_activity >= 1000
GROUP BY communication_method
ORDER BY transaction_activity DESC
LIMIT 10; 

-- select customers who transaction is between 3500 and 10000
SELECT customer_id, name, email, transaction_activity as number_of_transactions, communication_method
FROM customer_details
WHERE transaction_activity BETWEEN 3500 AND 10000
GROUP BY communication_method;

-- 
