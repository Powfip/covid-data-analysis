'''
Leer archivo CSV, agrupar por dia de la semana y por provincia
Guardar archivo en JSON
'''
# Importamos librerias necesarias
import pandas as pd

# Abrir el CSV
df = pd.read_csv('data/Proyecto 3.csv')

# Convertir a columna date a fecha
df['date'] = pd.to_datetime(df['date'])

# Agrupar por dia y provincia num_def, new_cases, num_hosp, num_uci
datos_agrupados = df.groupby(['date', 'province']).agg({'num_def': 'sum', 'new_cases': 'sum', 'num_hosp': 'sum', 'num_uci': 'sum'})
print(datos_agrupados.info())

# Generar un DataFrame con los datos agrupados
datos_agrupados_df = pd.DataFrame(datos_agrupados)

# Guardar el DataFrame en un archivo CSV
datos_agrupados_df.to_csv('data/datos_agrupados.csv')