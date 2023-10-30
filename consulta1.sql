-- Obtiene información de los proveedores cuyos productos pesan 1 kilogramo o menos.

-- Selecciono el identificador del proveedor, el nombre de la empresa, el tipo de productos,
-- la dirección, el número de teléfono principal, el número de teléfono secundario y el correo electrónico.
SELECT
    pr.id,
    pr.empresa,
    pr.tipo_producto,
    pr.direccion,
    pr.nro_tel_princ,
    pr.nro_tel_sec,
    pr.email
FROM
    public.proveedores pr

-- Realizo una unión (JOIN) con la tabla de productos.
JOIN
    public.productos p ON p.id_proveedor = pr.id

-- Aplico un filtro para seleccionar solo productos cuyo peso sea 1 kilogramo o menos.
WHERE
    p.peso <= 1.0;
