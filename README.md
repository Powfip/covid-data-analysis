# 📊 COVID-19 Data Processing and Analysis (Spain)

Proyecto de análisis de datos desarrollado en **Python** que procesa información epidemiológica de COVID-19 a partir de un archivo CSV, limpia y transforma los datos con **Pandas**, y posteriormente almacena los resultados en una base de datos **SQLite** para realizar consultas analíticas.

El objetivo del proyecto es construir un pequeño **pipeline de datos modular**, desde la ingestión del dataset hasta la generación de consultas de análisis por provincia.

---

# 🚀 Tecnologías utilizadas

- Python 3
- Pandas
- SQLite
- SQL
- CSV
- Programación modular en Python

---

# 📂 Estructura del proyecto

```
covid-data-analysis/
│
├── data/
│   ├── Proyecto 3.csv
│   └── datos_agrupados.csv
│
├── database/
│   ├── datos_covid.db
│   
│
├── output/
│   ├── extraccion.py
│   ├── base_datos_covid.py|
│   ├── menu.py
│
└── main.py   
│
└── README.md
```

---

# ⚙️ Procesamiento de datos

El proyecto realiza los siguientes pasos:

## 1️⃣ Carga del dataset

Se importa un archivo CSV con datos de COVID-19.

```python
import pandas as pd

df = pd.read_csv("Proyecto 3.csv")
```

---

## 2️⃣ Limpieza y transformación

Se seleccionan únicamente las columnas relevantes para el análisis:

- `num_def` → número de defunciones  
- `new_cases` → nuevos casos  
- `num_hosp` → hospitalizados  
- `num_uci` → ingresos en UCI  

Posteriormente se guardan en un nuevo archivo CSV procesado.

```
datos_agrupados.csv
```

---

## 3️⃣ Creación de la base de datos

Los datos procesados se almacenan en una base de datos **SQLite**.

Tabla principal:

```
covid_stats
```

Columnas:

```
provincia
num_def
new_cases
num_hosp
num_uci
```

---

# 🔎 Consultas analíticas

Se implementaron varias consultas SQL para identificar las provincias con mayores indicadores sanitarios.

## Top 10 provincias con más defunciones

```sql
SELECT provincia, SUM(num_def) AS total_defunciones
FROM datos
GROUP BY provincia
ORDER BY total_defunciones DESC
LIMIT 10;
```

---

## Top 10 provincias con más nuevos casos

```sql
SELECT provincia, SUM(new_cases) AS total_nuevos_casos
FROM datos
GROUP BY provincia
ORDER BY total_nuevos_casos DESC
LIMIT 10;
```

---

## Top 10 provincias con más hospitalizados

```sql
SELECT provincia, SUM(num_hosp) AS total_hospitalizados
FROM datos
GROUP BY provincia
ORDER BY total_hospitalizados DESC
LIMIT 10;
```

---

## Top 10 provincias con más ingresos en UCI

```sql
SELECT provincia, SUM(num_uci) AS total_ingresos_en_uci
FROM datos
GROUP BY provincia
ORDER BY total_ingresos_en_uci DESC
LIMIT 10;
```

---

# 🧩 Modularización del proyecto

El código está dividido en varios módulos para mejorar la organización y reutilización:

| Módulo | Función |
|------|------|
| `extraccion.py` | Limpieza y transformación del CSV |
| `database.py` | Creación y conexión a SQLite |
| `menu.py` | Consultas SQL |
| `main.py` | Ejecución principal del programa |

---

# ▶️ Ejecución

1️⃣ Clonar el repositorio

```
git clone https://github.com/usuario/covid-data-analysis.git
```

2️⃣ Instalar dependencias

```
pip install pandas
```

3️⃣ Ejecutar el proyecto

```
python main.py
```

---

# 📈 Posibles mejoras

- Visualización de datos con **Matplotlib** o **Seaborn**
- Crear un dashboard con **Streamlit**
- Automatizar la descarga del dataset
- Añadir análisis temporal por fechas
- Exportar resultados a gráficos o informes

---

# 🎯 Objetivo del proyecto

Este proyecto fue desarrollado como práctica de **análisis e ingeniería de datos**, aplicando:

- procesamiento de datos con **Pandas**
- modelado simple en **SQLite**
- consultas analíticas en **SQL**
- organización de código modular en **Python**