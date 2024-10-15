SELECT title, release_year, rental_rate FROM public.film 
WHERE release_year=2006 AND rental_rate>4.0
ORDER BY film_id ASC;