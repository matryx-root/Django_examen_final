-- Listado de productos cuyo proveedor es "Huella Natural."
SELECT
    p.codigo,
    p.nombre,
    p.marca,
    p.tipo
FROM
    public.productos p

-- Realizo una unión (JOIN) con la tabla de proveedores para filtrar por proveedor.
JOIN
    public.proveedores pr ON p.id_proveedor = pr.id

-- Aplico un filtro para seleccionar productos cuyo proveedor sea "Huella Natural."
WHERE
    pr.empresa = 'Huella Natural';
