import csv
import mysql.connector
import time

start = time.time()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tienda"
)
cursor = conn.cursor()

with open("clientes.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')  
    next(reader)  

    for i, row in enumerate(reader, start=2):
        if len(row) != 16:
            print(f"❌ Línea {i} tiene {len(row)} columnas: {row}")
            continue  

        try:
            cursor.execute("""
                INSERT INTO clientes (
                    id_cliente, genero, edad, nivel_academico, estrato, ciudad_residencia,
                    cant_hijos, num_salarios_minimos, pensionado, tipo_tarjeta,
                    intension_tarjeta, cantidad_articulos_comprados, tipo_articulo_mas_comprado,
                    mes_mas_compra, compra_quincena, articulo_mayor_intension
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, row)
        except mysql.connector.Error as e:
            print(f"⚠️ Error en línea {i}: {e}")

conn.commit()
cursor.close()
conn.close()

end = time.time()
print(f"✅ Carga completada en {end - start:.2f} segundos")
