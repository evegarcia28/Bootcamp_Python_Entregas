SELECT 
    rental.rental_id, rental.rental_date, rental.inventory_id, rental.customer_id,
	customer.first_name, customer.last_name, customer.email
FROM 
    rental
JOIN 
    customer ON rental.customer_id = customer.customer_id
WHERE 
    EXTRACT(YEAR FROM rental.rental_date) = 2005 
    AND EXTRACT(MONTH FROM rental.rental_date) = 5;