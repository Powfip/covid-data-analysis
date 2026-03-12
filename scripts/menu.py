'''
Crear consultas de Provincia con más defunciones, nuevos casos, hospitalizados y UCIs
Crear Menú infinito con las consultas
'''

import sqlite3 as sql

# Función para consulta de más defunciones por provincia
def defunciones_por_provincia():
    with sql.connect('database/datos_covid.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT province, SUM(num_def) AS total_defunciones
                       FROM datos
                       GROUP BY province
                       ORDER BY total_defunciones DESC
                       LIMIT 10
                       ''')
        resultado_total = cursor.fetchall()
        print("\n"+"="*50)
        print("10 PROVINCIAS CON MÁS DEFUNCIONES:")
        print("="*50)
        for provincia, dato in resultado_total:
            print(f"{provincia}: {dato}")

# Función para consulta de nuevos casos por provincia
def nuevos_casos_por_provincia():
    with sql.connect('database/datos_covid.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT province, SUM(new_cases) AS total_nuevos_casos
                       FROM datos
                       GROUP BY province
                       ORDER BY total_nuevos_casos DESC
                       LIMIT 10
                       ''')
        resultado_total = cursor.fetchall()
        print("\n"+"="*50)
        print("10 PROVINCIAS CON MÁS NUEVOS CASOS:")
        print("="*50)
        for provincia, dato in resultado_total:
            print(f"{provincia}: {dato}")

# Función consulta de más hospitalizados por provincia
def hospitalizados_por_provincia():
    with sql.connect('database/datos_covid.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT province, SUM(num_hosp) AS total_hospitalizados
                       FROM datos
                       GROUP BY province
                       ORDER BY total_hospitalizados DESC
                       LIMIT 10
                       ''')
        resultado_total = cursor.fetchall()
        print("\n"+"="*50)
        print("10 PROVINCIAS CON MÁS HOSPITALIZADOS:")
        print("="*50)
        for provincia, dato in resultado_total:
            print(f"{provincia}: {dato}")

# Función consulta de más UCIs por provincia
def ingresos_uci_por_provincia():
    with sql.connect('database/datos_covid.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT province, SUM(num_uci) AS total_uci
                       FROM datos
                       GROUP BY province
                       ORDER BY total_uci DESC
                       LIMIT 10
                       ''')
        resultado_total = cursor.fetchall()
        print("\n"+"="*50)
        print("10 PROVINCIAS CON MÁS INGRESOS EN UCIS:")
        print("="*50)
        for provincia, dato in resultado_total:
            print(f"{provincia}: {dato}")



def main():
    while True:
        opcion = int(input('''
            ¿Qué consulta desea realizar?
            1. 10 provincias con más defunciones
            2. 10 provincias con más nuevos casos
            3. 10 provincias con más hospitalizados
            4. 10 provincias con más ingresos en UCIs
            5. Salir
                        '''))
        if opcion == 1:
            defunciones_por_provincia()
        elif opcion == 2:
            nuevos_casos_por_provincia()
        elif opcion == 3:
            hospitalizados_por_provincia()
        elif opcion == 4:
            ingresos_uci_por_provincia()
        elif opcion == 5:
            print("Adiós")
            break
        else:
            print('Opción inválida. Por favor, inténtelo de nuevo.')