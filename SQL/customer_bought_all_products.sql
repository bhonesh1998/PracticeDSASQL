select customer_id from Customer GROUP BY customer_id having COUNT(DISTINCT product_key ) = (select count(product_key) from Product )
