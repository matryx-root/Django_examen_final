-- Listado de clientes que utilizan Hotmail como servidor de correo.
SELECT
    c.nombre,
    c.apellido,
    c.email
FROM
    public.clientes c

-- Aplico un filtro para seleccionar clientes cuyo correo contiene "hotmail."
WHERE
    LOWER(c.email) LIKE '%hotmail%';