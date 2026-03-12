'''
Crear la base de datos
agregar los datos del fichero json
'''

# Importar librerias necesarias
import sqlite3 as sql
import pandas as pd

# Abrir el CSV
df = pd.read_csv('data/datos_agrupados.csv')
# Creamos la base de datos y volcamos datos del CSV generado anteriormente
try:
    with sql.connect('database/datos_covid.db') as conn:
        df.to_sql('datos', conn, if_exists='replace', index=False)
except sql.Error as error:
    print(error)