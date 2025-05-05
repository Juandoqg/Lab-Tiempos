import mysql.connector
import time

start = time.time()

# Ruta archivoo
csv_file_path = 'clientes.csv'  

# Conexión a MySQL, habilitando `local_infile` en la conexión
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tienda",
    connection_timeout=3600,  
    allow_local_infile=True    
)
cursor = conn.cursor()

# Ejecutar el comando LOAD DATA LOCAL INFILE
query = f"""
    LOAD DATA LOCAL INFILE '{csv_file_path}'
    INTO TABLE clientes
    FIELDS TERMINATED BY ';'        -- Delimitador de campos
    LINES TERMINATED BY '\n'        -- Delimitador de líneas
    IGNORE 1 LINES                 -- Ignorar la primera línea con los encabezados
    (id_cliente, genero, edad, nivel_academico, estrato, ciudad_residencia,
    cant_hijos, num_salarios_minimos, pensionado, tipo_tarjeta,
    intension_tarjeta, cantidad_articulos_comprados, tipo_articulo_mas_comprado,
    mes_mas_compra, compra_quincena, articulo_mayor_intension);
"""

cursor.execute(query)

conn.commit()


cursor.close()
conn.close()

end = time.time()
print(f"✅ Tiempo de ejecución: {end - start:.2f} segundos")
