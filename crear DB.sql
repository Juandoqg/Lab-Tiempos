-- Crear base de datos (puedes omitir si ya tienes una creada)
CREATE DATABASE IF NOT EXISTS tienda;
USE tienda;

-- Crear tabla clientes
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,                        -- [Columna A]
    genero TINYINT CHECK (genero IN (1, 2)),           -- [Columna B]
    edad TINYINT CHECK (edad BETWEEN 16 AND 85),       -- [Columna C]
    nivel_academico TINYINT CHECK (nivel_academico IN (1, 2, 3)),  -- [Columna D]
    estrato TINYINT CHECK (estrato BETWEEN 1 AND 5),   -- [Columna E]
    ciudad_residencia TINYINT CHECK (ciudad_residencia BETWEEN 1 AND 10), -- [Columna F]
    cant_hijos TINYINT CHECK (cant_hijos BETWEEN 0 AND 5),   -- [Columna G]
    num_salarios_minimos DECIMAL(3,1) CHECK (num_salarios_minimos BETWEEN 0 AND 10), -- [Columna H]
    pensionado TINYINT CHECK (pensionado IN (0, 1)),   -- [Columna I]
    tipo_tarjeta TINYINT CHECK (tipo_tarjeta IN (0, 1, 2)),   -- [Columna J]
    intension_tarjeta TINYINT CHECK (intension_tarjeta IN (0, 1)), -- [Columna K]
    cantidad_articulos_comprados TINYINT CHECK (cantidad_articulos_comprados BETWEEN 1 AND 25), -- [Columna L]
    tipo_articulo_mas_comprado TINYINT CHECK (tipo_articulo_mas_comprado BETWEEN 1 AND 50), -- [Columna M]
    mes_mas_compra TINYINT CHECK (mes_mas_compra BETWEEN 1 AND 12), -- [Columna N]
    compra_quincena TINYINT CHECK (compra_quincena IN (0, 1)), -- [Columna O]
    articulo_mayor_intension TINYINT CHECK (articulo_mayor_intension BETWEEN 1 AND 50) -- [Columna P]
);
