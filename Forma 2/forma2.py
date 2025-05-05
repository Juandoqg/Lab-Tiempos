import pandas as pd
import mysql.connector
import time

start = time.time()

# Leer CSV separado por ;
df = pd.read_csv("clientes.csv", delimiter=';')

# Validar que tenga 16 columnas
if df.shape[1] != 16:
    raise ValueError(f"❌ El archivo tiene {df.shape[1]} columnas. Se esperaban 16.")

# Convertir a tipos nativos de Python
data = [tuple(map(lambda x: x.item() if hasattr(x, "item") else x, row)) for row in df.values]

# Conexión a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tienda"
)
cursor = conn.cursor()

# Inserciones en lotes más pequeños (por ejemplo, 500 registros a la vez)
batch_size = 50
for i in range(0, len(data), batch_size):
    batch = data[i:i + batch_size]
    cursor.executemany("""
        INSERT INTO clientes (
            id_cliente, genero, edad, nivel_academico, estrato, ciudad_residencia,
            cant_hijos, num_salarios_minimos, pensionado, tipo_tarjeta,
            intension_tarjeta, cantidad_articulos_comprados, tipo_articulo_mas_comprado,
            mes_mas_compra, compra_quincena, articulo_mayor_intension
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, batch)

    conn.commit()  # Confirma los cambios en cada lote

cursor.close()
conn.close()

end = time.time()
print(f"✅ Tiempo de ejecución: {end - start:.2f} segundos")
