SELECT 
    table_name AS "Tabla",
    column_name AS "Columna",
    data_type AS "Tipo de Dato",
    is_nullable AS "¿Puede ser nulo?"
FROM 
    information_schema.columns
WHERE 
    table_schema = 'public' 
AND table_name IN('actor','store','address','category','city','country','customer',
'film_actor','film_category','inventory','language','rental','staff','payment','film')
ORDER BY table_name ASC;