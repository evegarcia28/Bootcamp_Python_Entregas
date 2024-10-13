SELECT 
    rental.*, customer.*
FROM 
    rental
JOIN 
    customer ON rental.customer_id = customer.customer_id
WHERE 
    EXTRACT(YEAR FROM rental.rental_date) = 2005 
    AND EXTRACT(MONTH FROM rental.rental_date) = 5;